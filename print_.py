import time
import random

def letterPrint(text, _end='\n'):
    for c in text:
        print(c, end='', flush=True)
        timeToWait = random.randint(1000,6000) / 50000
        time.sleep(timeToWait)
    print(_end, end='')

if __name__ == '__main__':
    letterPrint('''im literally shaking and crying rn how cuold you angle do you have any idea how much that hurts me dude honestly im so sad rn and you just had to push me over the edge thats it im literally ending it all how could you think that this is okay jesus christ dude think before you act, now look what you've done you've made a kid kill herself do you know how much of a bad person that makes you honestly please i hope that you never feel happy again you absolutely sickening person how did you ever get mod on any server let alone multiple i can't believe you've done this to me. you're the most mean and disrespectful person i've ever met and the fact that you exist hurts me on a personal level. i hope when you die you go to the deepest pit of hell where satan will rape you for all of eternity. i am truly sickened by your attitude and seemingly complete lack of empathy or thought for the impact of your words. my disappointment is immeasurable, and my day is ruined. i'm literally goinhg to leave this server now, and hope to never see you again in my life. you better pray to whatever insignificant god you believe in that we never meet in real life because i will literally snap you like a fucking glowstick and shit on your corpse. i will never trust anyone for the rest of my life thanks to you like honestly please think before you say something so hurtful and sickening. i hope that no one ever has to suffer the pain that you've put me through because i wouldn't wish it on anyone, except maybe for you.''')
