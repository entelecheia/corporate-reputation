import multiprocessing as mp

import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def process_week(weekly_data):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(weekly_data["tokenizedText"])
    similarity_matrix = cosine_similarity(tfidf_matrix)

    # Perform DBSCAN clustering on the similarity matrix
    db = DBSCAN(eps=0.8, min_samples=2, metric="precomputed", n_jobs=-1)
    db.fit(similarity_matrix)

    # For each cluster, get the index of the document with the earliest createdDt
    df = pd.DataFrame(
        {"cluster": db.labels_, "createdDt": weekly_data.index},
        index=weekly_data["newsId"],
    )
    earliest_doc_indices = df.groupby("cluster")["createdDt"].idxmin().values

    return weekly_data.loc[earliest_doc_indices]


def filter_similar_docs(dataset):
    num_cores = mp.cpu_count()
    pool = mp.Pool(num_cores)

    # Convert the HuggingFace dataset to a pandas DataFrame
    dataset = dataset.to_pandas()

    # Convert the createdDt column to datetime and set it as the index
    dataset["createdDt"] = pd.to_datetime(dataset["createdDt"])
    dataset.set_index("createdDt", inplace=True)

    # Split the dataset into weekly chunks for multiprocessing
    weeks = [g for n, g in dataset.groupby(pd.Grouper(freq="W"))]

    # Process each week in parallel
    filtered_weeks = pool.map(process_week, weeks)

    # Concatenate the results into a single filtered dataset
    filtered_dataset = pd.concat(filtered_weeks)

    pool.close()
    pool.join()

    return filtered_dataset


# Use the function as follows
# dataset is your HuggingFace dataset
# filtered_dataset = filter_similar_docs(dataset)
