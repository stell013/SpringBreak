

n = raw_input ("Please enter your username: ")
s = input ("Enter the year you were born: ")
H = raw_input ("Enter the name of the college you're transfered from: " )





import math
#c = math.sqrt(s)
myList = [ s]
print "       "
print "       "
print ("Here your data for now: " + n)
print ("Birth Year: " + `s`)
print ("College transfering: " + H)

               
print "----------------------------------------------------------------"




newInput2 = input ("Enter the year your started at " + H + ": " )
newInput3 = input ("Enter the year you drop school at " + H + ": ")

myList.append(newInput2)
myList.append(newInput3)


print " "

print " "


if max(myList) in myList:
    print ( n + " you should bring your transcrips graded until " + `newInput3`)
else:
    print ("Go to see an advisor")

print "  "


print " "

print '"SOME EXTRA INFORMATION ABOUT YOU "'
print "---------------------------------"
if myList.count (newInput2) == 2:
    if newInput2 < 2015 :
        print "You are a millenian"
    else:
        print "You are in highschool or probably younger than that"
elif myList.count(newInput2) == 1 and newInput3 >=2015 :
    print (" You have made some twists in your life since you started at " + H + "in " + `newInput2` + " and ended up in " + `newInput3`)
else:
    print ("This is a good start for you")

print " "

myList.sort()
print myList



print "     "                                      



raw_input ("Press <enter> to finalize the program")



