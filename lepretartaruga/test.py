import random
import time


turtle_pos : int = 1
hare_pos : int = 1
track = []

print("BANG  !!!!!!     AND THEY'RE OFF !!!!!!")

for i in range(1, 70):
    track.append('_')

def posizioni(turtle_pos, hare_pos, track):
    if turtle_pos == hare_pos:
        track[turtle_pos] = "OUCH!!!"
        print(*track)
        track[turtle_pos] = '_'
    else:
        track[turtle_pos] = 'T'
        track[hare_pos] = 'H'
        print(*track)
        track[turtle_pos] = '_'
        track[hare_pos] = '_'

def move_turle(turtle_pos):
        movement = random.randint(1, 10)
        if movement <= 5:
            turtle_pos += 3
        elif movement == 6 or movement == 7:
            turtle_pos -= 6
            if turtle_pos < 1:
                turtle_pos = 1
        elif movement >= 8:
            turtle_pos += 1
        return turtle_pos


def move_hare(hare_pos):
        movement = random.randint(1, 10)
        if movement <= 2:
            hare_pos += 0
        elif movement == 3 or movement == 4:
            hare_pos += 9
        elif movement == 5:
            hare_pos -= 12
            if hare_pos < 1:
                hare_pos = 1
        elif movement >= 6 and movement <= 8:
            hare_pos += 1
        elif movement == 9 or movement == 10:
            hare_pos -= 2
            if hare_pos < 1:
                hare_pos = 1
        return hare_pos

while turtle_pos < 70 and hare_pos < 70:
        turtle_pos = move_turle(turtle_pos)
        hare_pos = move_hare(hare_pos)
        posizioni(turtle_pos, hare_pos, track)
        time.sleep(1)

if turtle_pos >= 70 and hare_pos >= 70:
    print("It's a tie!")
elif turtle_pos >= 70:
    print("Turtle wins. Yay!")
elif hare_pos >= 70:
    print("Hare wins. Yuch.")