# from cs50 import get_string
import math
import re
import string
from nltk.tokenize import sent_tokenize


def main():
    text = input("Text: ")
    # returns list of words in text
    words = re.sub('['+string.punctuation+']', '', text).split()
    # return list of sentences in text
    sentences = sent_tokenize(text)
    lettersinwords = (num_letters(text) / len(words)) * 100
    wordsinsentences = (len(sentences) / len(words)) * 100
    index = 0.0588 * lettersinwords - 0.296 * wordsinsentences - 15.8
    if(math.ceil(index) > 15):
        print("Grade 16+")
    elif(math.ceil(index) < 2):
        print("Before Grade 1")
    else:
        print(f"Grade {math.ceil(index)}")


# returns the number of letters in 's' as an integer
def num_letters(s):
    text_length = len(s)
    letters = ""
    for i in range(text_length):
        if(s[i].isalpha() == True):
            letters += s[i]
    return len(letters)


main()