import random
import Guesslogo
num = random.randint(1, 50)
print(Guesslogo.logo)
diff_level = input("Enter the level of difficulty...Type 'easy' or 'hard': ")

if diff_level == "easy":
    attempts = 10
    print(f"Yor have {attempts} attempts to guess the number!")

elif diff_level == "hard":
    attempts = 5
    print(f"Yor have {attempts} attempts to guess the number!")

else:
    print("Enter valid input!")

while (diff_level == "easy" and attempts > 0) or (diff_level == "hard" and attempts > 0):
    guess = int(input("Make a guess: "))
    if attempts == 0:
        print("You lost")
    elif guess < num:
        attempts -= 1
        if attempts ==0:
            print("Your chances are over!You Lost")
        else:
            print("Your guess is too low!")
    elif guess > num:
        attempts -= 1
        if attempts==0:
            print("You chances are over!You Lost")
        else:
            print("Your guess is too high!")
    else:
        print("Your guess is correct...You won!")
        break
