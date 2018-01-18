import os
import shutil
import errno


class IOManager:
    def __init__(self):
        pass

    @staticmethod
    def init_directories(filename):
        try:
            os.makedirs(filename)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

    @staticmethod
    def copy_file(src, dest):
        try:
            shutil.copy(src, dest)
        except shutil.Error as e:
            print('Error: %s' % e)
        except IOError as e:
            print('Error: %s' % e.strerror)

    @staticmethod
    def read_file(filename):
        with open(filename, 'r') as content_file:
            content = content_file.read()
        return content
