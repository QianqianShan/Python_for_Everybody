# 9.4 Write a program to read through the mbox-short.txt and
# figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of
# those lines as the person who sent the mail. The program creates
#  a Python dictionary that maps the sender's mail address to a count
#  of the number of times they appear in the file. After the dictionary
# is produced, the program reads through the dictionary using a maximum
# loop to find the most prolific committer.

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

count = dict()
for line in handle:
    line=line.lstrip().rstrip()
    if line.startswith('From '): #there is one extra space under ' '
        t=line.split()
        count[t[1]]=count.get(t[1],0)+1

biggest=max(count.values())   # find the maximum number in the dictionary
for key in count:
    if count[key] is biggest:   # print as the required form
        print key,biggest

