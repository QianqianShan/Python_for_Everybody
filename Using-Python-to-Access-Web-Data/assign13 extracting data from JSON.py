# Extracting Data from JSON

# In this assignment you will write a Python program somewhat similar to
# http://www.pythonlearn.com/code/json2.py.
# The program will prompt for a URL, read the JSON data from that URL using urllib and
#  then parse and extract the comment counts from the JSON data, compute the sum of the
# numbers in the file and enter the sum below:
# We provide two files for this assignment.
#  One is a sample file where we give you the sum for your testing and
# the other is the actual data you need to process for the assignment.

# Sample data: http://python-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://python-data.dr-chuck.net/comments_314606.json (Sum ends with 53)
# You do not need to save these files to your folder since your program will read the
#  data directly from the URL.
#  Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.

# The closest sample code that shows how to parse JSON and extract a list is json2.py.
#  You might also want to look at geoxml.py to see how to prompt for a URL and retrieve data from a URL.

import urllib
import json

url=raw_input('Enter a url:')
if len(url)<1: url="http://python-data.dr-chuck.net/comments_314606.json"

print 'Retriving', url

data=urllib.urlopen(url).read()
print 'Retriving',len(data),'characters'
info=json.loads(data)

sum=0
count=0
for item in info['comments']:
    count+=1
#    print item['count']
    sum+=int(item['count'])

print "Count is:",count
print "Sum is:",sum
