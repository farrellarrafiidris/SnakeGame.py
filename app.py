import tkinter as tk
import random

GAME_WIDTH = 500
GAME_HEIGHT = 500
GAME_SPEED = 100
SPACE_SIZE = 50
BODY_PART = 3
SNAKE_COLOR = "#00FF00"  # Initial color
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"


class Snake:
    def __init__(self):
        self.body_size = BODY_PART
        self.coordinates = []
        self.squares = []
        self.color = SNAKE_COLOR  # Initial color of the snake

        for i in range(0, BODY_PART):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=self.color, tags="snake")
            self.squares.append(square)

    def change_color(self):
        # Method to change the snake's color
        new_color = random_color()
        self.color = new_color
        for square in self.squares:
            canvas.itemconfig(square, fill=new_color)


class Food:
    def __init__(self):
        x = random.randint(0, int(GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, int(GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")


def random_color():
    # Generate a random color in hexadecimal format
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))


def next_turn(snake, food):
    x, y = snake.coordinates[0]

    if direction == 'up':
        y -= SPACE_SIZE
    elif direction == 'down':
        y += SPACE_SIZE
    elif direction == 'left':
        x -= SPACE_SIZE
    elif direction == 'right':
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=snake.color)
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1

        label.config(text="Score:{}".format(score))

        canvas.delete(f"food")

        food = Food()
        snake.change_color()  # Change the snake's color when it eats food

    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collision(snake):
        game_over()
    else:
        window.after(GAME_SPEED, next_turn, snake, food)


def change_direction(new_direction):
    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction

    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction

    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction

    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction


def check_collision(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        return True

    elif y < 0 or y >= GAME_HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False


def game_over():
    canvas.delete(tk.ALL)
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2,
                       font=("consolas", 70), text="GAME OVER", fill="red", tag="gameover")
    countdown(10)


def countdown(seconds):
    if seconds > 0:
        canvas.delete("countdown")
        canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2 + 70,
                           font=("consolas", 50), text=str(seconds), fill="white", tag="countdown")
        window.after(1000, countdown, seconds - 1)
    else:
        restart_game()


def restart_game():
    global snake, food, score, direction

    canvas.delete(tk.ALL)

    score = 0
    direction = 'down'
    label.config(text="Score:{}".format(score))

    snake = Snake()
    food = Food()

    next_turn(snake, food)


window = tk.Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = 'down'

label = tk.Label(window, text="Score:{}".format(score), font=("consolas", 40))
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

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()
