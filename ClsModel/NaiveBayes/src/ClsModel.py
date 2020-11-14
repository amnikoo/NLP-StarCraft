from wordcloud import WordCloud
from nltk.corpus import stopwords
import copy
import math
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

def TrainData(Train):
    TrainWords = Train.read()
    TrainPhrasesList = TrainWords.split("\n")
    Class1TrainPhrasesList = []
    Class2TrainPhrasesList = []
    
    Class1 = TrainPhrasesList[0].split()[0]
    for Sent in TrainPhrasesList:
        SentWords = Sent.split()
        if Class1 in SentWords:
            Class1TrainPhrasesList.append(Sent)
        elif len(SentWords) != 0:
            Class2 = SentWords[0]
            Class2TrainPhrasesList.append(Sent)
        else:
            TrainPhrasesList.remove(Sent)
        
    Class1TrainWordsList = " ".join(Class1TrainPhrasesList).split(" ")
    Class2TrainWordsList = " ".join(Class2TrainPhrasesList).split(" ")
    Class1TrainWordsDict = {}
    Class2TrainWordsDict = {}
    TrainWordsV = len(set(" ".join(TrainPhrasesList).split(" ")))-2
    Class1TrainWordsV = len(set(Class1TrainWordsList))-1
    Class2TrainWordsV = len(set(Class2TrainWordsList))-1
    Class1TrainWordsCount = len(Class1TrainWordsList)-len(Class1TrainPhrasesList)
    Class2TrainWordsCount = len(Class2TrainWordsList)-len(Class2TrainPhrasesList)
    for word in Class1TrainWordsList:
        Class1TrainWordsDict[word] = (Class1TrainWordsList.count(word)+1) / (Class1TrainWordsCount+TrainWordsV)
    for word in Class2TrainWordsList:
        Class2TrainWordsDict[word] = (Class2TrainWordsList.count(word)+1) / (Class2TrainWordsCount+TrainWordsV)

    TrainStopWords = set(stopwords.words("english"))
    TrainStopWords = TrainStopWords | {"nt", "er", "ta", "ca", "na", "em", "wo", "era", "ai", "us"}
    for word in TrainStopWords:
        if word in Class1TrainWordsDict:
            del(Class1TrainWordsDict[word])
        if word in Class2TrainWordsDict:
            del(Class2TrainWordsDict[word])

    Class1Prob = len(Class1TrainPhrasesList) / (len(Class1TrainPhrasesList)+len(Class2TrainPhrasesList))
    Class2Prob = len(Class2TrainPhrasesList) / (len(Class1TrainPhrasesList)+len(Class2TrainPhrasesList))
    #Class Probabilities
    Class1TrainWordsDict[Class1] = Class1Prob
    Class2TrainWordsDict[Class2] = Class2Prob
    
    Class1TrainWordsDict["UNK"] = 1 / (Class1TrainWordsCount+TrainWordsV)
    Class2TrainWordsDict["UNK"] = 1 / (Class2TrainWordsCount+TrainWordsV)
    
    return((Class1TrainWordsDict, Class2TrainWordsDict, Class1, Class2))

def TestData(Test, TrainResult):
    Class1TrainWordsDict, Class2TrainWordsDict, Class1, Class2 = TrainResult
    ResultList = []
    TestWords = Test.read()
    TestPhrasesList = TestWords.split("\n")
    for i in range(len(TestPhrasesList)):
        Class1TestResult = Class1TrainWordsDict[Class1]
        Class2TestResult = Class2TrainWordsDict[Class2]
        SentWords = TestPhrasesList[i].split()
        for j in range(1, len(SentWords)):
            if SentWords[j] in Class1TrainWordsDict:
                Class1TestResult *= Class1TrainWordsDict[SentWords[j]]
            elif SentWords[j] not in Class1TrainWordsDict:
                Class1TestResult *= Class1TrainWordsDict["UNK"]
            if SentWords[j] in Class2TrainWordsDict:
                Class2TestResult *= Class2TrainWordsDict[SentWords[j]]
            elif SentWords[j] not in Class2TrainWordsDict:
                Class2TestResult *= Class2TrainWordsDict["UNK"]
        ResultList.append(Class1 + " " + "{0:.7f}".format(math.log(Class1TestResult, 10))[:-4] + " " + Class2 + " " + "{0:.7f}".format(math.log(Class2TestResult, 10))[:-4])
    return("\n".join(ResultList))

def ComputePerformance(TrueTest, AssignedTest, Class1, Class2):
    AssignedTestList = AssignedTest.split("\n")
    AssignedTestClassList = []
    for Expr in AssignedTestList:
        ExprList = Expr.split()
        if float(ExprList[1]) >= float(ExprList[3]):
            AssignedTestClassList.append(ExprList[0])
        else:
            AssignedTestClassList.append(ExprList[2])
    TrueTestWords = TrueTest.read()
    TrueTestPhrasesList = TrueTestWords.split("\n")
    Class1TrueAssigned = 0
    Class1TrueNotAssigned = 0
    Class1FalseAssigned = 0
    Class1FalseNotAssigned = 0
    for i in range(len(AssignedTestClassList)):
        if AssignedTestClassList[i] == Class1:
            if AssignedTestClassList[i] == TrueTestPhrasesList[i].split()[0]:
                Class1TrueAssigned += 1
            else:
                Class1FalseAssigned += 1
        else:
            if AssignedTestClassList[i] == TrueTestPhrasesList[i].split()[0]:
                Class1FalseNotAssigned += 1
            else:
                Class1TrueNotAssigned += 1
    Class2TrueAssigned = 0
    Class2TrueNotAssigned = 0
    Class2FalseAssigned = 0
    Class2FalseNotAssigned = 0
    for i in range(len(AssignedTestClassList)):
        if AssignedTestClassList[i] == Class2:
            if AssignedTestClassList[i] == TrueTestPhrasesList[i].split()[0]:
                Class2TrueAssigned += 1
            else:
                Class2FalseAssigned += 1
        else:
            if AssignedTestClassList[i] == TrueTestPhrasesList[i].split()[0]:
                Class2FalseNotAssigned += 1
            else:
                Class2TrueNotAssigned += 1
    
    Class1Recall = Class1TrueAssigned / (Class1TrueAssigned+Class1TrueNotAssigned)
    Class1Precision = Class1TrueAssigned / (Class1TrueAssigned+Class1FalseAssigned)
    Class1F1 = (2*Class1Precision*Class1Recall) / (Class1Precision+Class1Recall)
    Class1Accuracy = (Class1TrueAssigned+Class1FalseNotAssigned) / (Class1TrueAssigned+Class1TrueNotAssigned+Class1FalseAssigned+Class1FalseNotAssigned)
    
    Class2Recall = Class2TrueAssigned / (Class2TrueAssigned+Class2TrueNotAssigned)
    Class2Precision = Class2TrueAssigned / (Class2TrueAssigned+Class2FalseAssigned)
    Class2F1 = (2*Class2Precision*Class2Recall) / (Class2Precision+Class2Recall)
    Class2Accuracy = (Class2TrueAssigned+Class2FalseNotAssigned) / (Class2TrueAssigned+Class2TrueNotAssigned+Class2FalseAssigned+Class2FalseNotAssigned)

    ResultList = []
    ResultList.append(Class1 + " Recall:" + "{0:.3f}".format(Class1Recall) + " Precision:" + "{0:.3f}".format(Class1Precision) + " F1:" + "{0:.3f}".format(Class1F1) + " Accuracy:" + "{0:.3f}".format(Class1Accuracy))
    ResultList.append(Class2 + " Recall:" + "{0:.3f}".format(Class2Recall) + " Precision:" + "{0:.3f}".format(Class2Precision) + " F1:" + "{0:.3f}".format(Class2F1) + " Accuracy:" + "{0:.3f}".format(Class2Accuracy))
    return("\n".join(ResultList))

Train = open("../../../ClsData/TestCase/train.txt", 'r')

TrainResult = TrainData(Train)

Test = open("../../../ClsData/TestCase/test.txt", 'r')

TestResult = TestData(Test, TrainResult)

Test.close()

Output = open("../TestCase.output.txt", 'w')

Output.write(TestResult)

Test = open("../../../ClsData/TestCase/test.txt", 'r')

PerformanceResult = ComputePerformance(Test, TestResult, TrainResult[2], TrainResult[3])

Report = open("../TestCase.report.txt", 'w')

Report.write(PerformanceResult)

Train.close()
Test.close()
Output.close()
Report.close()


Train = open("../../../ClsData/train.txt", 'r')

TrainResult = TrainData(Train)

Test = open("../../../ClsData/test.txt", 'r')

TestResult = TestData(Test, TrainResult)

Test.close()

Output = open("../Test.output.txt", 'w')

Output.write(TestResult)

Test = open("../../../ClsData/test.txt", 'r')

PerformanceResult = ComputePerformance(Test, TestResult, TrainResult[2], TrainResult[3])

Report = open("../Test.report.txt", 'w')

Report.write(PerformanceResult)

Train.close()
Test.close()
Output.close()
Report.close()

