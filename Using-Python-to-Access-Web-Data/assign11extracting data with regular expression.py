# Finding Numbers in a Haystack
#In this assignment you will read through and
# parse a file with text and numbers.
# You will extract all the numbers in the file and compute the sum of the numbers.

# Data Files
# We provide two files for this assignment.
# One is a sample file where we give you the sum for your testing
# and the other is the actual data you need to process for the assignment.

# Sample data: http://python-data.dr-chuck.net/regex_sum_42.txt (There are 87 values with a sum=445822)
# Actual data: http://python-data.dr-chuck.net/regex_sum_314600.txt
# (There are 98 values and the sum ends with 347)
# These links open in a new window.
# Make sure to save the file into the same folder
# as you will be writing your Python program.
# Note: Each student will have a distinct data file for the assignment
#  - so only use your own data file for analysis.

import re
name=raw_input('Enter the file name:')
hand=open(name)
y=float(0)  # initialize y value
for line in hand:
    x = re.findall('[0-9]*[0-9]',line) #find numbers in each line and record it(them)
    if len(x)>0:
        y=sum(map(float,x))+y   # use 'map' to convert string numbers to float number
                                # and sum them if there are more than one number
print y

