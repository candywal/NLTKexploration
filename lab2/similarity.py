import nltk
from nltk.corpus import wordnet as wn
from collections import defaultdict, deque
import re
import os
import sys
import math
import random

# total_lemma_count = 0
# for synset in list((wn.all_synsets('n'))):
#     for lemma in synset.lemmas():
#         total_lemma_count += lemma.count() + 1 = 
# form slack
total_lemma_count = 94949 + 130727 

def hypernym_paths(synset): 
    if synset.hypernyms() == []:
        return {synset: 0}
    path = {}
    q = deque([(synset, 0)])
    while q:
        s, d = q.popleft()
        if s not in path:
            path[s] = d
            d += 1
            q.extend([(h, d) for h in s.hypernyms()])
            q.extend([(h, d) for h in s.instance_hypernyms()])
    return path

def pathlen(synset1, synset2):
    path1 = hypernym_paths(synset1)
    path2 = hypernym_paths(synset2)
    minlen = float('inf')
    for s1, d1 in path1.items():
        for s2, d2 in path2.items():
            if s1 == s2:
                minlen = min(minlen, d1 + d2)
    return minlen + 1
def p(c):
    return count(c) / total_lemma_count

def count(syn):
    c = 0
    a = get_hyponyms((syn))
    a.add(syn)
    for i in a:
        for j in i.lemmas():
            c += j.count() + 1
    return c
            
def get_hyponyms(synset):
    hyponyms = set()
    for hyponym in synset.hyponyms():
        hyponyms |= set(get_hyponyms(hyponym))
    return hyponyms | set(synset.hyponyms())

def simresnik(synset1, synset2):
    return -math.log(p(lcs(synset1, synset2)))

def simpath(synset1, synset2):
    return 1 / pathlen(synset1, synset2)

def lcs(a, b): 
    if a == b:
        return a
    a_paths = hypernym_paths(a)
    b_paths = hypernym_paths(b)
    lcs = None
    for s1, d1 in a_paths.items():
        for s2, d2 in b_paths.items():
            if s1 == s2:
                if lcs is None or d1 + d2 < a_paths[lcs] + b_paths[lcs]:
                    lcs = s1
    return lcs

def IC(synset):
    return -math.log(p(synset))

def simlin(synset1, synset2):
    return (2*math.log(p(lcs(synset1, synset2)))) / (math.log(p(synset1)) + math.log(p(synset2)))

def simjc(synset1, synset2):
    return 1/((2*math.log(p(lcs(synset1, synset2)))) - (math.log(p(synset1)) + math.log(p(synset2))))

def lms(arr1, arr2):
    len1 = len(arr1)
    len2 = len(arr2)
    max_len = 0
    end = -1
    for i in range(len1):
        for j in range(len2):
            k = 0
            while (i + k < len1) and (j + k < len2) and (arr1[i + k] == arr2[j + k]):
                k += 1
            if k > max_len:
                max_len = k
                end = i + k - 1
    return arr1[end - max_len + 1 : end + 1]

def overlap(s1, s2):
    a1 = [word.lower().strip(".,;:!?") for word in s1.split()]
    a2 = [word.lower().strip(".,;:!?") for word in s2.split()]
    k = []
    while lms(a1, a2):
        k.append(len(lms(a1, a2)))
        for i in lms(a1, a2):
            a1.remove(i)
            a2.remove(i)
    overlap = 0
    for i in k:
        overlap += i**2
    return overlap

def get_hyponym_definitions(synset):
    definitions = []
    for hyponym in synset.hyponyms():
        definitions.append(hyponym.definition())
    return " ".join(definitions)


def simelesk(synset1, synset2):
    hypodef1 = get_hyponym_definitions(synset1)
    hypodef2 = get_hyponym_definitions(synset2)
    def1 = synset1.definition()
    def2 = synset2.definition()
    return overlap(hypodef1, hypodef2) + overlap(def1, def2) + overlap(def1, hypodef2) + overlap(hypodef1, def2)
    

def main():
    arg1 = wn.synset(sys.argv[1]) if '.' in sys.argv[1] else wn.synsets(sys.argv[1])[0]
    arg2 = wn.synset(sys.argv[2]) if '.' in sys.argv[2] else wn.synsets(sys.argv[2])[0]
    print("path length based similarity: \t{:.3f}".format(simpath(arg1, arg2)))
    print("resnik similarity:            \t{:.3f}".format(simresnik(arg1, arg2)))
    print("lin similarity:               \t{:.3f}".format(simlin(arg1, arg2)))
    print("jc similarity:                \t{:.3f}".format(simjc(arg1, arg2)))
    print("elesk similarity:             \t{:.3f}".format(simelesk(arg1, arg2)))
if __name__ == "__main__":
    main()
