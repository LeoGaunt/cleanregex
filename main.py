# NEED TO SPLIT BY EACH CHARACTER
# NOT RECOGNISING TEXT TO FIND
# IF RE.FINDALL ALWAYS FINDS []



import re

def findAll(txt, find):
    print(re.findall(find, '.'))
    if re.findall(find, '.') != []:
        finder = re.findall(find, '.')
        if re.findall(find, '\s'):
            finder.append('\s')
    elif re.findall(find, '\s'):
        finder = re.findall(find, '\s')
    else:
        return "Unknown character for search"
    findList = re.findall(txt, find)
    return findList

def findAllNum(txt, find):
    findList = re.findall(txt, find)
    return len(findList)

def findFirst(txt, find):
    firstFind = re.search(find, txt)
    return firstFind.start()

def split(txt, splitAt):
    splitList = re.split(splitAt, txt)
    return splitList

def splitMax(txt, splitAt, maxSplit):
    splitList = re.split(splitAt, txt, maxSplit)
    return splitList

def replace(txt, change, to):
    altString = re.sub(change, to, txt)
    return altString

def replaceMax(txt, change, to, maxNum):
    altString = re.sub(change, to, txt, maxNum)
    return altString

print(findAll("hello", "ell"))