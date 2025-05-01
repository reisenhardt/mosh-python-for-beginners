command = ""
started = False
i = 1
while True:
    command = input("> ")
    if command == "help":
            print("""
start - to start the car
stop - to stop the car
quit - exit""")
    elif command == "start":
        if started:
            print("Car has already been started!")
        if not started:
            print("Car started...Ready to go!")
            started = True
    elif command == "stop":
        if not started:
            print("Car has already been stopped!")
        elif started:
            print("Car stopped.")
            started = False
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that...")