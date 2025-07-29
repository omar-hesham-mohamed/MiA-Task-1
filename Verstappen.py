from Racer import Racer

class Verstappen(Racer):
    def __init__(self):
        self.__fuel = 500.0
        self.__tireHealth = 100.0
        self.__defCount = 3
    
    @property
    def _fuel(self) -> int:
        return self.__fuel
    
    @property
    def _tireHealth(self) -> int:
        return self.__tireHealth
    
    @_tireHealth.setter
    def _tireHealth(self, value: int) -> None:
        self.__tireHealth = self.__tireHealth - value
    
    @property
    def _defCount(self) -> int:
        return self.__defCount
    
    def offence(self, id: int) -> int:
        if id == 1:
            if self.__fuel < 45:
                print("Not enough fuel for DRS Boost.")
                return 0
            else:
                self.__fuel -= 45
                print("DRS Boost move executed.")
                return 12
            
        if id == 2:
            if self.__fuel < 80   :
                print("Not enough fuel for Red Bull Surge.")
                return 0
            else:
                self.__fuel -= 80
                print("Red Bull Surge move executed.")
                return 20
        
        if id == 3:
            if self.__fuel < 30   :
                print("Not enough fuel for Precision Turn.")
                return 0
            else:
                self.__fuel -= 30
                print("Precision Turn move executed.")
                return 8
        
    
    def defence(self, id: int) -> int:
        if id == 1:
            if self.__fuel < 25:
                print("Not enough fuel for Brake Late.")
                return 0
            else:
                self.__fuel -= 25
                print("Brake Late move executed.")
                return 0.3
            
        if id == 2:
            if self.__fuel < 40:
                print("Not enough fuel for ERS Deployment.")
                return 0
            elif self.__defCount <= 0:
                print("No defensive moves left.")
                return 0
            else:
                self.__fuel -= 40
                self.__defCount -= 1
                print("ERS Deployment move executed.")
                return 0.5
        