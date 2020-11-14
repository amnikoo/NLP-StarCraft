import re
import math

def ComputePerplexity(LM1Path, LM2Path, LM3Path, TestFilePath):
    LMPath = LM1Path
    LMFile = open(LMPath, "r")
    LMList = LMFile.read().split("\n")
    LMList = LMList[:-1]
    LMDict = {}
    LMFile.close()
    Perplexity1 = 0
    Perplexity2 = 0
    Perplexity3 = 0
    TestFile = open(TestFilePath, "r")
    TestFileList = TestFile.read().split("\n")
    if "1" in LMPath:
        for Word in LMList:
            WordList = Word.split("|")
            LMDict[WordList[0]] = float(WordList[1])
        for i in range(len(TestFileList)):
            TestFileList[i] = "<s> " + TestFileList[i] + " </s>"
            SentWords = TestFileList[i].split()
            for j in range(1, len(SentWords)-1):
                if(SentWords[j] not in LMDict):
                    SentWords[j] = "UNK"
                Perplexity1 += math.log(LMDict[SentWords[j]])
            TestFileList[i] = " ".join(SentWords)
        Perplexity1 *= -(1 / len(LMDict))
        Perplexity1 = math.exp(Perplexity1)
        Perplexity1 = int(Perplexity1)
    
    LMPath = LM2Path
    LMFile = open(LMPath, "r")
    LMList = LMFile.read().split("\n")
    LMList = LMList[:-1]
    LMDict = {}
    LMFile.close()
    if "2" in LMPath:
        for Word in LMList:
            WordList = Word.split("|")
            LMDict[(WordList[0], WordList[1])] = float(WordList[2])
        for i in range(len(TestFileList)):
            SentWords = TestFileList[i].split()
            for j in range(len(SentWords)-1):
                if((SentWords[j], SentWords[j+1]) not in LMDict):
                    (SentWords[j], SentWords[j+1]) = ("UNK", "UNK")
                Perplexity2 += math.log(LMDict[(SentWords[j], SentWords[j+1])])
            TestFileList[i] = " ".join(SentWords)
        Perplexity2 *= -(1 / len(LMDict))
        Perplexity2 = math.exp(Perplexity2)
        Perplexity2 = int(Perplexity2)

    LMPath = LM3Path
    LMFile = open(LMPath, "r")
    LMList = LMFile.read().split("\n")
    LMList = LMList[:-1]
    LMDict = {}
    LMFile.close()
    if "3" in LMPath:
        for Word in LMList:
            WordList = Word.split("|")
            LMDict[(WordList[0], WordList[1], WordList[2])] = float(WordList[3])
        for i in range(len(TestFileList)):
            SentWords = TestFileList[i].split()
            for j in range(len(SentWords)-2):
                if((SentWords[j], SentWords[j+1], SentWords[j+2]) not in LMDict):
                    (SentWords[j], SentWords[j+1], SentWords[j+2]) = ("UNK", "UNK", "UNK")
                Perplexity3 += math.log(LMDict[(SentWords[j], SentWords[j+1], SentWords[j+2])])
            TestFileList[i] = " ".join(SentWords)
        Perplexity3 *= -(1 / len(LMDict))
        Perplexity3 = math.exp(Perplexity3)
        Perplexity3 = int(Perplexity3)
    TestFile.close()
    return(Perplexity1, Perplexity2, Perplexity3)
    
out1Path = "../../Model/test/out.1gram.lm"
out2Path = "../../Model/test/out.2gram.lm"
out3Path = "../../Model/test/out.3gram.lm"

Human1GramPath = "../../Model/Human.1gram.lm"
Human2GramPath = "../../Model/Human.2gram.lm"
Human3GramPath = "../../Model/Human.3gram.lm"

NotHuman1GramPath = "../../Model/NotHuman.1gram.lm"
NotHuman2GramPath = "../../Model/NotHuman.2gram.lm"
NotHuman3GramPath = "../../Model/NotHuman.3gram.lm"

HumanSentsTrainPath = "../../SplitData/Human/HumanSentsTrain.txt"
NotHumanSentsTrainPath = "../../SplitData/NotHuman/NotHumanSentsTrain.txt"
HumanSentsTestPath = "../../SplitData/Human/HumanSentsTest.txt"
NotHumanSentsTestPath = "../../SplitData/NotHuman/NotHumanSentsTest.txt"

Perplexities = ComputePerplexity(Human1GramPath, Human2GramPath, Human3GramPath, HumanSentsTrainPath)
print("Human1GramTrainPerplexity = " + str(Perplexities[0]))
print("Human2GramTrainPerplexity = " + str(Perplexities[1]))
print("Human3GramTrainPerplexity = " + str(Perplexities[2]))

Perplexities = ComputePerplexity(NotHuman1GramPath, NotHuman2GramPath, NotHuman3GramPath, NotHumanSentsTrainPath)
print("NotHuman1GramTrainPerplexity = " + str(Perplexities[0]))
print("NotHuman2GramTrainPerplexity = " + str(Perplexities[1]))
print("NotHuman3GramTrainPerplexity = " + str(Perplexities[2]))

Perplexities = ComputePerplexity(Human1GramPath, Human2GramPath, Human3GramPath, HumanSentsTestPath)
print("Human1GramTestPerplexity = " + str(Perplexities[0]))
print("Human2GramTestPerplexity = " + str(Perplexities[1]))
print("Human3GramTestPerplexity = " + str(Perplexities[2]))

Perplexities = ComputePerplexity(NotHuman1GramPath, NotHuman2GramPath, NotHuman3GramPath, NotHumanSentsTestPath)
print("NotHuman1GramTestPerplexity = " + str(Perplexities[0]))
print("NotHuman2GramTestPerplexity = " + str(Perplexities[1]))
print("NotHuman3GramTestPerplexity = " + str(Perplexities[2]))
