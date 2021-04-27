from time import sleep
import sys
def gameStart():
    worldDescription = """
You move forward through the unfamiliar portal formed by two bended trees.
You're immediately met by a fascinating world.
Waterfalls pour into the lagoon you're standing in from high above.
Light from the orange sun peeks over and warms you gently.
The terrain's treacherous to walk on.
Who knows what dangers await to those who fall.
Even though this world's harsh you're at ease and you feel secure in this world.
This world is peaceful beyond a doubt, but with so much to discover you can't help but explore.
Not far into the distance you see parts of creatures of a literally and figuratively different world.
Even though they seem good natured, you try to avoid getting too close.
It's obvious there are lean creatures, feathered creatures, and what you think might be muscular creatures of some sort.
With some rationing your supplies should last for a while as discovery after discovery is waiting to be made.
But, with a great sense of adventure, a good sense of direction, and some resourcefulness, you know you can fulfill this opportunity with everything you have.

Welcome to The Secret World

"""
    for line in worldDescription:
        for c in line:
            print(c, end='')
            sys.stdout.flush()
            sleep(0)
gameStart()            
print('[1] New Game\n[2] Continue\n[3] Exit')
userInput = int(input('Select: \n> '))
if userInput == 1:
    import gamestart
elif userInput == 2:
    print('Load Game')
else:
    quit()
