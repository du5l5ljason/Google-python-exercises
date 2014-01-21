# Project Name: Google Python Exercise Test.
# This is a project by Tingfang Du. The purpose of this project is to write test scripts
# when I was learning Python using Google python exercise as a material.
# Source code: https://github.com/du5l5ljason/Google-python-exercises

# File Name: sort_test.py
# Description: Function that runs some tests for sorting in Python
import utils

# Sort a dict by value.
def sort_dict_by_value(dict):
    result = sorted(dict.items(), key=lambda x:x[1])
    return result

def sort_dict_by_keyname(dict):
    result = sorted(dict.items(), key=lambda x:x[0])
    return result

def runTest():

    print
    print 'sort_dict_by_value'
    utils.test(sort_dict_by_value({'Japan':23, 'Germany':4, 'Brazil':2, 'China':89}),
                                  {'Brazil':2, 'Germany':4, 'Japan':23, 'China':89})

if __name__ == '__main__':
  runTest()

# End of sort_test.py
