import nltk
import re
import sys
import random
from nltk.corpus import gutenberg

text = gutenberg.raw('bible-kjv.txt')
#remove ' " (){}[] pairs  
text = re.sub(r'(?<!\w)[\(\)\{\}\[\]\"\']|[\(\)\{\}\[\]\"\'](?!\w)', '', text)
text = re.sub(r'\d:\d', '', text)
text = re.sub(r'[0-9]+', '', text)
tokens = nltk.word_tokenize(text)

trigram_model = {}

for i in range(len(tokens)-2):
    if tokens[i] + ' ' + tokens[i+1] in trigram_model:
        trigram_model[tokens[i] + ' ' + tokens[i+1]].append(tokens[i+2])
    else:
        trigram_model[tokens[i] + ' ' + tokens[i+1]] = [tokens[i+2]]

def generate_para():
    num1 = random.randint(1, 90); num2 = random.randint(1, 40)
    tsentences = []
    for i in range(random.randint(3, 6)):
        current_words = random.choice(list(trigram_model.keys())).split()
        sentence = current_words[0] + ' ' + current_words[1]
        for j in range(random.randint(15,20)):
            next_word = random.choice(trigram_model[current_words[0] + ' ' + current_words[1]])
            sentence += ' ' + next_word
            current_words[0] = current_words[1]
            current_words[1] = next_word
        tsentences.append(sentence)
        
        
    
    tsentences[0] = tsentences[0].capitalize()
    for i in tsentences: 
        i.capitalize()
        
        if ' , ' in i:
            i = i.replace(' , ', ', ')
        if ' . ' in i:
            rep = '. \n\t' + str(num1) + ':' + str(num2) + ' '  
            i = i.replace(' . ', rep)
            num2+=1
        if ' ! ' in i:
            rep = '. ' + str(num1) + ':' + str(num2) + ' '  
            i = i.replace(' ! ', rep)
            num2+=1
        if ' ? ' in i:
            rep = '. ' + str(num1) + ':' + str(num2) + ' '  
            i = i.replace(' ? ', rep)
            num2+=1
        if ' ;' in i:
            i = i.replace(' ;', ';')
        if ' - ' in i:
            i = i.replace(' - ', '-')
        if ' : ' in i:
            i = i.replace(' : ', ': ')
        
        print(i, end = ' ')
  
    num1+=1
    num2 = 0
    tsentences = []
    for i in range(random.randint(8, 10)):
        current_words = random.choice(list(trigram_model.keys())).split()
        sentence = current_words[0] + ' ' + current_words[1]
        for j in range(random.randint(15,20)):
            next_word = random.choice(trigram_model[current_words[0] + ' ' + current_words[1]])
            sentence += ' ' + next_word
            current_words[0] = current_words[1]
            current_words[1] = next_word
        tsentences.append(sentence)
        
        
    
    tsentences[0] = tsentences[0].capitalize()
    
    for i in tsentences: 
        i.capitalize()
        
        if ' , ' in i:
            i = i.replace(' , ', ', ')
        if ' . ' in i:
            rep = '. \n\t' + str(num1) + ':' + str(num2) + ' '  
            i = i.replace(' . ', rep)
            num2+=1
        if ' ! ' in i:
            rep = '. ' + str(num1) + ':' + str(num2) + ' '  
            i = i.replace(' ! ', rep)
            num2+=1
        if ' ? ' in i:
            rep = '. ' + str(num1) + ':' + str(num2) + ' '  
            i = i.replace(' ? ', rep)
            num2+=1
        if ' ;' in i:
            i = i.replace(' ;', ';')
        if ' - ' in i:
            i = i.replace(' - ', '-')
        if ' : ' in i:
            i = i.replace(' : ', ': ')
        
        print(i, end = ' ')
  
    num1+=1
    num2 = 1
    tsentences = []
    for i in range(random.randint(3, 6)):
        current_words = random.choice(list(trigram_model.keys())).split()
        sentence = current_words[0] + ' ' + current_words[1]
        for j in range(random.randint(15,20)):
            next_word = random.choice(trigram_model[current_words[0] + ' ' + current_words[1]])
            sentence += ' ' + next_word
            current_words[0] = current_words[1]
            current_words[1] = next_word
        tsentences.append(sentence)
        
        
    
    tsentences[0] = tsentences[0].capitalize()
    for i in tsentences: 
        i.capitalize()
        
        if ' , ' in i:
            i = i.replace(' , ', ', ')
        if ' . ' in i:
            rep = '. \n\t' + str(num1) + ':' + str(num2) + ' '  
            i = i.replace(' . ', rep)
            num2+=1
        if ' ! ' in i:
            rep = '. ' + str(num1) + ':' + str(num2) + ' '  
            i = i.replace(' ! ', rep)
            num2+=1
        if ' ? ' in i:
            rep = '. ' + str(num1) + ':' + str(num2) + ' '  
            i = i.replace(' ? ', rep)
            num2+=1
        if ' ;' in i:
            i = i.replace(' ;', ';')
        if ' - ' in i:
            i = i.replace(' - ', '-')
        if ' : ' in i:
            i = i.replace(' : ', ': ')
        
        print(i, end = ' ')
  
    num1+=1
    num2 = 1
    
def main():
    generate_para()
        

if __name__ == '__main__':
    main()