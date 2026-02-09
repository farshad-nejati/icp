## Persian Classical Poetry Author Classifier (`ipc`)

This repository contains a small information‑retrieval–style classifier for Persian classical poetry.  
Given a corpus of poems labeled by poet, it builds a token dictionary and then classifies new poems by estimating which poet is the most likely author.

The core implementation lives in the `ipc` package:

- **`DevExtractor`**: splits a raw corpus into training and development sets.
- **`DictionaryManager`**: scans the training set and builds a token dictionary with per‑poet frequencies and document frequency (`df`) for each token.
- **`IOManager`**: handles filesystem operations such as reading poems, copying files, and saving/loading Python objects with `pickle`.
- **`PoemTokenizer`**: tokenizes Persian poems using `hazm.word_tokenize`.
- **`Poet`**: provides the list of supported poets and keeps track of the number of poets.
- **`IRClassifier`**: implements a simple IR‑based classifier that:
  - tokenizes the input poem,
  - computes TF‑IDF weights for tokens that exist in the trained dictionary,
  - accumulates scores per poet and returns both the per‑poet score vector and the detailed token weights.

### Project Structure

- `ipc/`
  - `DevExtractor.py` – dataset splitting utilities
  - `DictionaryManager.py` – training and dictionary construction
  - `IOManager.py` – file I/O and object persistence
  - `IRClassifier.py` – TF‑IDF–based classification logic
  - `PoemTokenizer.py` – Hazm‑based tokenization
  - `Poet.py` – poet metadata
- `dataset/` (expected, not included here)
  - `raw_dataset/` – original labeled poems
  - `trainset/` – generated training subset
  - `devset/` – generated development subset
- `obj/` – pickled Python objects (created at runtime)

### Dataset Format

The system expects each poem to be stored in a separate text file.  
File names must follow this pattern:

```text
<poet>-<century>-<poem_id>.txt
```

For example:

```text
hafz-08-00123.txt
```

`IOManager.info_extractor` parses file names into:

- `poet` – poet identifier (e.g. `hafz`)
- `century` – an arbitrary century code
- `poem_id` – poem identifier within the poet’s works

The `Poet` class currently defines an internal mapping of supported poets and their corpus sizes. You should keep the poet identifiers in file names consistent with those keys.

### Requirements

This project uses Python 3 and the following external libraries:

- `hazm` – Persian NLP toolkit (for tokenization).

Install dependencies, for example:

```bash
pip install hazm
```

### Usage Overview

1. **Prepare the raw dataset**
   - Place all labeled poem files in `dataset/raw_dataset/` following the naming convention above.

2. **Split into train and dev sets**
   - Use `DevExtractor` to create `dataset/trainset/` and `dataset/devset/`.  
     By default, it copies every *n*-th file (e.g. every 5th) to the dev set and the rest to the train set.

3. **Train the dictionary**
   - Call `DictionaryManager.train()` to:
     - iterate over all files in `dataset/trainset/`,
     - tokenize each poem with `PoemTokenizer`,
     - update the global `dictionary_list` with token frequencies per poet and document frequency.
   - Optionally persist the trained dictionary using `IOManager.save_obj`.

4. **Classify a poem**
   - Load or build a dictionary (as produced by `DictionaryManager`).
   - Use `IRClassifier.get_class(file_path, dictionary)` with the path to a poem file:
     - the method returns a `vector` (per‑poet TF‑IDF weights) and a `score` dictionary mapping poet → total score.
   - The poet with the highest score can be treated as the predicted author.

### Example (Pseudo‑Code)

```python
from ipc.DevExtractor import DevExtractor
from ipc.DictionaryManager import DictionaryManager
from ipc.IOManager import IOManager
from ipc.IRClassifier import IRClassifier

# 1) Create train/dev splits from raw_dataset
DevExtractor()  # uses default ratio inside the class

# 2) Train dictionary on trainset
DictionaryManager.train()
dictionary = DictionaryManager.dictionary_list
IOManager.save_obj(dictionary, "dictionary")

# 3) Later, load dictionary and classify a poem
dictionary = IOManager.load_obj("dictionary")
vector, scores = IRClassifier.get_class("path/to/poem.txt", dictionary)
predicted_poet = max(scores, key=scores.get)
print(predicted_poet, scores[predicted_poet])
```

### Notes

- This is a simple research/educational implementation and does not perform any advanced preprocessing such as stemming, stop‑word removal, or normalization beyond what `hazm` provides.
- The training and classification procedures operate on files; make sure your dataset directories and file names follow the expected structure.