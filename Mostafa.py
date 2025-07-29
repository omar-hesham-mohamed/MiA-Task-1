from Racer import Racer

class Mostafa(Racer):
    def __init__(self):
        self.__fuel = 500.0
        self.__tireHealth = 100.0
        self.__defCount = 2
    
    @property
    def _fuel(self) -> float:
        return self.__fuel
    
    @property
    def _tireHealth(self) -> float:
        return self.__tireHealth
    
    @_tireHealth.setter
    def _tireHealth(self, value: int) -> None:
        self.__tireHealth = self.__tireHealth - value
    
    @property
    def _defCount(self) -> int:
        return self.__defCount

    def offence(self, id: int) -> int:
        if id == 1:
            if self.__fuel < 50:
                print("Not enough fuel for Turbo Start.")
                return 0
            else:
                self.__fuel -= 50
                print("Turbo Start move executed.")
                return 10
            
        if id == 2:
            if self.__fuel < 90   :
                print("Not enough fuel for Mercedes Charge.")
                return 0
            else:
                self.__fuel -= 90
                print("Mercedes Charge move executed.")
                return 22
        
        if id == 3:
            if self.__fuel < 25   :
                print("Not enough fuel for Corner Mastery.")
                return 0
            else:
                self.__fuel -= 25
                print("Corner Mastery move executed.")
                return 7
        
    
    def defence(self, id: int) -> int:
        if id == 1:
            if self.__fuel < 20:
                print("Not enough fuel for Slipstream Cut.")
                return 0
            else:
                self.__fuel -= 20
                print("Slipstream Cut move executed.")
                return 0.4
            
        if id == 2:
            if self.__fuel < 35:
                print("Not enough fuel for Aggresive Block.")
                return 0
            elif self.__defCount <= 0:
                print("No defensive moves left.")
                return 0
            else:
                self.__fuel -= 35
                self.__defCount -= 1
                print("Aggresive Block move executed.")
                return 1
        