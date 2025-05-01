command = ""
i = 1
while True:
    command = input("> ")
    if command == "help":
            print("""
start - to start the car
stop - to stop the car
quit - exit""")
    elif command == "start":
        if i < 2:
            print("Car started...Ready to go!")
            i += 1
        elif i >= 2:
            print("Car has already been started!")
    elif command == "stop":
        if i == 2:
            print("Car stopped.")
            i -= 1
        elif i <= 1:
            print("Car has already been stopped!")
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that...")