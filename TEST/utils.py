# Project Name: Google Python Exercise Test.
# This is a project by Tingfang Du. The purpose of this project is to write test scripts
# when I was learning Python using Google python exercise as a material.
# Source code: https://github.com/du5l5ljason/Google-python-exercises

# File Name: utils.py
# Description: functions that support the test code.

# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
import re
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

# read a file and parse all of the words into a dict.
def parse_words_from_file(fn):
    words = []  # a list to store all words in a line
    dict = {}   # a dict to store the occurrences of each words.
    # check type of fn?
    f = open(fn, 'r')
    for line in f:
        words = re.findall(r"[\w']+", line)
        lower_words = [word.lower() for word in words]
        for word in lower_words:
            if not dict or not word in dict.keys():
                dict[word] = 1
            elif word in dict.keys():
                dict[word] += 1
    return dict

# Sort a dict by value.
def sort_dict_by_value(dict):
    result = sorted(dict.items(), key=lambda x:x[1])
    return result

def sort_dict_by_keyname(dict):
    result = sorted(dict.items(), key=lambda x:x[0])
    return result