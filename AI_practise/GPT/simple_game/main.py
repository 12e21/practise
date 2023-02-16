# This is a more complex text game written in Python

# Welcome to the game!

print("Welcome to the game!")

# Get the player's name
name = input("What is your name? ")
print("Hello, " + name + "!")

# Set up the game loop 
playing = True 
while playing: 

    # Ask the player what they want to do 
    action = input("What would you like to do? (walk/run/fight/quit) ")

    # Respond to the player's action 
    if action == "walk": 
        print("You take a leisurely stroll around the park.") 

    elif action == "run": 
        print("You sprint around the park, feeling energized.") 

    elif action == "fight": 
        enemy = input("Who would you like to fight? (zombie/dragon/goblin)")

        if enemy == "zombie": 
            print("You punch and kick the zombie until it falls down.")

        elif enemy == "dragon": 
            print("You use your sword and shield to battle the dragon.")

        elif enemy == "goblin": 
            print("You throw rocks at the goblin until it runs away.")

        else: 
            print("I don't understand that command.")

    elif action == "quit": 
        print("Thanks for playing!") 
        playing = False 

    else: 
        print("I don't understand that command.")
