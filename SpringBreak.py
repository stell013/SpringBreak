s = input ("Enter the year you were born ")

m = pow (s,2)


import math
c = math.sqrt(s)
myList = [ s, m, c]

print ("This all your data for now:") 
print `myList[0:2]` + " THIS JUST AN EXAMPLE OF HOW TO MAKE SLICING"
print "----------------------------------------------------------------"
m = str (pow (s,2))

#this is just a way
#c  = str (math.sqrt(s))

print "The square of the year: " + m
print "Here the square root: " + `c`

minimum = min(myList)
mimi = minimum in myList
print `mimi` + ">> The mim number in my list is " + `minimum`

print "--------------------------------------------------------------"
newInput = input ("Enter the year you started school: ")
newInput2 = input ("Enter the year your started at the Cujae: ")
newInput3 = input ("Enter the year you drop school at Cujae: ")
#myList[0:] =
myList.append( newInput)             #,newInput2, newInput3)
myList.append (newInput2)
myList.append(newInput3)
print " "
print myList
print " "
siblings=(">> " +`1999` + ". It\'s also the year when Ricky and Laura were born, Samira")

if 1999 in myList:
    print siblings
else:
    print "False"

print "  "
if myList.count (2013) == 2: 
    print myList.append ("2013 is two times here")
else :
    print " Well folk, 2013 is just once on your list . Just look at it, it\'s right below"

print " "    
myList.sort()
print myList



print "                                           "

#minimum = min(myList)
#print "The minmum number of myList is: " + `minimum`

raw_input ("Press <enter> to finalize the program")



