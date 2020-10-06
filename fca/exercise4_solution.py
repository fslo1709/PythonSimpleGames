"""You can add your own words to the guesser, you can
    play to guess a random letter, and you can remove words
    from the game as well.
"""

import random

maxClues = 3
#Base words:

myList = ["car", "computer", "plane", "lion"]

dict1 = {"car": "It's a type of vehicle", "computer": "It has a screen", "plane": "It's a vehicle", "lion": "Has a big mane"}
dict2 = {"car": "It has four wheels", "computer": "It's an electronic used to code", "plane": "It has wings", "lion": "King of the jungle"}
dict3 = {"car": "The most common one in a city", "computer": "We use it in class", "plane": "We use it to travel", "lion": "Roars"}

clues = [dict1, dict2, dict3]   #To use the first, second or third clue

def PrintAllWords():
    for w in myList:
        print(w)

def PrintAllClues(w):
    for i in range(maxClues):
        print("%d. %s" %(i + 1, clues[i][w]))
    
def editClue(numClue, input_word):
    if numClue < 1 or numClue > maxClues:
        print("Enter a valid Clue number (1, 2, 3)")
    else:
        clues[numClue - 1][input_word] = input("Enter the new clue for clue number %d\n" %numClue)

if __name__ == "__main__":
    flag = True
    print("You can play to guess a word based on clues, or you can add your own\nwords to the game!")
    while flag:         #So the program runs until we tell it to play
        print("Input E to edit a word, Input A to add a word")
        print("Input P to print all words and clues")
        print("Input D to delete a word, Input X to exit and play")
        ans = input().lower()
        if ans == "x":
            flag = False
        elif ans == "e":
            print("Which word do you want to edit?")
            PrintAllWords()
            ans = input()
            if ans not in myList:
                print("The word is not in the list")
            else:
                print("Which clue do you want to edit? Input a number (1, 2, 3)")
                PrintAllClues(ans)
                num = int(input())
                editClue(num, ans)
        elif ans == "a":
            ans = input("Input your new word:\n")
            if ans in myList:
                print("This word already exists")
            else:
                myList.append(ans)
                for i in range(maxClues):
                    editClue(i+1, ans)
        elif ans == "p":
            for w in myList:
                print("%s:" %w)
                for d in clues:
                    print(d[w])
        elif ans == "d":
            print("Which word do you want to delete?")
            PrintAllWords()
            ans = input()
            if ans not in myList:
                print("The word is not in the list")
            else:
                myList.remove(ans)      
        else:
            print("Invalid input")
    flag = True
    while flag:
        secret_index = random.randint(0, len(myList) - 1)
        secret = myList[secret_index]
        guesses = 0
        inner_flag = True
        while guesses < maxClues and inner_flag == True:
            print("Clue No. %d: %s" %(guesses + 1, clues[guesses][secret]))
            guesses += 1
            user_guess = input("Make your guess. This is guess No. %d out of %d\n" %(guesses, maxClues)).lower()
            if user_guess in myList:
                inner_flag = False
        if inner_flag == True:
            print("You lost :( The correct answer is: %s" %secret)
        else:
            print("Congratulations! You got the correct word!")
        ans = input("Do you want to play again? y/n\n").lower()
        if ans == "n":
            flag = False
        else:
            print("x")
