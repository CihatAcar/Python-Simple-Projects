from ipy_lib import SnakeUserInterface

WIDTH = 32
HEIGHT = 24
SCALE = 0.50
FRAMES_PER_SECOND = 10.0
FOOD = 1


class Snake:
    def __init__(self):
        self.body = [[0, 0], [1, 0]]
        self.coordinate = 0
        self.add = 0
        self.arrow_pressed = False

    def select_direction(self, direction):
        self.arrow_pressed = True

        if direction == "r":
            snake.coordinate = 0
            snake.add = 1

        elif direction == "l":
            snake.coordinate = 0
            snake.add = -1

        elif direction == "d":
            snake.coordinate = 1
            snake.add = 1

        elif direction == "u":
            snake.coordinate = 1
            snake.add = -1

    def eat_food(self):
        if self.body[len(self.body) - 1] == food.coordinates:
            food.coordinates[0] = ui.random(WIDTH - 1)
            food.coordinates[1] = ui.random(HEIGHT - 1)

            food.score += 1
            return True

        return False

    def dead(self):
        snake_length = len(snake.body)
        head = snake.body[snake_length - 1]
        for i in range(0, snake_length - 1):
            if snake.body[i] == head:
                return True

        return False


class Food:
    def __init__(self):
        self.coordinates = [2, 3]
        self.score = 0


ui = SnakeUserInterface(WIDTH, HEIGHT, SCALE)  # Create GUI
x, y = 0, 0

snake = Snake()
food = Food()


def process_other(event_data):
    print(event_data)


def process_arrow(event_data):
    snake.select_direction(event_data)
    print(event_data)


ui.set_animation_speed(FRAMES_PER_SECOND)


def emerge_snake():  # When the snake reaches the end of the screen, it will re-emerge at the other end.
    snake_length = len(snake.body) - 1
    if snake.body[snake_length][0] == -1:
        snake.body[snake_length][0] = WIDTH - 1

    elif snake.body[snake_length][0] == WIDTH:
        snake.body[snake_length][0] = 0

    elif snake.body[snake_length][1] == -1:
        snake.body[snake_length][1] = HEIGHT - 1

    elif snake.body[snake_length][1] == HEIGHT:
        snake.body[snake_length][1] = 0


def move_snake(head):
    if snake.arrow_pressed:
        head[snake.coordinate] += snake.add
    else:
        head[0] += 1

    snake.body.append(head)
    del snake.body[0]


def snake_game():
    if snake.eat_food():  # If food eaten, then increment the size of snake
        snake.body.insert(0, snake.body[0])
        ui.place(snake.body[0][0], snake.body[0][1], ui.SNAKE)
        ui.wait(30)

    ui.place(food.coordinates[0], food.coordinates[1], ui.FOOD)

    snake_length = len(snake.body)

    if snake.dead():
        print("Game over!")
        ui.close()

    for i in range(0, snake_length):
        ui.place(snake.body[i][0], snake.body[i][1], ui.SNAKE)

    head = list(snake.body[snake_length - 1])
    move_snake(head)
    emerge_snake()

    print(snake.body)
    ui.show()


def process_animation(event_data):  # process_animation function keeps refreshing...
    snake_game()


def process_event(event):
    if event.name == "other":
        process_other(event.data)

    elif event.name == "arrow":
        process_arrow(event.data)

    elif event.name == "alarm":
        ui.clear()
        process_animation(event.data)


while True:
    event = ui.get_event()
    process_event(event)