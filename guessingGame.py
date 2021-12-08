# I,Patel Manan, student number 000735153, certify that all code submitted is my own work; that I have not copied it from any other source.  I also certify that I have not allowed my work to be copied by others.

import random

randomNumber = random.randint(1 , 100)

pickedNumber = 0

while True:
    print( "I picked a number between 1 and 100 inclusive, can you guess it?" )
    guess = input()
    number = int(guess)

    pickedNumber = pickedNumber + 1
    if number == randomNumber:
        break

    elif number < randomNumber:
        print ( "Sorry, my number is higher than that. Try again!" )

    elif number > randomNumber:
        print ( "Sorry, my number is lower than that. Try again!" )

  

if number == randomNumber:
    pickedNumber = str(pickedNumber)
    print ( "Yes! That's correct! It took you " + pickedNumber + " guesses to find my number." )


