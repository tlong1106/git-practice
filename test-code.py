# simple code

import time

bottlesOfBeer = 99

while bottlesOfBeer > 0:
    print(f"{bottlesOfBeer} bottles of beer on the wall, {bottlesOfBeer} bottles of beer! Take one down, pass it around...")
    bottlesOfBeer -= 1
    print(f"{bottlesOfBeer} bottles of beer on the wall!")
    print("\n")
    time.sleep(.5)