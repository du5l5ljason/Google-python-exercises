# Project Name: Google Python Exercise Test.
# This is a project by Tingfang Du. The purpose of this project is to write test scripts
# when I was learning Python using Google python exercise as a material.
# Source code: https://github.com/du5l5ljason/Google-python-exercises

# File Name: strRepeat.py
# Description: Function that enables create a repeat str.

import sys

def strRepeat(str, n, mode):
    """Returns the string str repeated n times.
    If mode is "normal" or default, just add the repeated strs at the end of the original str.
    If mode is "mirror", add the reversed strs to the end of the original str.
    """

    if mode == "normal" | mode == "":
        result = str * n
    elif mode == "mirror":
        result = str[::-1]
    else:
        result = ""

    print result
    return result

# End of strRepeat.py