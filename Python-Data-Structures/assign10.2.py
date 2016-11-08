# 10.2 Write a program to read through the mbox-short.txt and
#  figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and
# then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count = dict()
for line in handle:
    line=line.lstrip().rstrip()
    if line.startswith('From '): #there is one extra space under ' '
        t=line.split()[5]        #extract the time from line
        hour=t.split(':')[0]     #find the hour
        count[hour]=count.get(hour,0)+1  # count the frequency
lst=list()
for key,val in count.items():
    lst.append((key,val))
lst.sort()                        #sort the list
for key,val in lst:               #print the list out in required form
    print key,val
