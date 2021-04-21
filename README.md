# Test task "Simulation of the game"


### INSTALLATION:
1. git clone https://github.com/DenMaslov/testTask.git
2. cd ./testTask
3. python main.py

### TESTED WITH:
* Windows 10
* python 3.9

### DESCRIPTION:
* Project contains two classes: User and GameManager.
  * Class User provides fields, which regard to basic functionality of player's instance: starting health, current health, type: User or Computer,  name, point of low health and different functions for interaction.
  * Class GameManager provides two public functions: add_player and start. Function add_player adds player to protected list of players. Function "start" begins main loop of the game. But before running "start", list of players should consist of **TWO** or more players.
  * module "manager" except class, also contains decorator for function "start"
  * style: **PEP8** and **PEP257**

### FUNCTIONALITY:
* move - is equal to 1 iteration of game loop.
* Current user - is a user who is making an action during this move.
* Action - could be Medium range damage, Max range damage, or Treatment. Each actions is applied towards **INACTIVE PLAYER** (even treatment, not towards current user).
* TREATMENT - for users the chance is **33.3%**, but if inactive player is **Computer** and it has **low** health (less **35%**) chance is enhanced to around **70%**.
* Information about: health of players before manipulation, whose turn if, if chance of treatment for computer is enhanced, chosen action and points and result health of players - **is printed each iteration**.
* If health of any player is lower or equal 0. The game is stopped and prints the name of winner.
* Random choice of turn of players.
* Random choice of action.
* Random choice of points in specific range.

#### Screenshot

![image](https://user-images.githubusercontent.com/76794599/115594604-991a2900-a2de-11eb-8af7-defb94873a74.png)



