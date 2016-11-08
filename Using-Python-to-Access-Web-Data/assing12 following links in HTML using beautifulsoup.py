# Following Links in HTML Using BeautifulSoup
# In this assignment you will write a Python program that expands on
#  http://www.pythonlearn.com/code/urllinks.py.
# The program will use urllib to read the HTML from the data files below,
#  extract the href= vaues from the anchor tags,
# scan for a tag that is in a particular position relative to
# the first name in the list, follow that link and
# repeat the process a number of times and report the last name you find.

# We provide two files for this assignment.
# One is a sample file where we give you the name for your testing and
# the other is the actual data you need to process for the assignment

# Sample problem: Start at http://python-data.dr-chuck.net/known_by_Fikret.html
# Find the link at position 3 (the first name is 1).
# Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
# Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
# Last name in sequence: Anayah

# Actual problem: Start at: http://python-data.dr-chuck.net/known_by_Madelyn.html
#Find the link at position 18 (the first name is 1).
# Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
# Hint: The first character of the name of the last page that you will load is: R

#Strategy
#The web pages tweak the height between the links and hide the page
# after a few seconds to make it difficult for you to do the assignment
#  without writing a Python program.
# But frankly with a little effort and patience you can overcome
# these attempts to make it a little harder to complete the assignment
# without writing a Python program. But that is not the point.
# The point is to write a clever Python program to solve the program.



import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
times=int(raw_input('Enter the numer of times to repeat:')) # make sure the number is recognized as an integer
position=int(raw_input('Enter the position you look at:'))

# Retrieve anchor tags, with a while loop
while times>0:
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    name=tags[position-1].contents[0] #contents[0] is the name 
    print name
    url=tags[position-1].get('href',None)   #follow the link
    times=times-1




### Note: fast way to check source of html
## Ctrl+u on windows
## Ctrl+Alt+u on Mac


