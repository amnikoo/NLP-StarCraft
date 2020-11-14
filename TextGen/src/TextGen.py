import re
import math
import random

def TextGenerator(LMPath, n, Seed):
    LMFile = open(LMPath, "r")
    LMList = LMFile.read().split("\n")
    LMFile.close()
    LMList = LMList[:-1]
    LMListCopy = []
    RandomText = []
    OutText = []
    LMDict = dict()
    random.seed(Seed)
    for i in range(len(LMList)):
        if "UNK" not in LMList[i]:
            LMListCopy.append(LMList[i])
    LMList = LMListCopy.copy()
    for i in range(n):
        RandomText = []
        if "1" in LMPath:
            for i in range(n):
                Choice = random.randint(0, len(LMList)-1)
                ChoiceWord = LMList[Choice].split("|")
                RandomText.append(ChoiceWord[0])
    
        elif "2" in LMPath:
            for Word in LMList:
                WordList = Word.split("|")
                LMDict.setdefault(WordList[0], []).append(WordList[1])
            Choice = random.randint(0, len(LMList)-1)
            ChoiceWord = LMList[Choice].split("|")
            RandomText.append(ChoiceWord[0])
            RandomText.append(ChoiceWord[1])
            for i in range(1, n-1):
                if WordList[i] in LMDict:
                    RandomText.append(random.choice(LMDict[WordList[i]]))
                else:
                    break
    
        elif "3" in LMPath:
            for Word in LMList:
                WordList = Word.split("|")
                LMDict.setdefault((WordList[0], WordList[1]), []).append(WordList[2])
            Choice = random.randint(0, len(LMList)-1)
            ChoiceWord = LMList[Choice].split("|")
            RandomText.append(ChoiceWord[0])
            RandomText.append(ChoiceWord[1])
            RandomText.append(ChoiceWord[2])
            for i in range(1, n-2):
                if (WordList[i], WordList[i+1]) in LMDict:
                    RandomText.append(random.choice(LMDict[(WordList[i], WordList[i+1])]))
                else:
                    break
        while "<s>" in RandomText:
            RandomText.remove("<s>")
        while "</s>" in RandomText:
            RandomText.remove("</s>")
        RandomText = " ".join(RandomText)
        print(RandomText)
        OutText.append(RandomText)
    return("\n".join(OutText))
    

    
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

print("1GramText : ")
TextGenerator(out1Path, 10, 60)
print("2GramText : ")
TextGenerator(out2Path, 10, 60)
print("3GramText : ")
TextGenerator(out3Path, 10, 60)

print("1GramText : ")
OutText = TextGenerator(Human1GramPath, 10, 60)
File = open("../Human.1gram.gen", "w")
File.write(OutText)
File.close()
print("2GramText : ")
OutText = TextGenerator(Human2GramPath, 10, 60)
File = open("../Human.2gram.gen", "w")
File.write(OutText)
File.close()
print("3GramText : ")
OutText = TextGenerator(Human3GramPath, 10, 60)
File = open("../Human.3gram.gen", "w")
File.write(OutText)
File.close()

print("1GramText : ")
OutText = TextGenerator(NotHuman1GramPath, 10, 60)
File = open("../NotHuman.1gram.gen", "w")
File.write(OutText)
File.close()
print("2GramText : ")
OutText = TextGenerator(NotHuman2GramPath, 10, 60)
File = open("../NotHuman.2gram.gen", "w")
File.write(OutText)
File.close()
print("3GramText : ")
OutText = TextGenerator(NotHuman3GramPath, 10, 60)
File = open("../NotHuman.3gram.gen", "w")
File.write(OutText)
File.close()
