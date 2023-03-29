#WRITE YOUR CODE IN THIS FILE
def hasL(word):
    numL= 0
    for i in range(0,len):
        if word[i] == "l":
            numL += 1
    if numL > 1:
        return True
    else:
        False