# import modules
from math import ceil
import markdown
import sys
import webbrowser
import os

# functions 
def bionicWord(word):
    # markdown bold special character
    bold = "**"

    length = len(word)
    boldLettersNo = ceil(length/2)

    return str(bold + word[:boldLettersNo] + bold + word[boldLettersNo:])


# get the file names passed from the command line after the program name
arguments = sys.argv[1:]

# output array
output = []

# go through each command line file name
for x in range(0, len(arguments)):
    print("running ... ", arguments[x])

    # array to store all the paragraphs in the file 
    paragraphs = []

    # error management for files that don't exist 
    try:
        file = open(arguments[x], "r")
        for y in file:
            paragraphs.append(y)
    except:
        print("error opening file ... ", arguments[x])

    # bionic the words
    for y in range(0, len(paragraphs)):
        words = paragraphs[y].split(" ")

        for z in range(0, len(words)):
            convert = bionicWord(words[z])
            words[z] = convert
        
        joined = " ".join(words)
        paragraphs[y] = joined

    output.append(paragraphs)
    
    print(arguments[x], "complete\n")


fileName = "BionicText.html"

# clear file
file = open(fileName, "w")
file.write("")
file.close()

for x in output:
    # convert markdown to HMTL
    for y in range(0, len(x)):
        x[y] = markdown.markdown(x[y])

    # write HTML to file 
    file = open(fileName, "a")
    for y in x:
        file.write(y)
    file .close()

# open browser with bionic text
filename = 'file:///'+os.getcwd()+'/' + 'BionicText.html'
webbrowser.open_new_tab(filename)