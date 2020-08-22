import time
import json

def loadSaves(saves):
    # select saves, looping if the user selects an invalid save, deleting if requested
    while True:
        print("Saves:")
        time.sleep(0.1)
        print('\n'.join(saves.keys()))
        time.sleep(0.1)
        save = input('Select a save file, type "new" to create a new file, or type "del" to remove a file: ')
        print(len('Select a save file, type "new" to create a new file, or type "del" to remove a file: ')*'=')

        time.sleep(0.1)
        # create a new game
        if save == 'new':
            inventory = []
            locationCode = '0'
            break
        # delete a save
        elif save == 'del':
            saveToRemove = input('What save would you like to delete? ')
            correctSave = True if input(f"You selected {saveToRemove} to delete. Is this correct? (y/n) ") == 'y' else False
            if correctSave:
                try:
                    # delete the save from saves.json
                    del saves[saveToRemove]
                    with open('saves.json', 'w+') as f:
                        json.dump(saves, f)
                except:
                    print('Incorrect save name.')
                    continue
            else:
                continue
        elif save not in saves:
            print('Invalid save')
            continue
        else:
            inventory = saves[save]['inventory']
            locationCode = saves[save]['location']
            break
    return inventory, locationCode
