from wordcloud import WordCloud
from nltk.corpus import stopwords
import copy
import math
import matplotlib.pyplot as plt


Train = open("../../train.txt", 'r')
Test = open("../../test.txt", 'r')

TrainWords = Train.read()
TestWords = Test.read()

TrainPhrases = TrainWords.split("\n")
TestPhrases = TestWords.split("\n")

for i in range(len(TrainPhrases)):
    Sent = TrainPhrases[i].split()
    Seen = set()
    UniqueSent = [x for x in Sent if not (x in Seen or Seen.add(x))]
    for j in range(1,len(UniqueSent)):
        UniqueSent[j] = "f_" + UniqueSent[j] + ":" + str(Sent.count(UniqueSent[j]))
    TrainPhrases[i] = " ".join(UniqueSent)
for i in range(len(TestPhrases)):
    Sent = TestPhrases[i].split()
    Seen = set()
    UniqueSent = [x for x in Sent if not (x in Seen or Seen.add(x))]
    for j in range(1,len(UniqueSent)):
        UniqueSent[j] = "f_" + UniqueSent[j] + ":" + str(Sent.count(UniqueSent[j]))
    TestPhrases[i] = " ".join(UniqueSent)

Train.close()
Test.close()

TrainWords = "\n".join(TrainPhrases)
TestWords = "\n".join(TestPhrases)

Train = open("../input.train.txt", 'w')
Test = open("../input.test.txt", 'w')

Train.write(TrainWords)
Test.write(TestWords)

Train.close()
Test.close()

