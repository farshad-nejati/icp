from .IOManager import *

DATASET_DIRNAME = os.path.abspath(os.path.join(os.path.dirname(__file__), '../dataset'))
RAW_DATASET_DIRNAME = os.path.abspath(os.path.join(os.path.dirname(__file__), '../dataset/raw_dataset'))
DEVSET_DIRNAME = os.path.abspath(os.path.join(os.path.dirname(__file__), '../dataset/devset'))
TRAINSET_DIRNAME = os.path.abspath(os.path.join(os.path.dirname(__file__), '../dataset/trainset'))


class DevExtractor:
    def __init__(self):
        self.create_dataset(5)

    def create_dataset(self, ratio_number):
        IOManager.init_directories(DEVSET_DIRNAME)
        IOManager.init_directories(TRAINSET_DIRNAME)
        temp = 1
        print("Extracting...")
        for f in os.listdir(RAW_DATASET_DIRNAME):
            file_path = os.path.join(RAW_DATASET_DIRNAME, f)
            if os.path.isfile(file_path) and temp % ratio_number == 0:
                IOManager.copy_file(file_path, DEVSET_DIRNAME)
            else:
                IOManager.copy_file(file_path, TRAINSET_DIRNAME)
            temp = temp + 1
        print("Done.")
