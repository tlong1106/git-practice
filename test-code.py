# simple code

import time

bottlesOfBeer = 99

while bottlesOfBeer > 0:
    if bottlesOfBeer >=2:
        # assumes plural (e.g. bottles) for first verse
        print(f"{bottlesOfBeer} bottles of beer on the wall, {bottlesOfBeer} bottles of beer! Take one down, pass it around...")
        bottlesOfBeer -= 1
        # catches instance of singular (e.g. bottle) for second verse
        if bottlesOfBeer == 1:
            print(f"{bottlesOfBeer} bottle of beer on the wall!")
            print("\n")
            # pause
            time.sleep(.5)
            # starts at beginning of loop for instance of singular
            continue
        print(f"{bottlesOfBeer} bottles of beer on the wall!")
        print("\n")
        time.sleep(.5)
    # catches instance of singular (e.g. bottle) for first verse
    elif bottlesOfBeer == 1:
        print(f"{bottlesOfBeer} bottle of beer on the wall, {bottlesOfBeer} bottle of beer! Take one down, pass it around...")
        bottlesOfBeer -= 1
        # ends script with unique verse for no bottles
        print(print(f"no more bottles of beer on the wall!"))