""" This is how you add multiple line comments.

"""

""" Exercise 2: Can you finish this code that helps us
    do some math problems? We'll introduce you to two operators:
        - Summation Operator 
        - Factorial Operator
    We need to do three things:
        1) Ask for which operator you need
        2) Ask for which number to operate
        3) Print the result """

print("This program will help you do Summation from 0 to a number and Factorial")
option = input("Input S for summation, and F for factorial\n")

#Please fill in the lines with red comments:

if option == "S": #Summation option
    
    num = int(input("What positive number do you want to operate?\n"))
        
    if num > 0 and num < 10000: #Numbers have to be between 0 and 10000 to be valid
        
        res = 0    #Result variable
        for i in range(num):  #How many operations are we going to make?
            
            res = res + i        #What do we need to add?
        print("The summation from 0 to %d is: %d" %(num,res))
    else:
        print("Invalid input")
        
elif option == "F":   #Factorial option

    num = int(input("What positive number do you want to operate?\n"))
    
    if num < 0 or num > 50:         #Negative number (less than zero) is invalid, numbers bigger than 50 will cause an error
        
        print("Invalid input")

    elif num == 0:      #Factorial of zero is just 1, fill the condition

        print("1")
        
    else:
        
        res = 1
        i = num
        
        while i > 0: #We will multiply from num down to 1, so what do we need to check here?                               
            res = res * i     #What do we need to multiply?
            i = i - 1       #Decrease the conditional variable
            
        print("The factorial of %d is: %d" %(num, res))

else:
    print("Invalid input")
