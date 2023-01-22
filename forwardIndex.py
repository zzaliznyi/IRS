import os

def createDictionary():
    appendedBuffer = {}
    keys = {}
    with open('keys.txt', 'r') as keysFile:
        keys = keysFile.read().lower().split()
    cwd = os.getcwd()
    os.chdir(cwd + '/textFiles')
    fileList = os.listdir(os.getcwd())
    fileList.sort()
    for file in fileList:
        with open(file, 'r') as f:
            words = f.read().lower().split()
            appendedBuffer[f.name] = []
            for word in words:
                if word[-1] in [',', '!', '?', '.']:
                    word = word[:-1]
                if word in keys and word not in appendedBuffer[f.name]:
                    appendedBuffer[f.name] += [word]
    os.chdir(cwd)
    return appendedBuffer, cwd

def writeToFile(words, cwd):
    os.chdir(cwd)
    with open('forwardIndex.txt', 'w') as indexFile:
        for file, files in words.items():
            indexFile.write(file[:file.find(".txt")] + " ")
            for word in files:
                indexFile.write(word + " ")
            indexFile.write('\n')

writeToFile(*createDictionary())