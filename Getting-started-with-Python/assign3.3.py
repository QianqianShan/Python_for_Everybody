# 3.3 Write a program to prompt the user for a score using raw_input. Print out a letter grade based on the
# following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of
# 0.85.

score = raw_input("Enter Score: ")
score=float(score) #make sure it's a float number
if score <=1 and score >=0.9:
    print "A"
elif score <0.9 and score >=0.8:
    print "B"
elif score <0.8 and score >=0.7:
    print "C"
elif score <0.7 and score >=0.6:
    print "D"
elif score<0.6 and score <0.6:
    print "F"
else:
    print "Error"
