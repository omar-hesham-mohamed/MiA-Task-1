from Verstappen import Verstappen
from Mostafa import Mostafa

class Race:
    def __init__(self):
        self.max = Verstappen()
        self.mostafa = Mostafa()
        self.roundNo = 1
        self.maxTurn = True
        self.lastDamage = 0
    
    def start(self):

        while self.max._tireHealth > 0 and self.mostafa._tireHealth > 0:

            if self.maxTurn:
                print("It's Max's turn.")
                self.maxTurn = False
                tactic = input("Are you going to attack or defend, Max? Enter 1 for attack, 2 for defend: ")
                if tactic == '1':
                    self.max._tireHealth = self.lastDamage
                    move = input("What is your move, Max? Enter a number: ")
                    self.lastDamage = self.max.offence(int(move))
                elif tactic == '2':
                    move = input("What is your move, Max? Enter a number: ")
                    defence = self.max.defence(int(move))
                    self.max._tireHealth = (1 - defence) * self.lastDamage
                else:
                    print("Invalid input. Please enter 1 or 2.")
                    self.maxTurn = True
            else:
                print("It's Mostafa's turn.")
                self.maxTurn = True
                tactic = input("Are you going to attack or defend, Mostafa? Enter 1 for attack, 2 for defend: ")
                if tactic == '1':
                    self.mostafa._tireHealth = self.lastDamage
                    move = input("What is your move, Mostafa? Enter a number: ")
                    self.lastDamage = self.mostafa.offence(int(move))
                elif tactic == '2':
                    move = input("What is your move, Mostafa? Enter a number: ")
                    defence = self.mostafa.defence(int(move))
                    self.mostafa._tireHealth = (1 - defence) * self.lastDamage
                else:
                    print("Invalid input. Please enter 1 or 2.")
                    self.maxTurn = False

            print(f"Round {self.roundNo + 1} complete.")
            self.roundNo += 1
            print(f"Max's fuel: {self.max._fuel}, tire health: {self.max._tireHealth}")
            print(f"Mostafa's fuel: {self.mostafa._fuel}, tire health: {self.mostafa._tireHealth}")
        
        if self.max._tireHealth <= 0:
            print("Mostafa wins!")
        elif self.mostafa._tireHealth <= 0:
            print("Max wins!")

    