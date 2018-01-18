from ipc import *
import os

if False:
    dev_extractor = DevExtractor()

if False:
    d = os.path.abspath(os.path.join(os.path.dirname(__file__), 'dataset/raw_dataset/frdvsi-Fourth-9929.txt'))
    poem = PoemTokenizer.tokenize_poem(d)
    print(poem)
