import random

"""introduces player to the game"""
print("\nWelcome to GT.503")
print("You have stolen a Lamborghini Aventador and must get across state lines")
print("to avoid law enforcement. It is 100 miles to state lines.")
print("Do what you must to keep officers at a distance.\n")

# Variables
amount_gas = 100
cop_distance_driven = -10
distance_driven = 0
state_line_distance = 100
gas_fillups = 6
done = False


# this line asks user to begin
if not done:
    start = input("Would you like to begin? press 'y' or 'n': ")
    if start == "y":
        done = False
    elif start == "n":
        done = True

# This line asks user which roadways to drive on
if not done:
    print()
    print("""    A: highway (shortcut) 
    B: backroads (long way)""")
    player_input = input("Which road will you take? ")
    if player_input == "a":
        cops_proximity = 3
        print("\nYou have run into rush hour traffic!")
        print("The cops are", cops_proximity, "miles behind")

    elif player_input == "b":
        state_line_distance += 10
        cops_proximity = 10
        print("\nThe path is clear, but you extended your trip by 10 miles, totalling", state_line_distance, "miles!")
        print("The cops are", cops_proximity, "miles behind.")


# Main loop of game
        while not done:
            distance_from_cops = distance_driven - cop_distance_driven
            speed_limit = random.randrange(4, 9)
            drive_fast = random.randrange(10, 16)
            print("""
            A: Drive fast
            B: Drive the speed limit 
            C: Check gas level 
            D: Get gas
            Q: Quit""")
            print()
            player_input = input("What is your choice? ")
            if player_input.lower() == "q":
                done = True

# Drive Fast
            elif player_input.lower() == "a":
                print("\nYou accelerated to 150 mph!")
                print("You have gained distance away from the cops!")
                distance_driven += drive_fast
                amount_gas -= 28
                distance_from_cops = random.randrange(4, 9)


# Drive the speed limit
            elif player_input.lower() == "b":
                print("\nYou are driving the speed limit of 70 mph.")
                print("You have not gained nor lost distance from the cops.")
                distance_driven += speed_limit
                amount_gas -= 10


# Check gas Status
            elif player_input.lower() == "c":
                print("\nYour gas level is", amount_gas, "out of 100!")
                print("The cops are", distance_from_cops, "miles away.")
                print("You have", state_line_distance, "miles until you reach state lines.")
                print("You have", gas_fillups, "refuels remaining.")

# Hit the gas station to refuel
            elif player_input.lower() == "d":
                if amount_gas >= 80:
                    amount_gas += 20
                elif amount_gas == 90:
                    amount_gas += 10
                if gas_fillups == 0:
                    print("You have no more refills!")
                print("\nYou have gained", amount_gas, "gallons of fuel!")
                print("You have lost", distance_from_cops, "miles to the cops.")

# in-game checks
            if cops_proximity <= 5:
                print("The cops are very close!")
            if cops_proximity >= distance_driven:
                print("""You have been arrested!
                Your car is being impounded!
                Bail is set at $25,000.""")
                done = True
            if amount_gas <= 50:
                print("Fuel is halfway drained.")
            if amount_gas <= 25:
                print("One-Quarter tank remaining")
            if amount_gas == 0:
                print("""You have run out of fuel!
                You have been caught by the cops!
                Your car is being impounded!
                Bail is set at $25,000.""")
                done = True
