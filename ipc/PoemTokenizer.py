from __future__ import unicode_literals
from hazm import *
from .IOManager import *


class PoemTokenizer:

    @staticmethod
    def tokenize_poem(poem):
        poem_content = IOManager.read_file(poem)
        return word_tokenize(poem_content)
