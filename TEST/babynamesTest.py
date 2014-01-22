# Project Name: Google Python Exercise Test.
# This is a project by Tingfang Du. The purpose of this project is to write test scripts
# when I was learning Python using Google python exercise as a material.
# Source code: https://github.com/du5l5ljason/Google-python-exercises

# File Name: babynamesTest.py
# Description: Function that runs word count

import sys
import utils
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  lines = open(filename, 'r')
  result = []
  yearFound = False
  print 'parse year!'
  for line in lines:
    if not yearFound:
        match = re.search(r'Popularity in \d+', line)
        if match:
            # parse the year from this line
            temp_str = str(match.group())
            print 'The line is ' + match.group()
            year = re.search(r'\d+', temp_str)
            if year:
                result.append(year.group())
                yearFound = True
            else:
                print 'Exception:!'

  print 'parse baby names and rankings'
  lines = open(filename, 'r')
  dict = {}
  for line in lines:
    match = re.search(r'<tr align="right"><td>(\d+)</td><td>([\w-]+)</td><td>([\w-]+)</td>', line)
    if match:
        dict[match.group(2)] = match.group(1)
        dict[match.group(3)] = match.group(1)

  baby_name_list = utils.sort_dict_by_keyname(dict)

  # remove parathesis
  for element in baby_name_list:
    new_str = element[0] + ', ' + element[1]
    result.append(new_str)

  return result


def runTest():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  print 'TEST: Write summary into file -- START!'
  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  data_file_names = []
  print 'get all of the data files'
  for filename in args:
    # check if filename is correct
    match = re.search(r'baby\d+.html', filename)
    if match:
        print match.group()
        data_file_names.append(filename)
    else:
        print "the filename is invalid!"

  dataSet = []
  print 'extract names'
  for filename in data_file_names:
    # extract_names from each file, the dataset is ['Year', 'name rank']
    data_set = extract_names(filename)

    if summary == False:
        print data_set
    else:
        # write into file
        filename = data_set[0] + '_summary.csv'
        f = open(filename, 'a')
        f.write(str(data_set))
        f.close()

  print 'TEST: Write summary into file -- DONE!'


if __name__ == '__main__':
  runTest()

# End of babynamesTest.py