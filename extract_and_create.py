def extract(dirname,path,name):
    f = open(path+"/"+name, 'r')
    data = None
    for x in f:
        data = str.lower(x)

    data = str.split(x)
    stem = ['in', 'to', 'for', 'and', 'the', 'by', 'of', 'a', 'on', 'an', 'is', 'this', 'as', 'be', 'do', 'these',
            'any', 'which', 'their',
            'there', 'are', 'thus', 'from', 'it', 'at', 'or', 'can', 'that', 'will']
    special = [',', '.', '!', '(', ')', '\'']

    newdata = []
    dataset = set()

    for i in data:
        if i not in stem:
            newdata.append(str.lower(i))

    for i in newdata:
        set.add(dataset, i)

    data = ""

    for i in newdata:
        data += i

    f.close()

    # to create tag file

    f = open(dirname+"/"+"tag_file_"+name, "w")
    for i in dataset:
        sen = str(i) + " " + str(data.count(i)) + "\n"
        f.write(sen)

    f.close()

