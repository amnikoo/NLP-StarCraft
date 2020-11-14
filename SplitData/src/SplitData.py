from sklearn.model_selection import train_test_split

HumanSents = open("../../ProcessedData/Human/HumanSentsNorms.txt", 'r')
NotHumanSents = open("../../ProcessedData/NotHuman/NotHumanSentsNorms.txt", 'r')

HumanPhrases = HumanSents.read().split("\n")
NotHumanPhrases = NotHumanSents.read().split("\n")

HumanTrain, HumanTest = train_test_split(HumanPhrases, test_size=0.2)
NotHumanTrain, NotHumanTest = train_test_split(NotHumanPhrases, test_size=0.2)

HumanSentsTrain = open("../Human/HumanSentsTrain.txt", 'w')
HumanSentsTest = open("../Human/HumanSentsTest.txt", 'w')
NotHumanSentsTrain = open("../NotHuman/NotHumanSentsTrain.txt", 'w')
NotHumanSentsTest = open("../NotHuman/NotHumanSentsTest.txt", 'w')

HumanSentsTrain.write("\n".join(HumanTrain))
HumanSentsTest.write("\n".join(HumanTest))
NotHumanSentsTrain.write("\n".join(NotHumanTrain))
NotHumanSentsTest.write("\n".join(NotHumanTest))

HumanSents.close()
NotHumanSents.close()
HumanSentsTrain.close()
HumanSentsTest.close()
NotHumanSentsTrain.close()
NotHumanSentsTest.close()
