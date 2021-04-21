from user import User
from manager import GameManager


def main():
    user = User("User1")
    computer = User("Computer", is_computer=True)
    game = GameManager()
    game.add_player(user)
    game.add_player(computer)
    game.start()
    
if __name__ == "__main__":
    main()
   
