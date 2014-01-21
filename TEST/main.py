# Project Name: Google Python Exercise Test.
# This is a project by Tingfang Du. The purpose of this project is to write test scripts
# when I was learning Python using Google python exercise as a material.
# Source code: https://github.com/du5l5ljason/Google-python-exercises

# File Name: main.py
# Description: The main entrance of the test code.

import sys
import strTest1

# Define a main() function that handles all of the test code.
def main():
    # Get the command from the command line.
    if len(sys.argv) <= 1: # no specific command
        print 'Hello! This is a test Python learning program, please use the following commands:'
        print '-------- strTest -- test code of string repeat function'
    else:
        if sys.argv[1] == "str1":
            strTest1.runTest()
        else:
            print "No specific function!"

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()

# End of main.py