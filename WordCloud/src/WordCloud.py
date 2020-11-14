from wordcloud import WordCloud
from nltk.corpus import stopwords
import copy
import matplotlib.pyplot as plt

HumanWords = open("../../ProcessedData/Human/HumanWordsNorms.txt", 'r')
NotHumanWords = open("../../ProcessedData/NotHuman/NotHumanWordsNorms.txt", 'r')

HumanExprs = HumanWords.read()
NotHumanExprs = NotHumanWords.read()
HumanWordsList = HumanExprs.split("\n")
NotHumanWordsList = NotHumanExprs.split("\n")
Dict1 = {}
Dict2 = {}
Dict3 = {}
Dict4 = {}
Dict5 = {}
Dict6 = {}
Dict7 = {}
Dict8 = {}

for word in HumanWordsList:
    Dict1[word] = HumanExprs.count(word) / len(HumanExprs)
for word in NotHumanWordsList:
    Dict2[word] = NotHumanExprs.count(word) / len(NotHumanExprs)
Dict3 = copy.deepcopy(Dict1)
for word in Dict3:
    if(word in Dict2):
        Dict3[word] = Dict3[word] - Dict2[word]
Dict4 = copy.deepcopy(Dict2)
for word in Dict4:
    if(word in Dict1):
        Dict4[word] = Dict4[word] - Dict1[word]

HumanStopWords = set(stopwords.words("english"))
HumanStopWords = HumanStopWords | {"nt", "er", "ta", "ca", "na", "em", "wo", "era", "ai", "us"}
Dict5 = copy.deepcopy(Dict1)
for word in HumanStopWords:
    if word in Dict5:
        del(Dict5[word])
NotHumanStopWords = set(stopwords.words("english"))
NotHumanStopWords = NotHumanStopWords | {"nt", "en", "us"}
Dict6 = copy.deepcopy(Dict2)
for word in NotHumanStopWords:
    if word in Dict6:
        del(Dict6[word])
HumanStopWords = set(stopwords.words("english"))
HumanStopWords = HumanStopWords | {"nt", "er", "ta", "ca", "na", "em", "wo", "era", "ai", "us"}
Dict7 = copy.deepcopy(Dict3)
for word in HumanStopWords:
    if word in Dict7:
        del(Dict7[word])
NotHumanStopWords = set(stopwords.words("english"))
NotHumanStopWords = NotHumanStopWords | {"nt", "en", "us"}
Dict8 = copy.deepcopy(Dict4)
for word in NotHumanStopWords:
    if word in Dict8:
        del(Dict8[word])

#1
WordCloud1 = WordCloud().generate_from_frequencies(Dict1)
WordCloud1.to_file("../out/1.jpg")
plt.imshow(WordCloud1, interpolation='bilinear')
plt.axis("off")
plt.show()

#2
WordCloud2 = WordCloud().generate_from_frequencies(Dict2)
WordCloud2.to_file("../out/2.jpg")
plt.figure()
plt.imshow(WordCloud2, interpolation='bilinear')
plt.axis("off")
plt.show()

#3
WordCloud3 = WordCloud().generate_from_frequencies(Dict3)
WordCloud3.to_file("../out/3.jpg")
plt.figure()
plt.imshow(WordCloud3, interpolation='bilinear')
plt.axis("off")
plt.show()

#4
WordCloud4 = WordCloud().generate_from_frequencies(Dict4)
WordCloud4.to_file("../out/4.jpg")
plt.figure()
plt.imshow(WordCloud4, interpolation='bilinear')
plt.axis("off")
plt.show()

#5
WordCloud5 = WordCloud().generate_from_frequencies(Dict5)
WordCloud5.to_file("../out/5.jpg")
plt.figure()
plt.imshow(WordCloud5, interpolation='bilinear')
plt.axis("off")
plt.show()

#6
WordCloud6 = WordCloud().generate_from_frequencies(Dict6)
WordCloud6.to_file("../out/6.jpg")
plt.figure()
plt.imshow(WordCloud6, interpolation='bilinear')
plt.axis("off")
plt.show()

#7
WordCloud7 = WordCloud().generate_from_frequencies(Dict7)
WordCloud7.to_file("../out/7.jpg")
plt.figure()
plt.imshow(WordCloud7, interpolation='bilinear')
plt.axis("off")
plt.show()

#8
WordCloud8 = WordCloud().generate_from_frequencies(Dict8)
WordCloud8.to_file("../out/8.jpg")
plt.figure()
plt.imshow(WordCloud8, interpolation='bilinear')
plt.axis("off")
plt.show()

