# I,Patel Manan, student number 000735153, certify that all code submitted is my own work; that I have not copied it from any other source.  I also certify that I have not allowed my work to be copied by others.

#GET input
userString = input ( "Please enter a string less than 30 characters: " )

#CALCULATE string length
stringLength =  len(userString)

centerMessage = int (stringLength / 2 )

#WHILE input lenght < 30
if (stringLength < 30) :
    print ( "Your centered string is: " )
    print ( " " * (40 - centerMessage) + userString )
      

else:
    print ( "I'm sorry, your string is too long, good bye. " )


 
