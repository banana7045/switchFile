def countWordsFromFile():
    fileName =  input("file name here:  ")

    numberOfWords = 0

    file =  open(fileName, 'r')
    for line in file:
        words = line.split()
        numberOfWords = numberOfWords + len(words)
    print("the amount of words in the folder: ")
    print(numberOfWords)





countWordsFromFile()