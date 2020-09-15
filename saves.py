import time
import json

def load(saves):
    # select saves, looping if the user selects an invalid save, deleting if requested
    while True:
        print("Saves:")
        time.sleep(0.1)
        print('\n'.join(saves.keys()))
        time.sleep(0.1)
        save = input('Enter a save file, type "new" to create a new file, or type "del" to remove a file: ')
        print(len('Enter a save file, type "new" to create a new file, or type "del" to remove a file: ')*'=')

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

def save(saves, inventory, locationCode):
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
        # print how many save files it saved
        items = 0
        for item in saves:
            items += 1
        print(f'Saved {items} saves.')
        time.sleep(0.5)
