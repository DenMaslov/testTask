import random
import os
import time
from user import User


def start_game(func):
    """Decorator of start func, provides countdown"""
    def inner(*args, **kwargs):
        os.system('cls||clear')
        for i in range(3, 0, -1):
            print(f'Game will start in {i} ...')
            time.sleep(1)
            os.system('cls||clear')
        print('Starting... \n' + '-' * 50)
        func(*args, **kwargs)
    return inner


class GameManager():
    """Main class of game loop.

    Contains game loop. Game is starting with running func start(),
    before start, you should add at least two Player's objects by using
    func: addPlayer() and pass object of Player as parameter and only then
    call start func

    """

    _players = []
    _activePlayer = None
    _currentAction = None
    _points = 0
    _isBiggerCureChance = False

    _ACTIONS = ['MEDIUM_DAMAGE', 'MAX_DAMAGE', 'TREATMENT']
    _RANGES = {'MEDIUM_RANGE': [18, 25], 'MAX_RANGE': [10, 35]}

    def add_player(self, player: User):
        """Add player to list of players"""
        if isinstance(player, User):
            self._players.append(player)
        else:
            print(f'{player} is not User-type')

    @start_game
    def start(self):
        """Main loop of game"""
        if len(self._players) >= 2:
            while self._is_all_players_alive():
                self._set_active_player()
                self._show_health()
                self._set_current_action()
                self._make_actions()
                self._log()
            self._show_winner()
        else:
            print("There are not enough players! Should be at least 2!")

    def _is_all_players_alive(self):
        """Checks if there is a dead player"""
        for player in self._players:
            if not player.is_alive():
                return False
        return True

    def _set_active_player(self):
        """Random choice of player who will make action"""
        self._activePlayer = random.choice(self._players)

    def _set_current_action(self):
        """Set action with higher chance of selecting treatment or not"""
        if self._is_low_health():
            self._set_with_higher_treatment()
        else:
            self._set_with_usual_treatment()

    def _set_with_higher_treatment(self):
        """Set action with chance of selecting treatment 71.42%"""
        actionIndex = random.randint(0, (len(self._ACTIONS) + 3))
        if actionIndex >= len(self._ACTIONS):
            actionIndex = 2
        self._currentAction = self._ACTIONS[actionIndex]

    def _set_with_usual_treatment(self):
        """Set action with chance of selecting treatment 33.3%"""
        self._currentAction = random.choice(self._ACTIONS)
        self._isBiggerCureChance = False

    def _is_low_health(self):
        """Checks if there is an inactive computer-player with low health"""
        for player in self._players:
            if player != self._activePlayer and player.is_computer():
                self._isBiggerCureChance = player.is_low_health()
                return self._isBiggerCureChance

    def _apply_action(self, player: User):
        """Apply current action to specific user"""
        if self._currentAction == self._ACTIONS[0]:
            ranges = self._RANGES['MEDIUM_RANGE']
            self._points = random.randint(ranges[0], ranges[1])
            player.subtract_health(self._points)
        elif self._currentAction == self._ACTIONS[1]:
            ranges = self._RANGES['MAX_RANGE']
            self._points = random.randint(ranges[0], ranges[1])
            player.subtract_health(self._points)
        elif self._currentAction == self._ACTIONS[2]:
            ranges = self._RANGES['MEDIUM_RANGE']
            self._points = random.randint(ranges[0], ranges[1])
            player.add_health(self._points)

    def _make_actions(self):
        """Apply current action to all inactive user"""
        for player in self._players:
            if player != self._activePlayer:
                self._apply_action(player)

    def _log(self):
        """Prints main information about current move"""
        print(f'It\'s  {self._activePlayer.name()}\'s turn ... ')
        print(f'Bigger chance of treatment: {self._isBiggerCureChance}')
        print(f'Chosen action: {self._currentAction} with {self._points} points')
        print('Result health points - ', end=' ')
        self._show_health()
        print("-" * 50)

    def _show_winner(self):
        """Prints name of winner"""
        for player in self._players:
            if player.is_alive():
                print('=' * 50)
                print(f'Player {player.name()} won!')
                print('=' * 50)

    def _show_health(self):
        """Prints current health points of players"""
        for player in self._players:
            print(player.name() + ": " + str(player.health()), end=' ')
        print()
