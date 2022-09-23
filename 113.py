"""Write a Python program that returns a string sorted alphabetically by the first character of a given string of words. Go to the editor
Sample Data:
("Red Green Black White Pink") -> "Black Green Pink Red White"
("Calculate the sum of two said numbers given as strings.") -> ("Calculate as given numbers of sum said strings. the two")
("The quick brown fox jumps over the lazy dog.") -> ("The brown dog. fox jumps lazy over quick the")"""

def SortedString(text):

    return ' '.join(sorted(text.split()))


sentance=input("Enter orginal text: ")

print("The sorted string: ",SortedString(sentance))


print(' '.join(sorted("Today is firday".split())))