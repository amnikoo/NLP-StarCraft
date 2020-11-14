from wordcloud import WordCloud
from nltk.corpus import stopwords
import copy
import math
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


HumanSents = open("../../ProcessedData/Human/HumanSentsNorms.txt", 'r')
NotHumanSents = open("../../ProcessedData/NotHuman/NotHumanSentsNorms.txt", 'r')

HumanPhrases = list(set(HumanSents.read().split("\n")))
NotHumanPhrases = list(set(NotHumanSents.read().split("\n")))

for i in range(len(HumanPhrases)):
    HumanPhrases[i] = "Human " + HumanPhrases[i]
for i in range(len(NotHumanPhrases)):
    NotHumanPhrases[i] = "NotHuman " + NotHumanPhrases[i]

Phrases = []
Phrases = HumanPhrases + NotHumanPhrases

# These below lines are for split data to test and train
'''
PhrasesTrain, PhrasesTest = train_test_split(Phrases, test_size=0.2)

Train = open("../train.txt", 'w')
Test = open("../test.txt", 'w')

Train.write("\n".join(PhrasesTrain))
Test.write("\n".join(PhrasesTest))

Train.close()
Test.close()
'''

HumanSents.close()
NotHumanSents.close()
