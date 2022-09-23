def SplitString(text):

    splitText=text.split()
    return sorted(splitText)


sentence=str(input("Enter a text: "))
print(' '.join(SplitString(sentence)))