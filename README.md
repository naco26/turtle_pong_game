# turtle_pong_game

Pong game is a classic 2-player game where each player have a paddle and their objective is to not let the ball pass through their paddle. They score a point if other player 
let the ball pass through their paddle.

## Files Explanation
It uses turtle library of pyhton.

### main.py 
Main File of the project where paddle logic, ball logic, scoreboard logic is called and screen structure is maintained.

### pong.py
It creates paddles, sets it to appropriate position and movement (up & down) for each paddle

### ball.py
It creates ball, moves ball , bounces ball from ceil and floor and bounces back from paddle (if paddle hits it). If player let it pass, it also refreshes i.e set it to 
initital position

### scoreboard.py
It mainitains the score of both the players and also display it to the user in real time.

It's play time!!

