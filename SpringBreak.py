n = raw_input ("Please enter your name: ")
s = input ("Enter the year you were born: ")
H = raw_input ("Enter the name of the college you're transfered from: " )
               
#m = pow (s,2)


import math
#c = math.sqrt(s)
myList = [ s]
print "       "
print "       "
print ("Here your data for now: " + n)
print ("Birth Year: " + `s`)
print ("College transfering: " + H)
#print `myList[0:2]` + " THIS JUST AN EXAMPLE OF HOW TO MAKE SLICING"
               
print "----------------------------------------------------------------"
#m = str (pow (s,2))

#this is just a way
#c  = str (math.sqrt(s))

#print "The square of the year: " + m
#print "Here the square root: " + `c`

#minimum = min(myList)
#imi = minimum in myList
#print `mimi` + ">> The mim number in my list is " + `minimum`

print "--------------------------------------------------------------"
#newInput = input ("Enter the year you started school: ")
newInput2 = input ("Enter the year your started at " + H + ": " )
newInput3 = input ("Enter the year you drop school at " + H + ": ")
#myList[0:] =
myList.append(newInput2)
myList.append(newInput3)


print " "
#print myList
print " "
#siblings=(">> " +`1999` + ". It\'s also the year when Ricky and Laura were born, Samira")

if max(myList) in myList:
    print ( n + " you should bring your transcrips graded until " + `newInput3`)
else:
    print ("Go to see an advisor")

print "  "

#JUST TRYING
#if myList.count (newInput) == 2: 
 #   print myList.append (" This year was witness of two important events in your life")
#elif myList.count (newInput) == 1:
 #   print "That was actually an awesome year"
#else:
 #   print " Well folk, 2013 is just once on your list . Just look at it, it\'s right below"

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

#minimum = min(myList)
#print "The minmum number of myList is: " + `minimum`

raw_input ("Press <enter> to finalize the program")



