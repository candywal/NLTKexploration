import re
import sys
import random
import nltk
from nltk.corpus import udhr

def read_file(file_name):
    with open(file_name, 'r') as f:
        text = f.read()
    return text

def preprocess(text):
    text = re.sub(r'[^\w\s]', '', text)
    text = text.lower()
    return text

def calculate_frequency(text):
    languages = {'afrikaans': 0, 'danish': 0, 'dutch': 0, 'english': 0, 'french': 0, 'german': 0, 
                 'indonesian': 0, 'italian': 0, 'spanish': 0, 'swedish': 0}
    nltklangs = ['Afrikaans-Latin1', 'Danish_Dansk-Latin1', 'Dutch_Nederlands-Latin1', 'English-Latin1', 
             'French_Francais-Latin1', 'German_Deutsch-Latin1', 'Indonesian-Latin1', 'Italian-Latin1', 
             'Spanish_Espanol-Latin1','Swedish_Svenska-Latin1']
    for word in text.split():
        for lang in languages.keys():
            if word in udhr.words(nltklangs[list(languages).index(lang)]):
                languages[lang] += 1

    return languages

def determine_language(languages):
    max_value = max(languages.values())
    most_likely_language = random.choice([k for k, v in languages.items() if v == max_value])
    return most_likely_language

if __name__ == '__main__':
    text = read_file(sys.argv[1])
    text = preprocess(text)
    languages = calculate_frequency(text)
    language = determine_language(languages)
    print("The text is most likely in: ", language)
    
