import os

def find(keylist, wordData, wordCounts):
    length = len(keylist)

    finCount = 0
    for i in keylist:
        index = None
        if i in wordData:
            index = wordData.index(i)
            finCount += (int(wordCounts[index])*1.0)/(length*1.0)
    return finCount/(length*1.0)


def search(path):
    a = input("Enter string to be searched: ")
    a = str.lower(a);
    keywords = str.split(a)
    print(keywords)
    dirs = os.listdir(path)
    tag = []
    tagdata = []
    result = []

    for name in dirs:
        tagdata = []
        if name.endswith(".txt") and "tag" in name:
            f = open(path+"/"+name, 'r')
            for x in f:
                sen = str.lower(x)
                sen = str.replace(sen, "\n", "")
                tagdata.append(sen)

            wordData = []
            wordCount = []
            for words in tagdata:
                word = words.split(" ")
                wordData.append(word[0])
                wordCount.append(word[1])

            result.append(name)
            result.append(find(keywords, wordData, wordCount))
            f.close()
    print(result)
    return result

