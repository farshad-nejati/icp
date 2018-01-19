from ipc import *
import os
import operator

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
    dev_extractor = DevExtractor()


if False:
    DictionaryManager.train()
    IOManager.save_obj(DictionaryManager.dictionary_list, 'data')
    print(DictionaryManager.dictionary_list)


if False:
    dictionary = IOManager.load_obj('data')
    temp = 0
    size = 0
    for f in os.listdir(DEVSET_DIRNAME):
        file_path = os.path.join(DEVSET_DIRNAME, f)
        if os.path.isfile(file_path):
            vector, score = IRClassifier.get_class(file_path, dictionary)
            max_score = max(score.items(), key=operator.itemgetter(1))[0]
            file_info = IOManager.info_extractor(file_path)
            size = size + 1
            if file_info['poet'] == max_score:
                temp = temp + 1
            if size % 100 == 0:
                print(size)
    print(temp / size * 100)
