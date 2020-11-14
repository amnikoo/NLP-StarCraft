import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
import re
import os
import string

#tokenization
Human = open("../../Data/Human.txt", 'r')
NotHuman = open("../../Data/NotHuman.txt", 'r')

HumanPhrases = sent_tokenize(Human.read())
NotHumanPhrases = sent_tokenize(NotHuman.read())
HumanExprs = word_tokenize(" ".join(HumanPhrases))
NotHumanExprs = word_tokenize(" ".join(NotHumanPhrases))

Human.close()
NotHuman.close()

HumanSents = open("../Human/HumanSents.txt", 'w')
NotHumanSents = open("../NotHuman/NotHumanSents.txt", 'w')
HumanWords = open("../Human/HumanWords.txt", 'w')
NotHumanWords = open("../NotHuman/NotHumanWords.txt", 'w')

for HumanPhrase in HumanPhrases:
    HumanSents.write(HumanPhrase+"\n")
for HumanExpr in HumanExprs:
    HumanWords.write(HumanExpr+"\n")
for NotHumanPhrase in NotHumanPhrases:
    NotHumanSents.write(NotHumanPhrase+"\n")
for NotHumanExpr in NotHumanExprs:
    NotHumanWords.write(NotHumanExpr+"\n")

HumanSents.close()
NotHumanSents.close()
HumanWords.close()
NotHumanWords.close()

HumanSents = open("../Human/HumanSents.txt", 'r')
NotHumanSents = open("../NotHuman/NotHumanSents.txt", 'r')

#normalization sentences
HumanNorms = HumanSents.read()
NotHumanNorms = NotHumanSents.read()

HumanSents.close()
NotHumanSents.close()

HumanNorms = HumanNorms.lower()
NotHumanNorms = NotHumanNorms.lower()

HumanNorms = re.sub(r'\d+', '', HumanNorms)
NotHumanNorms = re.sub(r'\d+', '', NotHumanNorms)

HumanNorms = HumanNorms.translate(str.maketrans("","", string.punctuation))
NotHumanNorms = NotHumanNorms.translate(str.maketrans("","", string.punctuation))

HumanNorms = HumanNorms.strip()
NotHumanNorms = NotHumanNorms.strip()

HumanNs = open("../Human/HumanSentsNorms.txt", 'w')
NotHumanNs = open("../NotHuman/NotHumanSentsNorms.txt", 'w')

HumanNs.write(HumanNorms)
NotHumanNs.write(NotHumanNorms)

HumanNs.close()
NotHumanNs.close()

HumanWords = open("../Human/HumanWords.txt", 'r')
NotHumanWords = open("../NotHuman/NotHumanWords.txt", 'r')

#normalization words

HumanNorms = HumanWords.read()
NotHumanNorms = NotHumanWords.read()

HumanWords.close()
NotHumanWords.close()

HumanNorms = HumanNorms.lower()
NotHumanNorms = NotHumanNorms.lower()

HumanNorms = re.sub(r'\d+', '', HumanNorms)
NotHumanNorms = re.sub(r'\d+', '', NotHumanNorms)

HumanNorms = HumanNorms.translate(str.maketrans("","", string.punctuation))
NotHumanNorms = NotHumanNorms.translate(str.maketrans("","", string.punctuation))

HumanNorms = re.sub(" ", "",HumanNorms)
HumanNormsList = HumanNorms.split("\n")
for word in HumanNormsList:
    if(word == r'\W' or word == ''):
        HumanNormsList.remove(word)
        continue
    word = PorterStemmer().stem(word)
    word = WordNetLemmatizer().lemmatize(word)
HumanNorms = "\n".join(HumanNormsList)

NotHumanNorms = re.sub(" ", "",NotHumanNorms)
NotHumanNormsList = NotHumanNorms.split("\n")
for word in NotHumanNormsList:
    if(word == r'\W' or word == ''):
        NotHumanNormsList.remove(word)
        continue
    word = PorterStemmer().stem(word)
    word = WordNetLemmatizer().lemmatize(word)
NotHumanNorms = "\n".join(NotHumanNormsList)

HumanNorms = HumanNorms.strip()
NotHumanNorms = NotHumanNorms.strip()

HumanNorms = re.sub("\n\n", "\n",HumanNorms)
NotHumanNorms = re.sub("\n\n", "\n",NotHumanNorms)

HumanNs = open("../Human/HumanWordsNorms.txt", 'w')
NotHumanNs = open("../NotHuman/NotHumanWordsNorms.txt", 'w')

HumanNs.write(HumanNorms)
NotHumanNs.write(NotHumanNorms)

HumanNs.close()
NotHumanNs.close()
