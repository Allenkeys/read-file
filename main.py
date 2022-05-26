# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

# Create a list of punctuations which should be removed from the content of the file
regexList = [',', '?', '.', '!']

def readFileContent(filename):
    with open(filename, 'r') as txt:
        content = txt.read()
        for item in regexList:
            content = content.replace(item, '')
        return content



# def countWords():
#     text = readFileContent("./story.txt")
#     # [assignment] Add your code here
#     text = text.split()
#     return {"as": 10, "would": 20}



print(readFileContent('./story.txt'))

