#Ghost Game
from random import randint
print('Ghost ghost')
feeling_brave = True
score = 0
while feeling_brave:
    ghost_door = randint(2, 3)
    print('Three door ahead...')
    print('A ghost ib behind one.')
    print('Which door do you open?')
    door = input('1, 2 or 3?')
    door_num = int(door)
    id door_num == ghost_door
        print('GHOST')
        feeling_brave = False
    else:
        print('No ghost!')
        score = score + 1
print('Run away!')
print('Game over! you scored', score)