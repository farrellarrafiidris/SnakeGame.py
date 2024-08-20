import tkinter as tk
import random

GAME_WIDTH = 1000
GAME_HEIGHT = 600
GAME_SPEED = 100
SPACE_SIZE = 10
BODY_PART = 3
SNAKE_COLOR_1 = "#00FF00"  # Initial color for Snake 1
SNAKE_COLOR_2 = "#0000FF"  # Initial color for Snake 2
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"
FOOD_SPAWN_INTERVAL = 1000  # 1000 ms = 1 second
RESTART_DELAY = 10000  # 10000 ms = 10 seconds
COUNTDOWN_SECONDS = 10  # Countdown from 10 seconds


class Snake:
    def __init__(self, color, start_position):
        self.body_size = BODY_PART
        self.coordinates = []
        self.squares = []
        self.color = color

        for i in range(0, BODY_PART):
            self.coordinates.append(start_position)

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=self.color, tags="snake")
            self.squares.append(square)

    def move(self, x, y):
        self.coordinates.insert(0, (x, y))

        square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=self.color)
        self.squares.insert(0, square)

        del self.coordinates[-1]
        canvas.delete(self.squares[-1])
        del self.squares[-1]

    def grow(self):
        last_square = self.squares[-1]
        x1, y1, x2, y2 = canvas.coords(last_square)
        self.coordinates.append((x1, y1))
        square = canvas.create_rectangle(x1, y1, x2, y2, fill=self.color)
        self.squares.append(square)

    def change_color(self):
        new_color = random_color()
        self.color = new_color
        for square in self.squares:
            canvas.itemconfig(square, fill=new_color)


class Food:
    def __init__(self):
        x = random.randint(0, int(GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, int(GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]
        self.color = random_color()  # Assign random color initially

        self.food_id = canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=self.color, tag="food")


def random_color():
    # Generate a random color in hexadecimal format
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

score1 = 0
score2 = 0


def next_turn(snake1, snake2, foods, score1, score2):
    move_snake(snake1, direction1)
    move_snake(snake2, direction2)

    # Check if any snake eats any of the food
    for food in foods[:]:
        snake1_head = snake1.coordinates[0]
        snake2_head = snake2.coordinates[0]
        food_position = tuple(food.coordinates)  # Convert food coordinates to a tuple

        if snake1_head == food_position:
            score1 += 1
            label.config(text="Player 1 Score: {} | Player 2 Score: {}".format(score1, score2))
            canvas.delete(food.food_id)
            foods.remove(food)
            snake1.grow()
            snake1.change_color()

        if snake2_head == food_position:
            score2 += 1
            label.config(text="Player 1 Score: {} | Player 2 Score: {}".format(score1, score2))
            canvas.delete(food.food_id)
            foods.remove(food)
            snake2.grow()
            snake2.change_color()

    if check_collision(snake1) or check_collision(snake2) or check_snake_collision(snake1, snake2):
        game_over()
    else:
        window.after(GAME_SPEED, next_turn, snake1, snake2, foods, score1, score2)


def move_snake(snake, direction):
    x, y = snake.coordinates[0]

    if direction == 'up':
        y -= SPACE_SIZE
    elif direction == 'down':
        y += SPACE_SIZE
    elif direction == 'left':
        x -= SPACE_SIZE
    elif direction == 'right':
        x += SPACE_SIZE

    snake.move(x, y)


def change_direction(snake_number, new_direction):
    global direction1, direction2

    if snake_number == 1:
        if new_direction == 'left' and direction1 != 'right':
            direction1 = new_direction
        elif new_direction == 'right' and direction1 != 'left':
            direction1 = new_direction
        elif new_direction == 'up' and direction1 != 'down':
            direction1 = new_direction
        elif new_direction == 'down' and direction1 != 'up':
            direction1 = new_direction
    else:
        if new_direction == 'left' and direction2 != 'right':
            direction2 = new_direction
        elif new_direction == 'right' and direction2 != 'left':
            direction2 = new_direction
        elif new_direction == 'up' and direction2 != 'down':
            direction2 = new_direction
        elif new_direction == 'down' and direction2 != 'up':
            direction2 = new_direction


def check_collision(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False


def check_snake_collision(snake1, snake2):
    # Check if snake1 collides with snake2 or vice versa
    for body_part in snake2.coordinates:
        if snake1.coordinates[0] == body_part:
            return True
    for body_part in snake1.coordinates:
        if snake2.coordinates[0] == body_part:
            return True
    return False


def game_over():
    canvas.delete(tk.ALL)
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2,
                       font=("consolas", 70), text="GAME OVER", fill="red", tag="gameover")
    countdown(COUNTDOWN_SECONDS)  # Start the countdown


def countdown(seconds):
    if seconds > 0:
        canvas.delete("countdown")
        canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2 + 100,
                           font=("consolas", 40), text=f"Restarting in {seconds}...", fill="white", tag="countdown")
        window.after(1000, countdown, seconds - 1)
    else:
        restart_game()


def restart_game():
    global snake1, snake2, foods, score1, score2, direction1, direction2
    
    canvas.delete(tk.ALL)

    score1 = 0
    score2 = 0
    direction1 = 'down'
    direction2 = 'up'
    label.config(text="Player 1 Score: {}  |  Player 2 Score: {}".format(score1, score2))

    snake1 = Snake(SNAKE_COLOR_1, (0, 0))
    snake2 = Snake(SNAKE_COLOR_2, (GAME_WIDTH - SPACE_SIZE, GAME_HEIGHT - SPACE_SIZE))
    foods = []

    next_turn(snake1, snake2, foods, score1,score2)
    spawn_food()


def spawn_food():
    food = Food()
    foods.append(food)
    window.after(FOOD_SPAWN_INTERVAL, spawn_food)  # Schedule the next food spawn


window = tk.Tk()
window.title("Snake Game")
window.resizable(False, False)

score1 = 0
score2 = 0
direction1 = 'down'
direction2 = 'up'

label = tk.Label(window, text="Player 1 Score: {}  |  Player 2 Score: {}".format(score1, score2), font=("consolas", 40))
label.pack()

canvas = tk.Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.state('zoomed')

window.bind('<Left>', lambda event: change_direction(2, 'left'))
window.bind('<Right>', lambda event: change_direction(2, 'right'))
window.bind('<Up>', lambda event: change_direction(2, 'up'))
window.bind('<Down>', lambda event: change_direction(2, 'down'))

window.bind('<a>', lambda event: change_direction(1, 'left'))
window.bind('<d>', lambda event: change_direction(1, 'right'))
window.bind('<w>', lambda event: change_direction(1, 'up'))
window.bind('<s>', lambda event: change_direction(1, 'down'))

snake1 = Snake(SNAKE_COLOR_1, (0, 0))
snake2 = Snake(SNAKE_COLOR_2, (GAME_WIDTH - SPACE_SIZE, GAME_HEIGHT - SPACE_SIZE))
foods = []

next_turn(snake1, snake2,foods, score1,score2)
spawn_food()

window.mainloop()

# To Start type on terminal app.py
