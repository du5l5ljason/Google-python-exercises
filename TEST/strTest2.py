# Project Name: Google Python Exercise Test.
# This is a project by Tingfang Du. The purpose of this project is to write test scripts
# when I was learning Python using Google python exercise as a material.
# Source code: https://github.com/du5l5ljason/Google-python-exercises

# File Name: strTest2.py
# Description: Function that runs string Test 2
# End of strTest2.py

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s):
  # +++your code here+++
  if len(s) < 3:
    result = s;
  else:
    if s[-3:] == 'ing':
        result = ''.join([s, 'ly'])
    else:
        result = ''.join([s, 'ing'])
  return result


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
  # +++your code here+++
  oriStr1 = 'not'
  oriStr2 = 'bad'
  dstStr = 'good'
  if s.find(oriStr1) < s.find(oriStr2):
    result = s.replace(s[s.find(oriStr1):(s.find(oriStr2)+len(oriStr2))], dstStr)
  else:
    result = s
  return result


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def split_halves(s):
  """divide a string into two halves from the middle
  if the length is even, the front and back halves are the same length.
  if the length is odd, we'll say that the extra char goes in the front half.
  returns a list of the two halves.
  """
  result = []
  if len(s) % 2 == 0: # even
    result.append(s[:len(s)/2])
    result.append(s[len(s)/2:])
  else:
    result.append(s[:(int(len(s)/2)+1)])
    result.append(s[(int(len(s)/2)+1):])
  return result

def front_back(a, b):
  # +++your code here+++
  tuple_a = split_halves(a)
  tuple_b = split_halves(b)
  return ''.join([tuple_a[0], tuple_b[0], tuple_a[1], tuple_b[1]])

  # Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# runTest() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def runTest():
  print 'verbing'
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  print
  print 'not_bad'
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

  print
  print 'front_back'
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  runTest()