# This is the terminal version of the game Bulls and Cows, in which we are supposed to guess the number within a given number of trials.

from random import randint

digits = '0123456789'
Number = ""
for _ in range(4):
    ind = randint(0, len(digits) - 1)
    Number += digits[ind]
    digits = digits[:ind] + digits[ind+1:]
if Number[0] == '0':
    Number = Number[1] + Number[0] + Number[2:]
i = 1
trials = int(input("Enter the number of trials: "))
if trials == 1:
    print("All the best with your confidence!")
while i <= trials:
    Guess = input(f"Guess {i}: ")
    if len(Guess) != len(Number):
        print("Enter the guess number of length 4!")
        continue
    if Guess == Number:
        print(f"You cracked it in {i} tries")
        break
    else:
        cows = bulls = 0
        for idx, digit in enumerate(Guess):
            if (digit in Number) and (Number[idx] == digit):
                bulls += 1
            elif (digit in Number) and (Number[idx] != digit):
                cows += 1
        i += 1
        print(f"{cows} COW and {bulls} BULL")
else:
    print(f"The Number is {Number}")
    print(f"You cannot guess the NUMBER in {trials} trials! Better luck next time.")
