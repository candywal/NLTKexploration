import re
import os
import sys
import math
import random
import nltk
import syllables
from syllables import estimate
from nltk.corpus import cmudict


cmu = cmudict.dict()

def count_syllables(word):
    word = word.lower()
    if word in cmu:
        if cmu.get(word):
            phones = cmu.get(word)
            phones = phones[0]       
            return len([p for p in phones if p[-1].isdigit()]) 
        else:
            return estimate(word)
    else:
       return estimate(word)

def new_flesch_reading_ease(text):
    words = re.findall(r'\b\w+\b', text)
    sentences = len(re.split(r'[.!?]+', text))
    syllables = 0
    for word in words:
        syllables += count_syllables(word)
    one_syllable_words = [word for word in words if count_syllables(word) == 1]
    nosw = (len(one_syllable_words) / len(words) )* 100
    score = 1.599 * nosw - 1.015*(len(words)/sentences) - 31.517
    return score

def flesch_kincaid_grade_level(text):
    words = re.findall(r'\b\w+\b', text)
    sentences = re.split(r'[.!?]+', text)
    sentence_count = len(sentences)
    word_count = len(words)
    syllable_count = 0
    for word in words:
        syllable_count += count_syllables(word)
    kincaid = (0.39 * (word_count / sentence_count)) + (11.8 * (syllable_count / word_count)) - 15.59
    return kincaid

def dale_chall_readability_score(text):
    dale_chall_words = []
    f = open("dcwords.txt", "r")
    for i in f.read().split('\n'):
        dale_chall_words.append(i.strip())
    f.close()

    words = re.findall(r'\b\w+\b', text)
    sentences = len(re.split(r'[.!?]+', text))
    difficulty = 0
    for word in words:
        if not word in dale_chall_words:
            difficulty += 1
    difficulty = difficulty / len(words) * 100
    score = 0.1579 * difficulty + 0.0496 * (len(words) / sentences) + 3.6365
    return score


def gunning_fog_index(text):
    words = re.findall(r'\b\w+\b', text)
    sentences = re.split(r'[.!?]+', text)
    sentence_count = len(sentences)
    word_count = len(words)
    complex_words = 0
    for word in words:
        syllables = count_syllables(word)
        if syllables >= 3:
            complex_words += 1
    fog = 0.4 * ((word_count / sentence_count) + 100 * (complex_words /word_count))
    return fog

def smog_index(text):
    words = re.findall(r'\b\w+\b', text)
    sentence_count = len(re.split(r'[.!?]+', text))
    polysyllable_count = 0
    for word in words:
        syllables = count_syllables(word)
        if syllables >= 3:
            polysyllable_count += 1
    wrongsmog = 1.0430 * math.sqrt(polysyllable_count * (30 / sentence_count)) + 3.1291
    smog = 3 + math.sqrt(polysyllable_count * (30 / sentence_count))
    return smog

def main():
    with open(sys.argv[1], 'r') as file:
        text = file.read()

    print("New Flesch Reading Ease: {:.2f}".format(new_flesch_reading_ease(text)))
    print("Flesch-Kincade Grade Level: {:.2f}".format(flesch_kincaid_grade_level(text)))
    print("Dale-Chall Readability Score: {:.2f}".format(dale_chall_readability_score(text)))
    if dale_chall_readability_score(text) <= 4.9:
        print("Dale-Chall Readability Grade: Grade 4 and below")
    if dale_chall_readability_score(text) >= 5.0 and dale_chall_readability_score(text) <= 5.9:
        print("Dale-Chall Readability Grade: Grade 5-6")
    if dale_chall_readability_score(text) >= 6.0 and dale_chall_readability_score(text) <= 6.9:
        print("Dale-Chall Readability Grade: Grade 7-8")
    if dale_chall_readability_score(text) >= 7.0 and dale_chall_readability_score(text) <= 7.9:
        print("Dale-Chall Readability Grade: Grade 9-10")
    if dale_chall_readability_score(text) >= 8.0 and dale_chall_readability_score(text) <= 8.9:
        print("Dale-Chall Readability Grade: Grade 11-12")
    if dale_chall_readability_score(text) >= 9.0 and dale_chall_readability_score(text) <= 9.9:
        print("Dale-Chall Readability Grade: College(13-15)")
    if dale_chall_readability_score(text) >= 10.0:
        print("Dale-Chall Readability Grade: College Graduate(16+)")

    
    print("Gunning-Fog Index: {:.2f}".format(gunning_fog_index(text)))
    print("SMOG Grade: {:.2f}".format(smog_index(text)))

if __name__ == '__main__':
    main()
