from Verstappen import Verstappen
from Mostafa import Mostafa

class RaceText:
    def __init__(self):
        self.max = Verstappen()
        self.mostafa = Mostafa()
        self.roundNo = 0
        self.maxTurn = True
        self.lastDamage = 0
    
    def start(self):

        while self.max._tireHealth > 0 and self.mostafa._tireHealth > 0:

            if self.maxTurn:
                print("It's Max's turn.")
                tactic = input("Are you going to attack or defend, Max? Enter 1 for attack, 2 for defend: ")
                if tactic == '1':
                    self.max._tireHealth = self.lastDamage
                    move = int(input("What is your move, max? Enter a number: "))
                    while move < 1 or move > 3:
                        move = int(input("Enter a number (1-3): "))
                    move = input("What is your move, Max? Enter a number: ")
                    self.lastDamage = self.max.offence(int(move))
                    self.maxTurn = False
                elif tactic == '2':
                    move = int(input("What is your move, Max? Enter a number: "))
                    while move < 1 or move > 2:
                        move = int(input("Enter a number (1-2): "))
                    defence = self.max.defence(int(move))
                    self.max._tireHealth = (1 - defence) * self.lastDamage
                    self.maxTurn = False
                else:
                    print("Invalid input. Please enter 1 or 2.")
                    continue
            else:
                print("It's Mostafa's turn.")
                tactic = input("Are you going to attack or defend, Mostafa? Enter 1 for attack, 2 for defend: ")
                if tactic == '1':
                    self.mostafa._tireHealth = self.lastDamage
                    move = int(input("What is your move, Mostafa? Enter a number: "))
                    while move < 1 or move > 3:
                        move = int(input("Enter a number (1-3): "))
                    move = input("What is your move, Mostafa? Enter a number: ")
                    self.lastDamage = self.mostafa.offence(int(move))
                    self.maxTurn = True
                elif tactic == '2':
                    move = int(input("What is your move, Mostafa? Enter a number: "))
                    while move < 1 or move > 2:
                        move = int(input("Enter a number (1-2): "))
                    defence = self.mostafa.defence(int(move))
                    self.mostafa._tireHealth = (1 - defence) * self.lastDamage
                    self.maxTurn = True
                else:
                    print("Invalid input. Please enter 1 or 2.")
                    continue

            print(f"Round {self.roundNo + 1} complete.")
            self.roundNo += 1
            print(f"Max's fuel: {self.max._fuel}, tire health: {self.max._tireHealth}")
            print(f"Mostafa's fuel: {self.mostafa._fuel}, tire health: {self.mostafa._tireHealth}")
        
        if self.max._tireHealth <= 0:
            print("Mostafa wins!")
        elif self.mostafa._tireHealth <= 0:
            print("Max wins!")


myRace = Race()
myRace.start()    