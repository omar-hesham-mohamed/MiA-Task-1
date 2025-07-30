from Gears import Gears
import time

class Gearstick:

    def __init__(self, gear_number: Gears = Gears.GEAR_0):
        self.gear_number = gear_number
    
    def display_gear(self, gear_number):

        try:
            old_gear_number = self.gear_number
            self.gear_number = getattr(Gears, f"GEAR_{gear_number}")
        except AttributeError:
            print(f"Invalid gear number: {gear_number}")
            return

        self.animate_shift(old_gear_number.value, self.gear_number.value)
    
    def animate_shift(self, start_gear, end_gear):
        
        for line in start_gear:
            for char in line:
                print(char, end="")
            print()
        
        time.sleep(0.5)

        print("\n" * 20)

        for line in end_gear:
            for char in line:
                print(char, end="")
            print()


myGearStick = Gearstick()
myGearStick.display_gear(1)