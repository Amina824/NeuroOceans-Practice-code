import random

i = 1
while i <= 5:
    print(i)
    i += 1

jackpot = random.randint(1, 10)
tries = 0

while tries < 3:
    guess = int(input("guess the number (1-10): "))
    tries += 1
    if guess == jackpot:
        print("jackpot!! you won in", tries, "tries")
        break
    elif guess < jackpot:
        print("too low")
    else:
        print("too high")
else:
    print("you lost, number was", jackpot)
