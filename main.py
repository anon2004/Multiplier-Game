from random import randint
number=int(input( "Enter a number you wanna test the multiples for>: "))
attempts=int(input("Enter the number of attempts you wanna test>: "))
points=0
for i in range(attempts):
 multiplier=randint(1,100)
 answer=int(input(f"if the multiplier is {multiplier} what is the answer?:"))
 if answer==multiplier*number:
  print("You nailed It")
  points=points+1
 else:
    print("Dummy")
    points=points-1
print(f"You got {points} points out of {attempts}") 
  

