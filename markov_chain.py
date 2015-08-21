import random
import sys
import os

#filePath = "novels/"
#filePath = "speeches/"
#filePath = "Shakespeare/"
#filePath = "doyle/"
filePath = "watsky/"
inputFiles = os.listdir(filePath)

prefixDict = {}

# Build nested dictionaries 
for i in range(0, len(inputFiles)):
    file = open(filePath + inputFiles[i], 'r')
    fullText = file.read()
    words = fullText.split()
    for word in range(1, len(words) - 1):
        prefix = words[word - 1] + " " +words[word]

        prefix = prefix.strip("[]:()\"\"''")
        prefix = prefix.lower()

        nextWord = words[word + 1]
        nextWord = nextWord.strip("[]:()\"\"''")
        nextWord = nextWord.lower()
                            
        if prefix in prefixDict:
            if nextWord in prefixDict[prefix]:
                prefixDict[prefix][nextWord] = prefixDict[prefix][nextWord] + 1
            else:
                prefixDict[prefix][nextWord] = 1
        else:
            prefixDict[prefix] = {}
            prefixDict[prefix][nextWord] = 1
    file.close()

# Control Inputs
sentenceLength = 100
currentKey = ""

# Output chain!
print(currentKey, end=" ")

for j in range(0, sentenceLength):
    choices = []
    if currentKey not in prefixDict:
        currentKey = random.choice(list(prefixDict.keys()))
        
    for key in prefixDict[currentKey]:
        for k in range(0, prefixDict[currentKey][key]):
            choices.append(key)
    choice = random.choice(choices)
    print(choice, end=" ")
    currentKey = currentKey.split()[1] + " " + choice
