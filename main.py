# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


# Create a list of punctuations to be removed from the text file
regexList = [',', '?', '.', '!']


# Read file and strip punctuations
def readFileContent(filename):
    with open(filename, 'r') as txt:
        content = txt.read()
        for item in regexList:
            content = content.replace(item, '')
        return content


# Count occurence of words in text
def countWords():
    text = readFileContent("./story.txt")
    dataDict = {}
    text = text.split()
    for word in text:
        if word in dataDict:
            dataDict[word] += 1
        else:
            dataDict[word] = 1  

    return dataDict          

  

print(countWords())

# print(readFileContent('./story.txt'))

