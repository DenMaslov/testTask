class User:
    """Basic player type"""

    __name = ''
    __health = 100
    __lowHealthPoint = 35
    __is_computer = False

    def __init__(self, name: str = 'User', is_computer: bool = False):
        self.__name = name
        self.__is_computer = is_computer
 
    def add_health(self, amount: int):
        """Increase health on amount points"""
        self.__health += amount

    def subtract_health(self, amount: int):
        """Subtract health on amount points"""
        self.__health -= amount

    def is_alive(self):
        """Checks if player is alive"""
        if self.__health <= 0:
            return False
        return True

    def is_low_health(self):
        """Checks if player has low health"""
        if self.__health <= self.__lowHealthPoint:
            return True
        return False

    def name(self):
        """Return name of player"""
        return self.__name

    def health(self):
        """Return health of player"""
        return self.__health
    
    def is_computer(self):
        """Checks if player is computer"""
        return self.__is_computer
