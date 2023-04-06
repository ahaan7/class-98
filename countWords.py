def countWordsfromfile():
    fileName=input("enter the file name -- ")
    noofwords=0
    file=open(fileName)
    for line in file:
        words=line.split()
        noofwords+=len(words)
    
    print("no of words = ",noofwords)

countWordsfromfile()