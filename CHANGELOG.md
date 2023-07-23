<!--next-version-placeholder-->

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
