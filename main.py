import json
import time
import functions
from exceptions import InvalidCommand

# store the story json into a dictionary
with open('story.json') as f:
    story = json.load(f)

with open('saves.json', 'r') as f:
    saves = json.load(f)

inventory, locationCode = functions.loadSaves(saves)

print('''
Possible Commands:
move <direction>
pickup <item>
exit
''')

# main game loop
while True:
    # tell the user the position and possible movements the user can make
    print(f"You are in a {story[locationCode]['location']}. {locationCode}")
    time.sleep(0.25)
    print(story[locationCode]['desc'])
    time.sleep(0.25)
    if len(story[locationCode]['possibleMovements'].keys()) > 1:
        print(f"You can go {', '.join(list(story[locationCode]['possibleMovements'].keys())[0:-1])}, or {list(story['0']['possibleMovements'].keys())[-1]}.")
    else:
        print(f"You can go {list(story[locationCode]['possibleMovements'].keys())[-1]}.")
    time.sleep(0.25)

    # ask the next direction, exiting if needed
    command = input('What do you do? ').lower()

    # perform the command and raise and InvalidCommand error if there is a mistype
    try:
        if command == 'exit':
            break
        elif command.split()[0] == "move":
            if command.split()[1] in story[locationCode]['possibleMovements']:
                locationCode = story[locationCode]['possibleMovements'][command.split()[1]]
            else:
                raise InvalidCommand
        elif command.split()[0] == "pickup":
            if command.split()[1] in story[locationCode]['availableItems']:
                inventory.append(command.split()[1])
            else:
                raise InvalidCommand
        else:
            raise InvalidCommand
    except InvalidCommand:
        print("Invalid Command!")
    except IndexError:
        print("Wrong number of inputs!")
    except Exception as e:
        print(f"Unknown error: {e}")

    # add a newline for formatting (makes the interface easier on the eyes)
    time.sleep(0.5)
    print()
    time.sleep(0.5)

# save the user's progress
saveState = True if input('Would you like to save your progress? (y/n): ') == 'y' else False
if saveState:
    saveName = input('Enter a save name: ')
    print('Please wait, saving progress...')
    with open('saves.json', 'w+') as f:
        # add the save to the saves dict
        saves[saveName] = {'location':locationCode, 'inventory':inventory}
        # save the saves dict to the saves.json file
        json.dump(saves, f)
    time.sleep(0.5)
