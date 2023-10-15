command = ""
started = False
while True:
    command = input(">").lower()
    if command== "start":
        if started:
            print("The car has already started.")
        else:
            started = True
            print("The car started...Ready to go!")

        
    elif command== "stop":
        if not started:
            print("The car has already stopped. ")
        else :
            started = False
            print("The car stopped.")
    elif command == "help":
        print("""
Start - to start the car
Stop - to stop the car
Quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("Don't Understand.")



