def GetDataGram(FilePath):
    File = open(FilePath, 'r')
    FileRead = File.read()
    FileList = FileRead.split("\n")
    FileDict = {}
    FileDict["UNK"] = 0
    for i in range(len(FileList)):
        sentWords = FileList[i].split()
        for word in sentWords:
            if word not in FileDict:
                if FileRead.count(word) == 1: # I took one_occurence word = UNK
                    FileDict["UNK"] += 1
                    sentWords = [w.replace(word, "UNK") for w in sentWords]
                else:
                    FileDict[word] = FileRead.count(word)
        FileList[i] = " ".join(sentWords)
    File.close()
    File = open(FilePath, 'w')
    File.write("\n".join(FileList))
    File.close()
    return(FileDict)

def UniGram(FileDict, FileInPath, FileOutPath):
    FileIn = open(FileInPath, 'r')
    FileRead = FileIn.read()
    FileIn.close()
    FileReadOneLine = FileRead.replace("\n"," ")
    FileWords = FileReadOneLine.split()
    OutList = []
    Divisor = len(FileWords)+len(FileDict) # count(AllWords) + V
    FileOut = open(FileOutPath, 'w')
    for word in FileWords:
        OutListWord = word+"|"+str((FileDict[word]+1) / Divisor)
        if OutListWord not in OutList:
            OutList.append(OutListWord)
            FileOut.write(OutListWord+"\n")
    FileOut.close()

def BiGram(FileDict, FileInPath, FileOutPath):
    FileIn = open(FileInPath, 'r')
    FileRead = FileIn.read()
    FileIn.close()
    FileReadOneLine = FileRead.replace("\n"," ")
    FileWords = FileReadOneLine.split()
    FileList = FileRead.split("\n")
    FileBiList = []
    for i in range(len(FileList)):
        FileList[i] = "<s> " + FileList[i] + " </s>"
        sentWords = FileList[i].split()
        for j in range(len(sentWords)-1):
            FileBiList.append((sentWords[j], sentWords[j+1]))
    OutList = []
    V = len(FileDict)
    FileDict["<s>"] = len(FileList)
    FileDict["</s>"] = len(FileList)
    FileOut = open(FileOutPath, 'w')
    for word in FileBiList:
        OutListWord = (word[0]+"|"+word[1]+"|"+
        str((FileBiList.count(word) + 1) / (FileDict[word[0]] + V)))
        if OutListWord not in OutList:
            OutList.append(OutListWord)
            FileOut.write(OutListWord+"\n")
    FileOut.close()
    return(FileBiList)

def TriGram(FileDict, FileBiList, FileInPath, FileOutPath):
    FileIn = open(FileInPath, 'r')
    FileRead = FileIn.read()
    FileIn.close()
    FileReadOneLine = FileRead.replace("\n"," ")
    FileWords = FileReadOneLine.split()
    FileList = FileRead.split("\n")
    FileTriList = []
    for i in range(len(FileList)):
        FileList[i] = "<s> " + FileList[i] + " </s>"
        sentWords = FileList[i].split()
        for j in range(len(sentWords)-2):
            FileTriList.append((sentWords[j], sentWords[j+1], sentWords[j+2]))
    OutList = []
    V = len(FileDict)
    FileOut = open(FileOutPath, 'w')
    for word in FileTriList:
        OutListWord = (word[0]+"|"+word[1]+"|"+word[2]+"|"+
        str((FileTriList.count(word) + 1) / (FileBiList.count((word[0], word[1])) + V)))
        if OutListWord not in OutList:
            OutList.append(OutListWord)
            FileOut.write(OutListWord+"\n")
    FileOut.close()

in1Path = "../test/in.1gram"
out1Path = "../test/out.1gram.lm"
out2Path = "../test/out.2gram.lm"
out3Path = "../test/out.3gram.lm"
in1FileDict = GetDataGram(in1Path)
UniGram(in1FileDict, in1Path, out1Path)
in1BiList = BiGram(in1FileDict, in1Path, out2Path)
TriGram(in1FileDict, in1BiList, in1Path, out3Path)

HumanSentsTrainPath = "../../SplitData/Human/HumanSentsTrain.txt"
Human1GramPath = "../Human.1gram.lm"
Human2GramPath = "../Human.2gram.lm"
Human3GramPath = "../Human.3gram.lm"
HumanSentsTrainFileDict = GetDataGram(HumanSentsTrainPath)
UniGram(HumanSentsTrainFileDict, HumanSentsTrainPath, Human1GramPath)
HumanSentsTrainBiList = BiGram(HumanSentsTrainFileDict, HumanSentsTrainPath, Human2GramPath)
TriGram(HumanSentsTrainFileDict, HumanSentsTrainBiList, HumanSentsTrainPath, Human3GramPath)

NotHumanSentsTrainPath = "../../SplitData/NotHuman/NotHumanSentsTrain.txt"
NotHuman1GramPath = "../NotHuman.1gram.lm"
NotHuman2GramPath = "../NotHuman.2gram.lm"
NotHuman3GramPath = "../NotHuman.3gram.lm"
NotHumanSentsTrainFileDict = GetDataGram(NotHumanSentsTrainPath)
UniGram(NotHumanSentsTrainFileDict, NotHumanSentsTrainPath, NotHuman1GramPath)
NotHumanSentsTrainBiList = BiGram(NotHumanSentsTrainFileDict, NotHumanSentsTrainPath, NotHuman2GramPath)
TriGram(NotHumanSentsTrainFileDict, NotHumanSentsTrainBiList, NotHumanSentsTrainPath, NotHuman3GramPath)

