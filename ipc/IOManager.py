import os
import shutil
import errno


class IOManager:
    def __init__(self):
        pass

    @staticmethod
    def init_directories(folder_name):
        try:
            os.makedirs(folder_name)
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
    def read_file(file_path):
        with open(file_path, 'r') as content_file:
            content = content_file.read()
        return content

    @staticmethod
    def info_extractor(file_path):
        filename = os.path.basename(file_path)
        filename = os.path.splitext(filename)[0]
        poet, century, poem_id = filename.split('-')
        return {'poem_id': poem_id, 'poet': poet, 'century': century}
