#This is a comment

#Exercise 1: Look at the following code

fr1 = "apples"
fr2 = "bananas"
fr3 = input("Write down any fruit:\n")

#We want to show all the fruits we have
#Complete the code:

print(fr1)
print(fr2)
print(fr3)

#Now, let's tell the user what fruit do you like the most
#using the variables

print("My favorite fruit is: " + fr1)

#Now, the following code is 3 variables with the amount
#of each fruit that we have. Ask for the third number instead.

n1 = 4
n2 = 3
n3 = int(input("How many %ss do I have?\n" %fr3))

#Print the total amount of fruits that we have using
#the variables and string formatting

print("I have %d %s, %d %s and %d %ss" %(n1, fr1, n2, fr2, n3, fr3) )
total = n1 + n2 + n3
print("I have %s fruits in total." %str(total) )
