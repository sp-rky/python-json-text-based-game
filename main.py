import json
import time
import saves
from exceptions import *

# store the story json into a dictionary
with open('story.json') as f:
    story = json.load(f)

with open('saves.json', 'r') as f:
    saveFile = json.load(f)

# load the help help message
with open('help_messages.txt') as f:
    helpMessage = '\n'.join(line.strip() for line in f)

inventory, locationCode = saves.load(saveFile)

print('''
Possible Commands:
move <direction>
pickup <item>
exit
''')

# main game loop
while True:
    # tell the user their position and possible movements the user can make
    print(f"You are in a {story[locationCode]['location']}.")
    time.sleep(0.25)
    print(story[locationCode]['desc'])
    time.sleep(0.25)
    # store all the possible movements, makes code a lot simpler and saves a lot of typing
    possibleMovements = [i for i in story[locationCode]['possibleMovements']]
    if len(possibleMovements) > 1:
        print(f"You can go {', '.join(possibleMovements[:-1])}, or {possibleMovements[-1]}.")
    else:
        print(f"You can go {possibleMovements[-1]}.")
    time.sleep(0.25)

    # ask the next direction, exiting if needed
    command = input('What do you do? ').lower()
    time.sleep(0.25)

    # perform the command and raise an InvalidCommand error if there is a mistype
    try:
        # exit the program
        if command == 'exit':
            break
        # move the player into the required room, if they have the required item in their inventory
        elif command.split()[0] == "move":
            # ensure it is a valid movement
            if command.split()[1] in possibleMovements:
                requiredItem = story[locationCode]['possibleMovements'][command.split()[1]][0]
                # if there is no required item (a None object) then just move them
                if not requiredItem:
                    locationCode = story[locationCode]['possibleMovements'][command.split()[1]][1]
                # otherwise ensure the item is in their inventory
                elif requiredItem:
                    if requiredItem in inventory:
                        locationCode = story[locationCode]['possibleMovements'][command.split()[1]][1]
                    else:
                        raise ItemNotInInventory(requiredItem)
            else:
                raise InvalidCommand
        # pick up the item, if it exists in the room
        elif command.split()[0] == "pickup":
            if command.split()[1] in story[locationCode]['availableItems'] and command.split()[1] not in inventory:
                inventory.append(command.split()[1])
            else:
                raise ItemDoesNotExist(command.split()[1])
        elif command.split()[0] == "help":
            print(helpMessage)
        else:
            raise InvalidCommand
    except InvalidCommand:
        print("Invalid Command!")
    except ItemDoesNotExist as e:
        print(f'There is no item named {e}.')
    except ItemNotInInventory as e:
        print(f'You do not have the required {e}.')
    except IndexError:
        print("Wrong number of inputs!")
    except Exception as e:
        print(f"Unknown error: {e}")
    # add a newline for formatting (makes the interface easier on the eyes)
    time.sleep(0.5)
    print()
    time.sleep(0.5)

# save the file, if the user wishes (handled within the function)
saves.save(saveFile, inventory, locationCode)
