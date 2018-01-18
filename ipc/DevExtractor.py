import os
import shutil

import errno

RAW_DATASET_DIRNAME = os.path.abspath(os.path.join(os.path.dirname(__file__), '../raw_dataset', ))
DATASET_DIRNAME = os.path.abspath(os.path.join(os.path.dirname(__file__), '../dataset', ))
DEVSET_DIRNAME = os.path.abspath(os.path.join(os.path.dirname(__file__), '../dataset/devset', ))
TRAINSET_DIRNAME = os.path.abspath(os.path.join(os.path.dirname(__file__), '../dataset/trainset', ))

'''

'''


class DevExtractor:
    def __init__(self):
        self.__count_files = 0
        self.create_dataset(5)

    def create_dataset(self, ratio_number):
        try:
            os.makedirs(DATASET_DIRNAME)
            os.makedirs(DEVSET_DIRNAME)
            os.makedirs(TRAINSET_DIRNAME)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

        temp = 1
        for f in os.listdir(RAW_DATASET_DIRNAME):
            file_path = os.path.join(RAW_DATASET_DIRNAME, f)
            if os.path.isfile(file_path) and temp % ratio_number == 0:
                self.copyFile(file_path, DEVSET_DIRNAME)
            else:
                self.copyFile(file_path, TRAINSET_DIRNAME)
            temp = temp + 1

    def copyFile(self, src, dest):
        try:
            shutil.copy(src, dest)
        except shutil.Error as e:
            print('Error: %s' % e)
        except IOError as e:
            print('Error: %s' % e.strerror)
