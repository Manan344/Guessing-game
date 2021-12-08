# I,Patel Manan, student number 000735153, certify that all code submitted is my own work; that I have not copied it from any other source.  I also certify that I have not allowed my work to be copied by others.

import random

newTotal = 0

a = 1
b = 1
randomNumber = random.randint(1 , 5)
print(randomNumber)
print( "Congratulations you have " + str(randomNumber) + " disks to play with. " ) 

while (a <= randomNumber) :
     print( "Dropping disk " + str(a) + "... ")
     b = 0
     tick = 0
     tock = 0

     while ( b < 5 ) :
          number = random.randint ( 1 , 100 )
          if (number <= 50) :
               print ( "-tick-" )
               b = b + 1
               tick = tick - 1
          else :
               print ( "-tock-" )
               b = b + 1
               tock = tock + 1

     a = a + 1
     totalSum = tick + tock
     print (totalSum)

     if (totalSum == 0) :
          total = 10000
          print ( "The disk landed in $10000, congratulations! " )
     elif (totalSum in [-1 , 1 , -5 , 5]) :
          total = 0
          print ( "The disk landed in $0, aww, too bad! " )
     elif (totalSum in [-2 , 2]) :
          total = 1000
          print ( "The disk landed in $1000, Congratulations! " ) 
     elif (totalSum in [-3 , 3] ) :
          total = 500
          print ( "The disk landed in $500, Congratulations! " )
     elif (totalSum in [-4 , 4] ) :
          total = 100
          print ( "The disk landed in $100, Congratulations! " )
          
          
     newTotal = newTotal + total

print ( "Your total prize winning today is $ " + str (newTotal) )     
               
               
     
     
          
         
               
               




