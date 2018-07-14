from collections import Counter

file = open("dev.txt","r")
file2 = open("train.txt","r")
file3 = open("test.txt","r")

mainString = ""

for strline in file:
    strline = file.read().replace('(', ' ')
    strline = strline.replace(')',' ')
    strline = strline.replace('1',' ')
    strline = strline.replace('2',' ')
    strline = strline.replace('3',' ')
    strline = strline.replace('4',' ')
    strline = strline.replace('5',' ')
    strline = strline.replace(',',' ')
    strline = strline.replace('.',' ')
    mainString = mainString + strline

for strline in file2:
    strline = file.read().replace('(', ' ')
    strline = strline.replace(')',' ')
    strline = strline.replace('1',' ')
    strline = strline.replace('2',' ')
    strline = strline.replace('3',' ')
    strline = strline.replace('4',' ')
    strline = strline.replace('5',' ')
    strline = strline.replace(',',' ')
    strline = strline.replace('.',' ')
    mainString = mainString + strline

for strline in file3:
    strline = file.read().replace('(', ' ')
    strline = strline.replace(')',' ')
    strline = strline.replace('1',' ')
    strline = strline.replace('2',' ')
    strline = strline.replace('3',' ')
    strline = strline.replace('4',' ')
    strline = strline.replace('5',' ')
    strline = strline.replace(',',' ')
    strline = strline.replace('.',' ')
    mainString = mainString + strline
    
wordList = mainString.split(" ")

myset = set(wordList)
print(len(myset))