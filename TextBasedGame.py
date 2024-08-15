# Michael Angel Cevallos
# Text based game that allows player to move through rooms and collect items
# Southern New Hampshire University

# Function to display the game instructions to the player
def show_instructions():
    # Print a main menu and the game instructions
    print()
    print("====== Welcome to 'The Silver Surfers Quest! Damsel In Distress' game! ===========".upper())
    print()
    print("INFO: ")
    print(
        'WELCOME TO THE GAME: You are the amazing Marvel superhero, THE SILVER SURFER , and can move through 8 Rooms.')
    print('** 6 of these rooms contain items you NEED to collect in order to defeat The Joker.')
    print()
    print('If you reach the final room, HINT: The SECRET HIDEOUT, without collecting all 6 items first,')
    print('You will be DESTROYED BY THE JOKER and LOSE the game.')
    print(
        "=== YOUR Mission Statement: COLLECT all 6 items located throughout the 8 rooms before reaching the final room so you can save the Damsel in distress. ====")
    print()
    print("HOW TO PLAY: ")
    print("TO MOVE: \nWHEN ASKED type a direction and press enter, your options : North, South, East, West.")
    print("If your direction is not an option because there is no room that way, pick another direction.")
    print("You will be asked if you want to pick up the item in the room (if there is one),")
    print(
        "if you say 'yes' it will be stored in your Inventory, If you choose 'no' the item stays in the room, you can always come back and get it later")
    print()
    print('TO END OR QUIT: ')
    print(
        "======= WHEN ASKED WHAT DIRECTION YOU WANT TO GO Type 'exit' and the game will stop. GOOD LUCK SURFER! =======")


# Function to show the player's current status (room and inventory)
def show_status(current_room, inventory, rooms):
    # Print the current room the player is in
    print(f"\n>>>> YOU ARE CURRENTLY IN THE :  {current_room} ROOM")

    # Print the current inventory of items collected by the player
    print(f">>>> YOUR CURRENT INVENTORY : {inventory}")

    # Check if there's an item in the current room that hasn't been collected
    if 'item' in rooms[current_room] and rooms[current_room]['item'] not in inventory:
        print(f"You found an item in the room : {rooms[current_room]['item']}")

    # Separator for clarity in the output
    print("----------------------")
    print()


# Function to determine the new room based on the player's move
def get_new_room(current_room, direction, rooms):
    # Check if the direction is valid in the current room's dictionary
    if direction in rooms.get(current_room, {}):
        # Return the new room based on the direction
        return rooms[current_room][direction]
    # Return None if the direction is not valid
    return None


# Main function that runs the game
def main():
    # Dictionary linking rooms to their possible moves and items
    rooms = {
        'Abandoned Laboratory': {'West': 'Enchanted Forest'},
        'Enchanted Forest': {'East': 'Abandoned Laboratory', 'South': 'Ancient Temple', 'item': 'Superhero Suit'},
        'Ancient Temple': {'North': 'Enchanted Forest', 'West': 'Underground Sewer', 'South': 'High-Tech Control Room',
                           'East': 'Frozen Cave', 'item': 'Magic Key'},
        'Underground Sewer': {'East': 'Ancient Temple', 'item': 'Encrypted Notebook'},
        'High-Tech Control Room': {'North': 'Ancient Temple', 'East': 'Abandoned Amusement Park',
                                   'item': 'Utility Belt'},
        'Abandoned Amusement Park': {'West': 'High-Tech Control Room', 'item': 'Ancient Map'},
        'Frozen Cave': {'West': 'Ancient Temple', 'North': 'Secret Hideout', 'item': 'Energy Drink'},
        'Secret Hideout': {'South': 'Frozen Cave'}
    }

    # Set the player's starting position to the 'Abandoned Laboratory'(STARTING ROOM OUT OF 8, NO ITEM HERE)
    current_room = 'Abandoned Laboratory'

    # Initialize the player's inventory as an empty list
    inventory = []

    # Call the function to show the game instructions
    show_instructions()

    # Call the function to show the player's initial status
    show_status(current_room, inventory, rooms)

    # Main game loop, continues until the player types exits or wins the game
    while current_room != 'exit':   # keep running the game if the player doesnt choose 'exit' as an option
        # Check if there's an item in the current room that hasn't been collected
        if 'item' in rooms[current_room] and rooms[current_room]['item'] not in inventory:
            item = rooms[current_room]['item']

            # Prompt the player to pick up the item or move
            action = input(
                f"You see a {item} here. Do you want to pick it up or keep moving? (pick up/move): ").strip().lower()

            if action == 'pick up':
                # Add the item to the player's inventory if they choose to pick it up
                inventory.append(item)
                print(f"{item} added to your inventory.")
                print('Items in Inventory:', inventory)
                print()

            elif action != 'move':
                # If the player enters an invalid choice, prompt them again
                print("Invalid choice. Please type 'pick up' or 'move'.")
                continue  # Continue to the next iteration of the loop without processing movement

        # Prompt the player to enter a direction to move
        move = input("ENTER WHICH DIRECTION YOU WANT TO GO (North, South, East, West, or exit): ").strip().capitalize()
        print()

        # Handle exit command, stop the game if the player types 'exit'
        if move.lower() == 'exit':
            print("Thanks for playing. Goodbye!")
            break

        # Get the new room based on the player's move
        new_room = get_new_room(current_room, move, rooms)
        if new_room:
            # Update the current room if the move is valid
            current_room = new_room
            # Show the updated status after the move
            show_status(current_room, inventory, rooms)
        else:
            # Inform the player if the move is invalid
            print("**** THERE IS NO ROOM IN THAT DIRECTION. TRY AGAIN! *****")

        # Check for the win condition: if all 6 items are collected and the player is in the 'Secret Hideout'
        if len(inventory) == 6 and current_room == 'Secret Hideout':
            print("Congratulations! You've collected all the items and won the game!")
            break

        # Check for the lose condition: if the player reaches the 'Secret Hideout' without collecting all 6 items
        if current_room == 'Secret Hideout' and len(inventory) < 6:
            print('NOM NOM...GAME OVER!')
            print('Thanks for playing the game. Hope you enjoyed it.')
            break


# Check if the script is being run directly (not imported as a module)
if __name__ == "__main__":
    # Start the game by calling the main function
    main()
