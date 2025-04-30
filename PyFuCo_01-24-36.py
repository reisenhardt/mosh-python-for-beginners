number = 9
i = 1
guess_number = ""
while i < 5:
    guess_number = int(input("Guess a number: "))
    i += 1
    if guess_number == number:
        print("Der Wahnsinn, Du hast es geschafft!")
        break
    print(f"Bitte noch einmal probieren! Du hast noch {5-i} Versuche!")
else:
    print("Sorry, you failed!")

print("Das war's. ")