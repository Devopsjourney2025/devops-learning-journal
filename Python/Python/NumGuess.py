import random
target = random.randint(3, 9)
print("target:", target)
print("Welcome to the Number Guessing Game!")

while True:
    num1 = int(input("Enter a number between 3 and 9: "))
    if num1 == target:
        print("🎉 Guess is correct! You win!")
        break  # Exit the loop
    else:
        print("❌ Guess is incorrect. Try again!")