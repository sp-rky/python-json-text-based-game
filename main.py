import os
import json
import time

# import custom libraries
import saves
from exceptions import *
from print_ import *
from colour import colour

# store the story json into a dictionary
with open('story.json') as f:
    story = json.load(f)

with open('saves.json') as f:
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
    letterPrint(f"You are in a {story[locationCode]['location']}.")
    time.sleep(0.75)
    letterPrint(story[locationCode]['desc'])
    time.sleep(0.75)
    # store all the possible movements, makes code a lot simpler and saves a lot of typing
    possibleMovements = [i for i in story[locationCode]['possibleMovements']]
    if len(possibleMovements) > 1:
        letterPrint(f"You can go {colour.BOLD}{f'{colour.END}, {colour.BOLD}'.join(possibleMovements[:-1])}{colour.END}, or {colour.BOLD}{possibleMovements[-1]}{colour.END}.")
    else:
        letterPrint(f"You can go {colour.BOLD}{possibleMovements[-1]}{colour.END}.")
    time.sleep(0.75)

    # ask the next direction, exiting if needed
    letterPrint('What do you do? ')
    command = input().lower()
    time.sleep(0.75)

    # perform the command and raise an InvalidCommand error if there is a mistype
    try:
        # exit the program
        if command == 'exit':
            break
        elif command == "inventory":
            if inventory != []:
                letterPrint(f"You have {', '.join(inventory)} in your inventory")
            else:
                letterPrint("You have nothing in your inventory.")
        # move the player into the required room, if they have the required item in their inventory
        elif command.split()[0] == "move":
            # ensure it is a valid movement
            if ' '.join(command.split()[1:]) in possibleMovements:
                requiredItem = story[locationCode]['possibleMovements'][' '.join(command.split()[1:])][0]
                # if there is no required item (a None object) then just move them
                if not requiredItem:
                    locationCode = story[locationCode]['possibleMovements'][' '.join(command.split()[1:])][1]
                # otherwise ensure the item is in their inventory
                else:
                    if requiredItem in inventory:
                        locationCode = story[locationCode]['possibleMovements'][' '.join(command.split()[1:])][1]
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
            letterPrint(helpMessage)
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
    print()
    time.sleep(0.5)

# save the file, if the user wishes (handled within the function)
saves.save(saveFile, inventory, locationCode)

print("Press any key to exit...", end='', flush=True)
os.system('pause >nul')
