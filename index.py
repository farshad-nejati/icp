from ipc import *
import os

if False:
    dev_extractor = DevExtractor()

if False:
    d = os.path.abspath(os.path.join(os.path.dirname(__file__), 'dataset/raw_dataset/frdvsi-Fourth-9929.txt'))
    poem = PoemTokenizer.tokenize_poem(d)
    print(poem)

if False:
    d = os.path.abspath(os.path.join(os.path.dirname(__file__), 'dataset/raw_dataset/frdvsi-Fourth-9929.txt'))
    print(IOManager.info_extractor(d))

if False:
    d = {
        'word1': {
            'ferdoosi': 3,
            'sadi': 5,
        },
        'word2': {
            'ferdoosi': 6,
            'sadi': 4,
        },
    }
    io = IOManager.save_obj(d, 'data')
    s = IOManager.load_obj('data')
    print(s['word2'])
