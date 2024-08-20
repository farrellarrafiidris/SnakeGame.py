
# SNAKE GAME🐍

The Snake game we developed is an enhanced version of the classic Snake game widely popular on Nokia mobile phones. Additional features incorporated include:

- Simultaneous multiplayer mode: Enabling two players to engage in competitive gameplay.

- Customizable snake color: Offering visual diversity and personal preference options.

- Score tracking: Allowing players to monitor their performance and strive for the highest score.
- Automated game restart: Facilitating seamless transitions to new games upon completion.

## Tech Stack ⚙️
1. Language 
**Python**

2. Library 
**Tkinter**

## Installation: 💾
### 1.Prerequisites:
- Make sure you have Python 3.x installed on your system. You can check by running python --version or python3 --version in your terminal. If not installed, download it from the official website (https://www.python.org/downloads/).

### 2.Install Required Libraries:
- Open a terminal or command prompt and navigate to your project directory (where you plan to save the game code).

- Run the following command to install tkinter:

```
Bash
pip install tkinter
```
## Running the Game: 🎮

### 1.Save the Code:
- Create a new Python file named snake_game.py (or any desired name) and paste the provided game code into it. You can find the code in the previous response or response A.

### 2.Run the Script:

- Open your terminal or command prompt and navigate to the directory where you saved `app.py`.

- Run the following command to start the game:
```
Bash
python app.py
```

## Gameplay:🕹️
1. The game window will appear with two snakes, one green (Snake 1) and one blue (Snake 2).

2. Each snake starts with a length of 3 body parts.

3. Food appears as a red circle or other color.

4. Player 1 controls their snake using the arrow keys (up, down, left, right).

5. Player 2 controls their snake using the letters w, s, a, d.

6. The snakes grow longer by eating food. Food spawns randomly on the screen.

7. Avoid collisions with the walls, your own snake's body, or the other snake's body.

8. The game ends when either snake collides with a wall or itself.

9. The snake with the longest body at the end wins!

## Tips:🗒️

- Try to strategically cut off the other snake's path to force them to collide.

- Pay close attention to your snake's direction and avoid sudden changes that might result in a collision.

- The game can be challenging at first, so practice and strategize your movements!

## Additional Notes: 🗒️

- You can customize the game settings by modifying the variables in the snake_game.py file, such as:
    
    `GAME_WIDTH`: Width of the game window

    `GAME_HEIGHT`: Height of the game window

    `SNAKE_COLOR_1` and `SNAKE_COLOR_2`: Colors of the snakes
    `FOOD_COLOR`: Color of the food

    `SPACE_SIZE`: Size of each snake body part

    `GAME_SPEED`: Speed of the game (affects how often the game updates)

- Feel free to experiment with different settings to create your own customized Snake game experience.



