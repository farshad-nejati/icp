from .PoemTokenizer import *

TRAINSET_DIRNAME = os.path.abspath(os.path.join(os.path.dirname(__file__), '../dataset/trainset'))


class DictionaryManager:
    dictionary_list = {}

    @staticmethod
    def train():
        temp = 1
        if temp == 1:
            print("Training...")
        for f in os.listdir(TRAINSET_DIRNAME):
            file_path = os.path.join(TRAINSET_DIRNAME, f)
            if os.path.isfile(file_path):
                DictionaryManager.training(file_path)
            if temp % 1000 == 0:
                print(temp, "file TRAINED!!!")
                if temp != 1:
                    print("Training...")
            temp = temp + 1
        print("Done.")

    # def test_data(self):
    #     return {
    #         'بوم': {
    #             'df': '2',
    #             'sadi': '10',
    #             'molavi': '3'
    #         },
    #         'آباد': {
    #             'df': '2',
    #             'sadi': '10',
    #             'molavi': '3'
    #         },
    #         'گشتند': {
    #             'df': '2',
    #             'sadi': '10',
    #             'molavi': '3'
    #         },
    #     }

    @staticmethod
    def training(file_path):

        file_tokens = PoemTokenizer.tokenize_poem(file_path)
        file_info = IOManager.info_extractor(file_path)
        poet = file_info['poet']

        for token_index in range(len(file_tokens)):
            single_token = file_tokens[token_index]

            if single_token in DictionaryManager.dictionary_list:
                exist_token = DictionaryManager.dictionary_list[single_token]
                DictionaryManager.add_element_to_dictionary(exist_token, poet)
            else:
                DictionaryManager.create_new_dictionary_element(single_token, poet)

    @staticmethod
    def add_element_to_dictionary(exist_token, poet):
        if poet in exist_token:
            exist_token[poet] = str(int(exist_token[poet]) + 1)
        else:
            exist_token[poet] = 1
            exist_token['df'] = str(int(exist_token['df']) + 1)

    @staticmethod
    def create_new_dictionary_element(single_token, poet):
        DictionaryManager.dictionary_list[single_token] = {
            'df': '1',
            poet: '1'
        }
