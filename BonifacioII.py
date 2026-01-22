player_name = input("Enter your name:")
health = 100
location = "forest"

health -=20 # player loses health
print(f"{player_name}, your health is now {health}")

def show_status(name, health, location):
    print(f"{name}, you are in the {location} with health {health}.")

show_status(player_name, health, location)

if health <= 0:
    print(f"{player_name}, you have perished in the {location}. Game Over.")
else:
    print(f"{player_name}, you continue your adventure in the {location}.")

# Simple adventure game scenario

# Player takes damage and status is displayed
# Player's fate is determined based on health
# Player's name, health, and location are managed and displayed

choice = input("You see a wolf. Do you fight (f) or run (r)? ")
if choice == 'f':
    health -= 30
    print("You chose to fight and lost some health.")
elif choice == 'r':
    print("You chose to run away safely.")
show_status(player_name, health, location)

print("\nAfter dealing with the wolf, you continue walking...\n")

choice = input ("You find a treasure chest. do you open it (o) or leave it (l)?")
if choice == 'o':
    health += 50
    print("You opened the chest and gained health!")
elif choice == 'l':
    print("You left the chest alone.")
else:
    print("Invalid choice.")
show_status(player_name, health, location)
if health <= 0:
    print(f"{player_name}, you have perished in the {location}. Game Over.")
else:
    print(f"{player_name}, you continue your adventure in the {location}.")
    
    print("Congratulations! You have survived the adventure.")
       
    
