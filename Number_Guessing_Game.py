Secret_number= 7
Guess_count = 0
Guess_limit = 3

while Guess_count < Guess_limit:
    guess = int(input("Guess a number: "))
    Guess_count += 1
    if guess == Secret_number :
        print("Your guess is right")
        break

else :
    print("Your guess is wrong.")