import glob
import os.path
from unidecode import  unidecode
import glob
import os.path
import math
from unidecode import unidecode


def kmers(s, k=3):
    """Generates k-mers for an input string."""
    for i in range(len(s)-k+1):
        yield s[i:i+k]

def relative_kmers_frequency(languageItem):
    dictionary = {}
    list_length = len(languageItem.kmers_list)
    for item in languageItem.kmers_set:
        item_freq = languageItem.kmers_list.count(item)
        relative_freq = item_freq / list_length
        dictionary.update({item: relative_freq})
    return dictionary

def cosine_similarity(langItemOne, langItemTwo):
    intersection = langItemOne.kmers_set.intersection(langItemTwo.kmers_set)
    scalar_product = 0
    lenght_multiply_one = 0
    lenght_multiply_two = 0
    for item in intersection:
        value_one = langItemOne.freq_dict.get(item)
        value_two = langItemTwo.freq_dict.get(item)
        scalar_product = scalar_product + (value_one * value_two)
        lenght_multiply_one = lenght_multiply_one + math.pow(value_one)
        lenght_multiply_two = lenght_multiply_two + math.pow(value_two)
    lenght_multiply_one = math.sqrt(lenght_multiply_one)
    lenght_multiply_two = math.sqrt(lenght_multiply_two)
    similarity = scalar_product / (lenght_multiply_one*lenght_multiply_two)
    return similarity

class LanguageItem:
    def __init__(self, data):
        """Initialize the clustering"""
        self.data = data
        self.freq_dict = {}
        self.kmers_set = set()
        self.kmers_list = []

if __name__ == "__main__":
    corpus = {}
    languages_dict = {}
    for file_name in glob.glob("languages\\TempLangugaes\\*"):
        name = os.path.splitext(os.path.basename(file_name))[0]
        text = unidecode(" ".join([line.strip() for line in open(file_name, "rt", encoding="utf8").readlines()]))
        text = text.lower()
        corpus[name] = text
        triples = list(kmers(text))
        lg = LanguageItem(text)
        lg.kmers_set = set(triples)
        lg.kmers_list = triples
        lg.freq_dict = relative_kmers_frequency(lg)
        languages_dict[name] = lg

    cosine_similarity(languages_dict.get("blg"),languages_dict.get("mkj"))





