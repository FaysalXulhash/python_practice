command = ""

started = False

while True:
    command = input("-> ")
    if command == "start":
        if started:
            print("Car is already Running. ")
        else:
            started = True
            print("Car Start... ")

    elif command == "stop":
        if not started:
            print("Car is already stop. ")

        else:
            started = False
            print("Car stop...Please Stop!")

    elif command == "help" :
        print("""
Start -> To start the car.
Stop  -> To stop the car.
Help  -> To get help 
        """)
