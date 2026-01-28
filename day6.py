import random
num = random.randint(10,20)
print (num)
i=1
user_input = input("Do you want to Play?: ")
while user_input == "Y" or user_input == "y" or user_input == "yes" or user_input == "Yes" or user_input == "YES":
    user_guess = int(input("Enter your guess between 10 and 20: "))
    if user_guess == num:
        print("You guessed it right in", i, "attempts")
        break

    else:
        print("You guessed it wrong, attempt times:", i )

    
    i = i + 1
    user_input = input("Do you want to play again?:  ")

print("Game Over")
