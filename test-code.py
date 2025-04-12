# simple code

import time

bottlesOfBeer = 5

while bottlesOfBeer > 0:
    if bottlesOfBeer >=2:
        print(f"{bottlesOfBeer} bottles of beer on the wall, {bottlesOfBeer} bottles of beer! Take one down, pass it around...")
        bottlesOfBeer -= 1
        if bottlesOfBeer == 1:
            print(f"{bottlesOfBeer} bottle of beer on the wall!")
            print("\n")
            time.sleep(.5)
            continue
        print(f"{bottlesOfBeer} bottles of beer on the wall!")
        print("\n")
        time.sleep(.5)
    elif bottlesOfBeer == 1:
        print(f"{bottlesOfBeer} bottle of beer on the wall, {bottlesOfBeer} bottle of beer! Take one down, pass it around...")
        bottlesOfBeer -= 1
        print(print(f"no more bottles of beer on the wall!"))