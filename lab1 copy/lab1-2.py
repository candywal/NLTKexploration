"""Using the Gutenberg corpus (available from nltk.gutenberg), 
create two models, a word bigram and a word trigram model using the three works of Jane Austen (Persuasion, Emma,
Sense and Sensibility). Write a program (lab1-2.py) to generate 5 random sentences per model """
import nltk
import re
import sys
import random
from nltk.corpus import gutenberg

text = gutenberg.raw('austen-persuasion.txt') + gutenberg.raw('austen-emma.txt') + gutenberg.raw('austen-sense.txt')
#remove ' " (){}[] pairs  
text = re.sub(r'(?<!\w)[\(\)\{\}\[\]\"\']|[\(\)\{\}\[\]\"\'](?!\w)', '', text)
tokens = nltk.word_tokenize(text)

bigram_model = {}

for i in range(len(tokens)-1):
    if tokens[i] in bigram_model:
        bigram_model[tokens[i]].append(tokens[i+1])
    else:
        bigram_model[tokens[i]] = [tokens[i+1]]

trigram_model = {}

for i in range(len(tokens)-2):
    if tokens[i] + ' ' + tokens[i+1] in trigram_model:
        trigram_model[tokens[i] + ' ' + tokens[i+1]].append(tokens[i+2])
    else:
        trigram_model[tokens[i] + ' ' + tokens[i+1]] = [tokens[i+2]]
        
bsentences = []
for i in range(5):
    current_word = random.choice(list(bigram_model.keys()))
    sentence = current_word
    for j in range(10):
        next_word = random.choice(bigram_model[current_word])
        sentence += ' ' + next_word
        current_word = next_word
    bsentences.append(sentence)

tsentences = []
for i in range(5):
    current_words = random.choice(list(trigram_model.keys())).split()
    sentence = current_words[0] + ' ' + current_words[1]
    for j in range(8):
        next_word = random.choice(trigram_model[current_words[0] + ' ' + current_words[1]])
        sentence += ' ' + next_word
        current_words[0] = current_words[1]
        current_words[1] = next_word
    tsentences.append(sentence)
    
    
print("\n\n Bigram Model: \n")
bsentences[0] = bsentences[0].capitalize()
for i in bsentences: 
    if ' , ' in i:
        i = i.replace(' , ', ', ')
    if ' . ' in i:
        i = i.replace(' . ', '. ')
        
    if ' ! ' in i:
        i = i.replace(' ! ', '! ')
    if ' ? ' in i:
        i = i.replace(' ? ', '? ')
    if ' ; ' in i:
        i = i.replace(' ; ', '; ')
    if ' : ' in i:
        i = i.replace(' : ', ': ')
    if ' -- ' in i:
        i = i.replace(' -- ', '-- ')
    
        
    print(i)
    
print("\n\n Trigram Model: \n")
tsentences[0] = tsentences[0].capitalize()
for i in tsentences: 
    if ' , ' in i:
        i = i.replace(' , ', ', ')
    if ' . ' in i:
        i = i.replace(' . ', '. ')
        
    if ' ! ' in i:
        i = i.replace(' ! ', '! ')
    if ' ? ' in i:
        i = i.replace(' ? ', '? ')
    if ' ; ' in i:
        i = i.replace(' ; ', '; ')
    print(i)
