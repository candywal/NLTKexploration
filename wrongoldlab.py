import nltk
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import udhr
import sys

language = ['Afrikaans', 'Danish', 'Dutch', 'English', 'French', 'German', 'Indonesian', 'Italian', 'Spanish', 'Swedish']
nltklangs = ['Afrikaans-Latin1', 'Danish_Dansk-Latin1', 'Dutch_Nederlands-Latin1', 'English-Latin1', 
             'French_Francais-Latin1', 'German_Deutsch-Latin1', 'Indonesian-Latin1', 'Italian-Latin1', 
             'Spanish_Espanol-Latin1','Swedish_Svenska-Latin1']
samples = {language: list(udhr.words(language)) for language in nltklangs}
training_set = []
for language, sample in samples.items():
    training_set.append((sample, language))

training_set = [({word: True for word in text}, language) for text, language in training_set]

classifier = NaiveBayesClassifier.train(training_set) #trains the classifier

if len(sys.argv)!=2:
    print("please just enter one file name expected use: python lab1-1.py <filename>")
    sys.exit()

file_name = sys.argv[1]
with open(file_name, 'r') as f:
    text = f.read()
    
text = text.split()
text_features = {word: True for word in text}
predicted_language = classifier.classify(text_features)
lang = predicted_language.split('-')[0]
lang = lang.split('_')[0]
print("Language of the inputted text: ", lang)
