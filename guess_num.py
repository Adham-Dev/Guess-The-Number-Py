import random

num = random.randint(1, 500)
guess = None
counter = 0    

while guess != num:
    guess = input("Guess a number between 1 and 500: ")
    guess = int(guess)
    counter = counter + 1
    
    if guess > num :                
        if guess > num+100: 
            print("--> Too High")
                    
        else:                       
            print("--> High")
        
        
    elif guess < num :
        if guess < num-100:
            print("--> Too low")
        
        else:
            print("--> Low")
        
    
    
if guess == num:
    print("----------------------------------")
    print("True the number was " + str(num))
    if counter == 1:
        print("You did it in " + str(counter) + "st time")
    elif counter == 2:
        print("You did it in " + str(counter) + "nd time")
    elif counter == 3:
        print("You did it in " + str(counter) + "rd time")
    else:
        print("You did it in " + str(counter) + "rd time")
    