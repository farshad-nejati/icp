from ipc import IOManager
from math import log10
from hazm import word_tokenize
from .Poet import *


class IRClassifier:
    score = {}
    vector = {}

    @staticmethod
    def get_class(file_path, dictionary):
        content = IOManager.read_file(file_path=file_path)
        poets = Poet.get_poets()
        for poet in poets:
            IRClassifier.score[poet] = 0
        token_set = set(word_tokenize(content))
        token_list = list(token_set)
        for token in token_list:
            if token in dictionary:
                IRClassifier.calculate_score_vector(token, dictionary, poets)

        return IRClassifier.vector, IRClassifier.score

    @staticmethod
    def get_tf_idf(tf, df):
        weight_tf = 1 + log10(int(tf))
        weight_idf = log10(Poet.poets_counts / int(df))
        tf_idf = weight_tf * weight_idf
        return tf_idf

    @staticmethod
    def calculate_score_vector(token, dictionary, poets):
        token_dictionary = dictionary[token]
        df = token_dictionary['df']

        for poet in poets:
            if poet in token_dictionary:
                tf = token_dictionary[poet]
                tf_idf = IRClassifier.get_tf_idf(tf, df)

                if poet not in IRClassifier.vector:
                    IRClassifier.vector[poet] = {}

                IRClassifier.vector[poet][token] = tf_idf
                IRClassifier.score[poet] = IRClassifier.score[poet] + tf_idf
