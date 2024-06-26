<!--next-version-placeholder-->

## v0.18.0 (2024-03-29)

### Feature

* **methodology:** Add detailed explanation for Aspect-Based Sentiment Analysis and Generative language models application ([`49f87bd`](https://github.com/entelecheia/corporate-reputation/commit/49f87bd35b78ebaa5823dcf8aba45cd0132e451f))

### Fix

* **dependencies:** Update python and hyfi versions; update thematos version ([`671ae1b`](https://github.com/entelecheia/corporate-reputation/commit/671ae1b7104e17ee87b046b1cbfa87a3c3dd2790))

### Documentation

* **implementation:** Refine methodology detail ([`685f3e3`](https://github.com/entelecheia/corporate-reputation/commit/685f3e3520e7b78f553af1b24526e313996c4593))
* **book:** Un-comment implementation chapter in table of contents ([`c070ae7`](https://github.com/entelecheia/corporate-reputation/commit/c070ae78d1e69ef673c4856eba068f1363266404))
* **book:** Add implementation details to the book paper ([`e98572c`](https://github.com/entelecheia/corporate-reputation/commit/e98572c88a27806730cec7a20e6da3b4a4d412e8))

## v0.17.0 (2023-09-09)

### Feature

* **pipeline:** Add datasets save predictions configuration ([`d29c1d2`](https://github.com/entelecheia/corporate-reputation/commit/d29c1d2e85c4539ad138c4b1db19715cd1fb2aac))
* **config:** Add datasets-save-predictions.yaml ([`bb93396`](https://github.com/entelecheia/corporate-reputation/commit/bb9339626f63d17f87f0e0bcb794aa48adb80c1f))

## v0.16.0 (2023-09-04)

### Feature

* **corprep-runner:** Add corprep-gpt4-train_year agent ([`2d7e1c5`](https://github.com/entelecheia/corporate-reputation/commit/2d7e1c5c262d8abc9a10d05e1e80d6785c7cf3ae))

### Fix

* **dependencies:** Upgrade hyfi-absa to 0.4.0 ([`5dc8ca8`](https://github.com/entelecheia/corporate-reputation/commit/5dc8ca89df94355050f9fa50bb2c2d6a48b4b0bb))

## v0.15.0 (2023-09-04)

### Feature

* **corprep-gpt3.yaml:** Add newsId to configuration ([`623012f`](https://github.com/entelecheia/corporate-reputation/commit/623012f82412b2ef507d81e2845e87f2b360d12d))
* **corprep:** Update text parsing instructions ([`42d7134`](https://github.com/entelecheia/corporate-reputation/commit/42d7134599bc5b52568913aee7ce7092cf0472f4))
* **workflow:** Add corprep-runner.yaml config file ([`d9b7ff7`](https://github.com/entelecheia/corporate-reputation/commit/d9b7ff76ea49652e93a9660c5ae36a0000649f8f))
* **config:** Add input_filename attribute to corprep-gpt3-sample.yaml, use input_filename for file path ([`6dd5b65`](https://github.com/entelecheia/corporate-reputation/commit/6dd5b653d65abecddcba9fd648b8bc6dfe628578))

### Fix

* **dependencies:** Upgrade hyfi to 1.32.1, lexikanon to 0.6.4 and hyfi-absa to 0.3.3 ([`82f72bb`](https://github.com/entelecheia/corporate-reputation/commit/82f72bbbbe0ba965f4c89db3b2153a50cb302ef6))

## v0.14.0 (2023-08-08)

### Feature

* **runner:** Add new corprep-gpt4-train_2019.yaml configuration file. ([`444b8c9`](https://github.com/entelecheia/corporate-reputation/commit/444b8c96f9f13e4e01105d6dd77241bd2fc4315e))
* **pipeline:** Add dataframe_select_columns task to datasets.yaml ([`2f796d7`](https://github.com/entelecheia/corporate-reputation/commit/2f796d715bf6f5f75c2a35ac620628aaeb94ad45))
* **corprep.yaml:** Add datasets-filter-year to pipeline, add filter_year variable ([`dc215a7`](https://github.com/entelecheia/corporate-reputation/commit/dc215a7c74d84075fbe4a10672a7d7c714ff70b8))
* **pipeline:** Add datasets filter configuration ([`db5f422`](https://github.com/entelecheia/corporate-reputation/commit/db5f422045e2e1b694e5beee2d4786b4196486b7))

## v0.13.0 (2023-08-07)

### Feature

* **corprep:** Add remove_columns function to dataset config ([`dd89120`](https://github.com/entelecheia/corporate-reputation/commit/dd89120d9101a66a3266fdc2ddc64b0bca707447))
* **workflow:** Add datasets-save pipeline ([`7a9f1d1`](https://github.com/entelecheia/corporate-reputation/commit/7a9f1d18c70289d967c6dcb97a30edb4ae20fc29))
* **pipeline:** Add dataset_remove_columns to datasets.yaml ([`9cdb2c8`](https://github.com/entelecheia/corporate-reputation/commit/9cdb2c8fd90fae12e3097858add7d6f75f745d55))
* **pipeline:** Add new pipeline for saving datasets ([`eff2232`](https://github.com/entelecheia/corporate-reputation/commit/eff22324ca986b40f2282d00da8bda005aeffa7e))

### Fix

* **config:** Correct dataset_path in corprep-gpt3-sample.yaml ([`837b9d9`](https://github.com/entelecheia/corporate-reputation/commit/837b9d95378b5fae902527ade24b25e88fd998db))
* **dependencies:** Upgrade lexikanon to 0.5.2 ([`44fa3df`](https://github.com/entelecheia/corporate-reputation/commit/44fa3df588b7a1cfbed53f8dc42d55ce8e5d379e))
* **dependencies:** Upgrade hyfi to 1.20.1 ([`b95917d`](https://github.com/entelecheia/corporate-reputation/commit/b95917d9508b5b14fe73818c8f69c550fcd691e0))

## v0.12.2 (2023-08-04)

### Fix

* **pipeline:** Replace find_similar_docs_ac with find_similar_docs_by_clustering in datasets, change column names in datasets-similar.yaml ([`78ad328`](https://github.com/entelecheia/corporate-reputation/commit/78ad3284dcd656e36e3dfbd4879501d5358812b8))
* **pipeline:** Update tokenizer parameter name ([`f96b9b1`](https://github.com/entelecheia/corporate-reputation/commit/f96b9b1af799675a21b2115e07cdf41d364c4630))

## v0.12.1 (2023-08-04)

### Fix

* **tokenizer:** Update stopwords path in kakao config ([`8158062`](https://github.com/entelecheia/corporate-reputation/commit/815806279beecd43f1a1909edafa577f0283fabe))
* **pipeline:** Increase sample size and adjust worker count, remove specific columns from removal list ([`28529da`](https://github.com/entelecheia/corporate-reputation/commit/28529da1a766a44993e97601e8616d2a3c75a8cd))
* **workflow:** Enable noun and similar pipelines ([`f242a63`](https://github.com/entelecheia/corporate-reputation/commit/f242a63172bad13521fc5fcc0e38ee0a92b16042))
* **pipeline:** Update filter_dataset to filter_and_sample_data ([`1e97c46`](https://github.com/entelecheia/corporate-reputation/commit/1e97c4655d40221105fb81392c3b20ae4fedb9b6))
* **pipeline:** Change num_samples to sample_size in datasets-test.yaml ([`c9ba5cb`](https://github.com/entelecheia/corporate-reputation/commit/c9ba5cbe76d3911a7518956091e6aedcad51833b))
* **pipeline:** Rename num_samples to sample_size in datasets-similar config ([`2cdc541`](https://github.com/entelecheia/corporate-reputation/commit/2cdc5413420042ec0f55167212a383c594fc21c7))
* **pipeline:** Change num_samples to sample_size in datasets-noun configuration ([`5c32059`](https://github.com/entelecheia/corporate-reputation/commit/5c32059407d8d71d35b4ff257290fcfbabfa61c9))
* **pipeline:** Add sample filename in datasets filter config ([`b0609d0`](https://github.com/entelecheia/corporate-reputation/commit/b0609d0ac71de93f81df14c25f3d6c4e14b2d33b))

## v0.12.0 (2023-08-03)

### Feature

* **corprep:** Add revision1 for more detailed sentiment task description ([`03edfb2`](https://github.com/entelecheia/corporate-reputation/commit/03edfb2c669cb691927b5bcd66c10e32839e4185))

## v0.11.0 (2023-08-03)

### Feature

* **config/runner:** Add new configuration files for GPT3 and GPT4 ([`6d83abc`](https://github.com/entelecheia/corporate-reputation/commit/6d83abc7d1ed48ce088c8fa135355f1359faf6e2))
* **pipeline:** Add new dataset filter and load steps ([`441e063`](https://github.com/entelecheia/corporate-reputation/commit/441e063c7d8ab923fcf5e017a04bc6cb2b0dfddd))
* **corprep:** Add filter pipeline in config and comment out noun and similar pipelines ([`6bbd818`](https://github.com/entelecheia/corporate-reputation/commit/6bbd818c635303a07a6a979513ce94e847867d75))
* **filter:** Add verbose print statements. ([`08cf03e`](https://github.com/entelecheia/corporate-reputation/commit/08cf03ea14cf5d17856c87ea1d6bd222e785faae))
* **corprep:** Add filter_dataset configuration files ([`6edb66f`](https://github.com/entelecheia/corporate-reputation/commit/6edb66f6f1462703a8dbc26efa8c5b19f19cb69f))
* **corprep/datasets:** Add filter functionality to datasets ([`3a2835a`](https://github.com/entelecheia/corporate-reputation/commit/3a2835ab2e10b6bb3fccdf0c1e7bb7fc8dc55cc1))

## v0.10.0 (2023-08-03)

### Feature

* **config/runner:** Add new gpt3 and gpt4 test configuration files ([`be6e168`](https://github.com/entelecheia/corporate-reputation/commit/be6e168ec944d8634b697c40e5f7e2692551341f))
* **corprep-conf-runner:** Add corprep-gpt3 and corprep-gpt4 configuration files ([`c82df5e`](https://github.com/entelecheia/corporate-reputation/commit/c82df5e068236c1eba8a6920a2a18d71ddd2ed69))
* **corprep:** Add gpt3 and gpt4 agent configurations ([`b2a52cd`](https://github.com/entelecheia/corporate-reputation/commit/b2a52cdb0227da2f011fdeda2e36d68a9e23a1b3))
* **corprep:** Add config for TRIPLE and QUAD tasks in prompts ([`cd8d7e4`](https://github.com/entelecheia/corporate-reputation/commit/cd8d7e42df41ea8a079873b2e51904f400422a10))

## v0.9.3 (2023-08-03)

### Fix

* **corprep:** Add secrets directory initialization ([`0bce74f`](https://github.com/entelecheia/corporate-reputation/commit/0bce74ffede7569b36b51760a8b53738648120e9))
* **pipeline:** Replace dataframe_save with save_dataframes, remove redundant dataframe_save and save_dataframes files ([`666226a`](https://github.com/entelecheia/corporate-reputation/commit/666226a430272cbcc9f38c776fb360e298411020))
* **dependencies:** Upgrade hyfi to 1.13.0 ([`41eb5e8`](https://github.com/entelecheia/corporate-reputation/commit/41eb5e8ac93c7da18c1353284707f9d7b4c355b9))

## v0.9.2 (2023-07-30)

### Fix

* **corprep:** Add hyabsa to plugins ([`6dbea3f`](https://github.com/entelecheia/corporate-reputation/commit/6dbea3f402c0c94c1fced6f2f4856aef3fb6b8f9))
* **dependencies:** Upgrade hyfi to 1.12.5 and add hyfi-absa 0.1.0 ([`b0c679c`](https://github.com/entelecheia/corporate-reputation/commit/b0c679c6b3a9bd2577329f9bf74ea67c5024e2c4))

## v0.9.1 (2023-07-28)

### Fix

* **dependencies:** Upgrade hyfi to 1.12.1 ([`21c83f5`](https://github.com/entelecheia/corporate-reputation/commit/21c83f5ae591290b150c058e4b14121171345b47))
* **pipeline:** Rename dataset_load_raw to load_raw_dataset, add file_pattern and set verbose to false ([`74cd0c2`](https://github.com/entelecheia/corporate-reputation/commit/74cd0c2f54e05aaea8db28bcd3884e190151bab2))
* **corprep:** Add load_raw_dataset configuration ([`fa0b9be`](https://github.com/entelecheia/corporate-reputation/commit/fa0b9be9f3b4add371805a78103465783712197b))
* **corprep:** Remove specific tasks and columns in absa_agent_predict.yaml ([`2debf24`](https://github.com/entelecheia/corporate-reputation/commit/2debf2483a332adf05058f78cd9ee1c7970de091))
* **absa_agent_predict:** Add null value to pipe_obj_arg_name property ([`99a6473`](https://github.com/entelecheia/corporate-reputation/commit/99a64730b0b3152215d7b420f89769d37086f421))
* **find_similar_docs:** Rename to find_similar_docs_ac.yaml ([`fc62043`](https://github.com/entelecheia/corporate-reputation/commit/fc620431873dd40b9a7b63dcf2bc9db3f0dc4404))
* **pipeline:** Rename dataset related functions for clarity ([`90ab34e`](https://github.com/entelecheia/corporate-reputation/commit/90ab34eaa656a6c1a138c4e74dcbf086c890ec61))
* **pipeline:** Reduce defaults in absa-kakao and gpt35 configurations ([`91b4e7c`](https://github.com/entelecheia/corporate-reputation/commit/91b4e7c29493b1eae5b6141a7493aa8fe4aff19a))
* **dependencies:** Upgrade lexikanon to 0.3.2, thematos to 0.2.1 ([`85257e4`](https://github.com/entelecheia/corporate-reputation/commit/85257e499f9b70b96b39e17d213e427a703b64c6))
* **corprep:** Add 'cluster' column to DataFrame in similar_docs functions ([`1903b6f`](https://github.com/entelecheia/corporate-reputation/commit/1903b6ff12996ecf70c677e9df5493d866e792a4))

## v0.9.0 (2023-07-27)

### Feature

* **corprep:** Add thematos plugin ([`45ae7f3`](https://github.com/entelecheia/corporate-reputation/commit/45ae7f333d76629fe746319109048f3c30b19bbc))
* **pyproject:** Add thematos dependency ([`6253d99`](https://github.com/entelecheia/corporate-reputation/commit/6253d99e8e94e1dfd34c2b4a16f9e84ad8780498))
* **book:** Add data.md in supplementary with filtering details ([`a8ed8ca`](https://github.com/entelecheia/corporate-reputation/commit/a8ed8ca6a0f65f09f3effc5391ab80e9ce04f385))
* **corprep:** Add dataset_to_pandas and pandas_print_head configuration files ([`834f55b`](https://github.com/entelecheia/corporate-reputation/commit/834f55b536cc7821a6725dab926f6a139ec83ead))
* **similarity.py:** Add multiple data-processing and plotting functions, switch clustering method from DBSCAN to Agglomerative Clustering ([`4f38cba`](https://github.com/entelecheia/corporate-reputation/commit/4f38cba731d27845f4da8861cdd5b76b57138112))
* **corprep:** Add yaml configurations for saving dataframes ([`5e5b235`](https://github.com/entelecheia/corporate-reputation/commit/5e5b235d1fd36d0068e82687717bba39872cf3c3))
* **corprep:** Add find_similar_docs configuration ([`c468597`](https://github.com/entelecheia/corporate-reputation/commit/c4685976e225967ff7cec3e24820ab0d18a912d9))
* **config:** Add new pipeline and task configuration for dataset simulation ([`3710f93`](https://github.com/entelecheia/corporate-reputation/commit/3710f93d574a08a8a2b942c7b1ec8a721e963893))

## v0.8.0 (2023-07-26)

### Feature

* **corprep:** Add run configurations for absa_agent_predict, filter_dataset and load_raw_dataset ([`7290fca`](https://github.com/entelecheia/corporate-reputation/commit/7290fcaadecf67e492cfb73f7e2370697b05d794))
* **workflow:** Add datasets-test configuration file ([`b612cc4`](https://github.com/entelecheia/corporate-reputation/commit/b612cc4aa8890a62e4e6241675b16a526a2623e7))
* **pipeline/config:** Enhance datasets.yaml ([`28a6108`](https://github.com/entelecheia/corporate-reputation/commit/28a61087aae57f6eb5591eb8bb8e9623af4e0622))
* **tokenize:** Add extract_tokens function to handle part-of-speech tagging ([`c6482fb`](https://github.com/entelecheia/corporate-reputation/commit/c6482fb1b69a6b54d4034df856a8e93f0bed2f2a))
* **corprep:** Add dataset_extract_nouns configuration, add dataset_extract_tokens configuration ([`5ddf017`](https://github.com/entelecheia/corporate-reputation/commit/5ddf017f49e61c7bbd171c6cabde4786f1ee5ecc))
* **tokenizer:** Add kakao configuration ([`9ae964f`](https://github.com/entelecheia/corporate-reputation/commit/9ae964ffebd0153bdffca32864b7a7b881d7e0dc))
* **pipeline:** Add extract tokens step with kakao tokenizer config ([`04e66d2`](https://github.com/entelecheia/corporate-reputation/commit/04e66d217c1790d8ca46470ae5aa118c45c53eaa))

### Fix

* **workflow:** Add workflow_name field to workflows ([`f9dfb5b`](https://github.com/entelecheia/corporate-reputation/commit/f9dfb5b67ba2b7ce444aa7381901c0269acca35c))
* **dependencies:** Upgrade hyfi to 1.9.4 ([`98e0228`](https://github.com/entelecheia/corporate-reputation/commit/98e02289983ecc7778e59cf5d149af0374cb41c0))

## v0.7.1 (2023-07-25)

### Fix

* **corprep:** Replace package name with path ([`adb8932`](https://github.com/entelecheia/corporate-reputation/commit/adb893278c152f2d6965469cbf4e197ed29fe27f))
* **dependencies:** Upgrade hyfi to 1.9.3 and lexikanon to 0.2.3 ([`1dd2766`](https://github.com/entelecheia/corporate-reputation/commit/1dd2766602bd09118684667c75d33812006c33fc))

## v0.7.0 (2023-07-24)

### Feature

* **tokenize:** Add load_from_cache_file option ([`f4e0057`](https://github.com/entelecheia/corporate-reputation/commit/f4e0057be857537a953cf94059bd644d2a99ef65))
* **pipeline:** Add load from cache option in tokenizer config ([`9617708`](https://github.com/entelecheia/corporate-reputation/commit/96177083e3140b7de138ab019f5a7e6fa2ea24b5))
* **corprep:** Add lexikanon plugin to HyFI initialization ([`2fe976a`](https://github.com/entelecheia/corporate-reputation/commit/2fe976ab53702422050618be95ba85da9e8aee67))

### Fix

* **dependencies:** Upgrade hyfi to 1.9.0 and ekonlpy to 2.0.1 ([`f53fa18`](https://github.com/entelecheia/corporate-reputation/commit/f53fa18dc188b9188577c3a7b8278144fdeabbb9))

## v0.6.0 (2023-07-23)

### Feature

* **tests:** Add tokenizer test in corprep module ([`5487cf7`](https://github.com/entelecheia/corporate-reputation/commit/5487cf7608628ea897682ab62101b5b03f746dd6))
* **corprep/datasets:** Add similarity.py file with similarity analysis functions ([`708e79f`](https://github.com/entelecheia/corporate-reputation/commit/708e79feabdc5cbb95c60172b928972363b8e417))
* **tokenizer:** Add strip_pos option to SimpleTokenizer configuration ([`7fc3991`](https://github.com/entelecheia/corporate-reputation/commit/7fc39910a6b45b55d72c4b4cd62f951f32f0a784))
* **corprep:** Add tokenizer_config_name and token_col to dataset tokenize configuration ([`4691e71`](https://github.com/entelecheia/corporate-reputation/commit/4691e71460c316ed2cbbddaef29ec4fad7e29b3b))
* **config/task:** Add new datasets-tokenize.yaml file ([`c3f2af5`](https://github.com/entelecheia/corporate-reputation/commit/c3f2af5762cd5f5f71a714c20230d64be8edc44c))
* **pipeline:** Create datasets-tokenize.yaml for tokenization in pipeline ([`743b8d7`](https://github.com/entelecheia/corporate-reputation/commit/743b8d765de0aa769c7e23d78e9a0a6969dca66d))
* **tokenizer:** Add flatten option to MecabTokenizer config ([`070740b`](https://github.com/entelecheia/corporate-reputation/commit/070740b61798d23ab7de37bbdeb0e2c11c4d96eb))
* **tokenizer:** Add new tokenizer configurations for SimpleTokenizer, MecabTokenizer, NLTKTokenizer, add new tagger configurations for mecab and nltk ([`26496c1`](https://github.com/entelecheia/corporate-reputation/commit/26496c1c6dd40a4f65d085d8b10053e19a06405a))
* **tokenizer:** Add new tokenizer classes and methods ([`df773b9`](https://github.com/entelecheia/corporate-reputation/commit/df773b9c1d68835a68e4e1575f9fc67c7b6998fb))
* **tokenizer:** Add hanja table loading function ([`b420649`](https://github.com/entelecheia/corporate-reputation/commit/b42064991ca9b4555350e7b9467b8bc5cc1edc59))
* **tests:** Add stopwords test in tokenizer ([`30335b3`](https://github.com/entelecheia/corporate-reputation/commit/30335b379f5c21ae684d81a381e60406348be857))
* **tokenizer:** Add stopwords functionality ([`073a176`](https://github.com/entelecheia/corporate-reputation/commit/073a176068c2262dee11cea3d56eace8b1d3206c))
* **corprep:** Add new stopwords configuration ([`bb79233`](https://github.com/entelecheia/corporate-reputation/commit/bb79233ba198e0690efaced848d28f6347642051))
* **pyproject.toml:** Add nltk dependency ([`cf00d4c`](https://github.com/entelecheia/corporate-reputation/commit/cf00d4c3ad621a1b34faafe78c9cf827cc8ded3b))
* **corprep:** Add new configuration files for text normalization ([`ce82466`](https://github.com/entelecheia/corporate-reputation/commit/ce824660ed8eb5f3703826e56dc637a13619729c))
* **normalizer:** Add new configurations for text normalization ([`ac53a45`](https://github.com/entelecheia/corporate-reputation/commit/ac53a45356eae16e8f4a770b85ca9687628e168e))
* **corprep:** Add new about information ([`bf79ee0`](https://github.com/entelecheia/corporate-reputation/commit/bf79ee0cfeab4c0ff69a2cc501ee312c1d94d345))
* **corprep/resources/dictionaries/mecab:** Add new ekon_v1.dic file ([`d408222`](https://github.com/entelecheia/corporate-reputation/commit/d408222785369eea7ce8b8d7d805c5944aa03bbb))
* **tokenizer:** Add utils for text normalization and string metrics ([`6b1d818`](https://github.com/entelecheia/corporate-reputation/commit/6b1d8184433717d51b962bc227b448fd4a9b4330))
* **tokenizer:** Add hangle encoder with normalization and decomposition functions ([`afe155b`](https://github.com/entelecheia/corporate-reputation/commit/afe155b1436c39ee7d5ab8906bc097bb43f27a28))
* **corprep/tokenizer/hanja:** Add new translation functions and character handling for Hangul and Hanja ([`490c763`](https://github.com/entelecheia/corporate-reputation/commit/490c763cfe1311216f356bd6ac4737e760f2e51b))
* **tokenizer:** Add normalizer.py with normalizer functionality ([`8e579aa`](https://github.com/entelecheia/corporate-reputation/commit/8e579aae696f0ba395865266637244d5e47092c5))
* **dependencies:** Add scikit-learn version 1.3.0 ([`6c34d44`](https://github.com/entelecheia/corporate-reputation/commit/6c34d44ad5156f543ef49369756587b994239f56))

### Fix

* **pipeline:** Correct typo in tokenize step ([`c9158d8`](https://github.com/entelecheia/corporate-reputation/commit/c9158d8a0b9f4c63c865f0b3149afbcad84af18c))
* **NLTKTokenizer:** Modify parse method return type ([`48ee9cd`](https://github.com/entelecheia/corporate-reputation/commit/48ee9cdd4283a998214ce97133f11adc0a5765d7))
* **corprep:** Streamline main function and import statements ([`11533a2`](https://github.com/entelecheia/corporate-reputation/commit/11533a2f793b5771f87d27a9cffe07fed0070ca3))
* **corprep:** Change how HyFi is initialized and used ([`c2e0344`](https://github.com/entelecheia/corporate-reputation/commit/c2e03440e8f9856878865a6c8b4dfa94cffd7d29))

## v0.5.0 (2023-07-20)

### Feature

* **config:** Add new configuration files for absa, pipeline, task, and workflow ([`0883120`](https://github.com/entelecheia/corporate-reputation/commit/0883120369d3e7d2726fc31cdda8712382f4017c))

### Documentation

* Update URL from Github pages to subdomain ([`f6b5f59`](https://github.com/entelecheia/corporate-reputation/commit/f6b5f59beb2acf938001dd08c02549cb4d6a19fa))

## v0.4.0 (2023-07-19)

### Feature

* **corprep:** Add new absa workflow configuration ([`c0fb068`](https://github.com/entelecheia/corporate-reputation/commit/c0fb068cf3bb0961aeb71cee464602377840f692))
* **corprep:** Add gpt35 pipeline to absa task configuration ([`d6c2fe8`](https://github.com/entelecheia/corporate-reputation/commit/d6c2fe8fe008a8040c5a7cdd1871bbf853af60dd))
* **pipeline:** Add new absa-kakao-gpt35.yaml configuration file ([`594c317`](https://github.com/entelecheia/corporate-reputation/commit/594c317202695d64260cf92ee7bbd85474c070b7))
* **corprep:** Add new gpt35.yaml configuration file for ABSA task ([`ceb35ab`](https://github.com/entelecheia/corporate-reputation/commit/ceb35ab00a3e6f337d34e333b94b9269024eed9d))

### Fix

* **absa/config:** Handle additional exceptions in call_api function ([`7a53ed4`](https://github.com/entelecheia/corporate-reputation/commit/7a53ed4e3e2c16fdd5bc4970e0832f36c9d0fc70))
* **corprep:** Handle api responses and modify related functions ([`3400a26`](https://github.com/entelecheia/corporate-reputation/commit/3400a260fe18a9afd648ae9f6f76f35c3ecc4676))
* **corprep/absa:** Handle InvalidRequestError in call_api function ([`4d70fbf`](https://github.com/entelecheia/corporate-reputation/commit/4d70fbf5d4d8e699909d1de1b41d4b26689f2370))
* **corprep/datasets:** Add number of samples logging ([`872879c`](https://github.com/entelecheia/corporate-reputation/commit/872879c772970ff2b01914f2c9d1205a332dab60))
* **absa:** Adjust agent call function and return structure ([`d10ad61`](https://github.com/entelecheia/corporate-reputation/commit/d10ad6135e4f31b0e77365cdfb19b281105d3121))

## v0.3.0 (2023-07-19)

### Feature

* **corprep:** Add absa-kakao pipeline configuration ([`bc1418d`](https://github.com/entelecheia/corporate-reputation/commit/bc1418d4726620d65d28865b4f079a6bd8971066))
* **corprep:** Add absa_agent_predict configuration file ([`62ef975`](https://github.com/entelecheia/corporate-reputation/commit/62ef97578c19f0b55b58d7c5f1069701eb44a2ed))
* **absa/prompts:** Add default.yaml configuration for TRIPLE and QUAD tasks ([`1c72bff`](https://github.com/entelecheia/corporate-reputation/commit/1c72bff6a424087023eac3f9dabfe22fd2d8de1b))
* **corprep:** Add new absa default configuration ([`68b6a58`](https://github.com/entelecheia/corporate-reputation/commit/68b6a58e738ac3078e21c2350b1649340f109015))
* **corprep/absa:** Add config module with API logic and data models ([`623bc76`](https://github.com/entelecheia/corporate-reputation/commit/623bc76fb9d6f9de7a59057ea33ac742ccb7dd3a))
* **corprep/absa:** Add agent module with predict functionalities ([`1e9285b`](https://github.com/entelecheia/corporate-reputation/commit/1e9285b6dbbf9e36274dcaf0da206494043d7996))
* **corprep/absa:** Add new file__init__.py ([`32dc886`](https://github.com/entelecheia/corporate-reputation/commit/32dc886d6d86eb530cdd96e0a31b74bc9c63a501))
* **corprep:** Add dataset_load and absa configurations ([`f40c599`](https://github.com/entelecheia/corporate-reputation/commit/f40c59927204ee0cab7b1920bcd3e0d2222b2392))
* **corprep:** Add absa task ([`653e525`](https://github.com/entelecheia/corporate-reputation/commit/653e525b5dc7b0ddef41bfc7f6aeed3bd772d573))
* **corprep/datasets/io.py:** Add load_dataset function ([`3cb4294`](https://github.com/entelecheia/corporate-reputation/commit/3cb4294351b7a355a4e9b150a5972685543c177d))
* **pipe:** Add dataset_sample and a second dataset_save to steps ([`57cc25c`](https://github.com/entelecheia/corporate-reputation/commit/57cc25cb4bf35994eec1fd0d4efa26cd890ca692))
* **corprep:** Add sample_dataset function and related configuration ([`4b64a40`](https://github.com/entelecheia/corporate-reputation/commit/4b64a40f6866b0332439127a2687e405378fc7d0))
* **pipeline:** Add tokenize step to datasets pipeline ([`1536430`](https://github.com/entelecheia/corporate-reputation/commit/15364302b9563cf54900bb83585de588afa2aee1))
* **corprep:** Add new file for tokenizing dataset ([`6fb827e`](https://github.com/entelecheia/corporate-reputation/commit/6fb827e2041f063363eb32e112b28bb7dce5849b))
* **corprep/datasets/preprocessing:** Add tokenize_dataset function ([`2db1824`](https://github.com/entelecheia/corporate-reputation/commit/2db1824baabb8ecb5afb37f7a303e4efae59970c))

### Fix

* **.tasks.toml:** Lower coverage fail threshold to 1% ([`b2b7718`](https://github.com/entelecheia/corporate-reputation/commit/b2b77188a10c0d4a47b3d40534358cee0df64806))
* **corprep:** Introduce setLogger for HyFI ([`c78e6e2`](https://github.com/entelecheia/corporate-reputation/commit/c78e6e24c11d2b3bdba2053e7d9bf66df0efe60f))
* **datasets:** Add path and file_pattern parameters to load_raw_dataset ([`2bf977b`](https://github.com/entelecheia/corporate-reputation/commit/2bf977b96c126cc165cae59079f1b5284ced584a))
* **dependencies:** Upgrade hyfi to 1.2.14 ([`ca9ac2b`](https://github.com/entelecheia/corporate-reputation/commit/ca9ac2b1864e00bc7b9f4b896e669c573e7d0e9c))

## v0.2.0 (2023-07-17)

### Feature

* **corprep:** Add save_dataset pipe ([`b7a3dff`](https://github.com/entelecheia/corporate-reputation/commit/b7a3dff1d7a29015f986a618c2159db1dc5994d5))
* **corprep:** Add save_raw_dataset configuration ([`7e331d2`](https://github.com/entelecheia/corporate-reputation/commit/7e331d2be8bdeafcd11c2d15b6aebb16e0777249))
* **corprep:** Add datasets.yaml configuration for pipeline ([`4cf7bd4`](https://github.com/entelecheia/corporate-reputation/commit/4cf7bd44f72a96f10ea7e88d63306c237812e7ee))
* **corprep:** Add new project configuration file ([`be8890d`](https://github.com/entelecheia/corporate-reputation/commit/be8890d3e7f4623eb6fc19013f3a101b112c4c65))
* **corprep:** Add new configuration file ([`4cdf806`](https://github.com/entelecheia/corporate-reputation/commit/4cdf8065ac4f5cb94ac7c616629fc2cd5e469ce9))
* **datasets:** Add function to save raw datasets ([`8a5319c`](https://github.com/entelecheia/corporate-reputation/commit/8a5319c443607d946103262f2bf00eb5e48dd348))
* **datasets:** Create corprep/datasets/__init__.py file ([`5808b35`](https://github.com/entelecheia/corporate-reputation/commit/5808b35df0944d42a2969cd92cb260a8e7e4f6e1))

### Fix

* **corprep:** Add global_workspace_name to yaml config file ([`ffe0c12`](https://github.com/entelecheia/corporate-reputation/commit/ffe0c126ab89f4366c5e7a2781284f6c6109e0e7))
* **dependencies:** Upgrade hyfi to 1.2.13 ([`d1b7658`](https://github.com/entelecheia/corporate-reputation/commit/d1b7658ca6fff488e54772cc61a213f435fe9243))
* **dependencies:** Upgrade hyfi to 1.2.10 ([`68314de`](https://github.com/entelecheia/corporate-reputation/commit/68314de361efb6ea3c391423e6893cf166eb8de9))
* **datasets:** Add Dataset import to raw.py ([`c959747`](https://github.com/entelecheia/corporate-reputation/commit/c95974736c15b232a531009be0c276d91b258dc7))
* **dependencies:** Upgrade hyfi to 1.2.7 ([`82ab4e6`](https://github.com/entelecheia/corporate-reputation/commit/82ab4e6e89e61e1d98f0d5fa99c6604643e9004f))
* **dependencies:** Upgrade hyfi to 1.2.6 ([`cfb2f3f`](https://github.com/entelecheia/corporate-reputation/commit/cfb2f3fd3daddcb3d7c8c5b3188c4e45f48953e0))

### Documentation

* **book:** Add new sections (introduction, literature, methodology, results, conclusion, supplementary materials) ([`e1f0aaf`](https://github.com/entelecheia/corporate-reputation/commit/e1f0aaf7dfa97f8ac82da880e532677423c3cb2b))

## v0.1.2 (2023-07-11)

### Fix

* **dependencies:** Upgrade hyfi to 1.2.2 ([`dfdc822`](https://github.com/entelecheia/corporate-reputation/commit/dfdc8228ae24c3929d0e47d3521313efbd077f64))

## v0.1.1 (2023-06-28)

### Fix

* **dependencies:** Upgrade hyfi to 0.15.0 ([`cc9463b`](https://github.com/entelecheia/corporate-reputation/commit/cc9463b3114cbfc31603da961338bd2900b2aaa1))

## v0.1.0 (2023-06-07)

### Feature

* Initial version ([`6b5cee9`](https://github.com/entelecheia/corporate-reputation/commit/6b5cee938a1315eb4aa313b03579047bd2918ba1))

### Fix

* Initial version ([`1a33102`](https://github.com/entelecheia/corporate-reputation/commit/1a3310267ec0ade0a94e6f549abaefb50186fab9))
