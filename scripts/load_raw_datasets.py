# %% [markdown]
# # Preprocessing Datasets
#
# %%
from datasets import Dataset
from ekonlpy.tag import Mecab  # type: ignore

from corprep import HyFI  # type: ignore

prj = HyFI.init_project(
    project_name="esg-coverage",
    task_name="datasets",
    project_root=HyFI.find_dotenv_dir(usecwd=True),
    log_level="DEBUG",
    verbose=True,
)

print("project directory:", prj.root_dir)
print("project workspace directory:", prj.workspace_dir)
print("Global dataset directory:", prj.path.glboal_dataset_dir)
# %%
raw_news_dir = prj.path.glboal_dataset_dir / "raw/daum_news_20230707"
raw_data_files = []
if raw_news_dir.exists():
    raw_data_files = HyFI.get_filepaths(f"{raw_news_dir}/*.dat")
    print(raw_data_files[:3])
else:
    print("No raw data files found.")

# %%
dataset = HyFI.load_dataset("json", data_files=raw_data_files)
ds_train: Dataset = dataset["train"]  # type: ignore
print(f"Number of training samples: {len(ds_train)}")
# %%
print(ds_train.features)
# %%
text = ds_train["bodyText"][0]
print(text)


# %%
# Define the POS tagging function for batch processing
def pos_tagging(batch):
    mecab = Mecab()
    batch_tags = []
    for text in batch["bodyText"]:
        sentences = text.split("\n")
        pos_tags = []
        for sentence in sentences:
            pos_tags.extend(mecab.pos(sentence))
        batch_tags.append(pos_tags)
    return {"pos_tags": batch_tags}


# Apply the POS tagging function
ds_train = ds_train.map(pos_tagging, num_proc=10, batched=True)


# Print the first 10 samples
print(ds_train.select(range(10))["pos_tags"])

print(ds_train[0]["pos_tags"])
# %%
ds_train.features


# %%
# Define the company checking function
def check_company(batch):
    batch_checks = []
    company_names = ["카카오", "다음카카오"]
    for pos_tags in batch["pos_tags"]:
        checks = any(
            tag in ["NNG", "NNP"] and word in company_names for word, tag in pos_tags
        )
        batch_checks.append(checks)

    return {"company_check": batch_checks}


# Apply the subject checking function
ds_train = ds_train.map(check_company, num_proc=10, batched=True)

# %%
# filter out the samples that do not contain the company name
ds_filtered = ds_train.filter(lambda example: example["company_check"])

# %%
# Print the first 10 samples
print(ds_train.select(range(10))["bodyText"])


# %%
def check_noun_subject(example):
    pos_tags = example["pos_tags"]
    subjects = []

    for i in range(len(pos_tags) - 1):
        word, tag = pos_tags[i]
        next_word, next_tag = pos_tags[i + 1]
        if tag == "NNG" and next_tag == "JX" and next_word in ["은", "는", "이", "가"]:
            subjects.append(word)

    return {"subj_check": bool(subjects)}


# Apply the subject checking function
ds_train = ds_train.map(check_noun_subject, num_proc=10, batched=True)
