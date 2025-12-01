from dataclasses import dataclass
import random

@dataclass
class Vec2D:
    x: int
    y: int

@dataclass
class Item:
    position: Vec2D
    energy: int

@dataclass
class Snake:
    positions: list[Vec2D]
    direction: Vec2D
    alive: bool
    grow: int

@dataclass
class Game:
    snake: Snake
    width: int
    height: int
    frame: int
    items: list[Item]

def add_vecs(a: Vec2D, b: Vec2D) -> Vec2D:
    return Vec2D(a.x + b.x, a.y + b.y)

def turn_direction(direction: Vec2D, turn: int) -> Vec2D:
    # turn: -1 = left, 1 = right, else = straight
    # turning right: right (1,0) -> down (0,1) -> left (-1,0) -> up (0,-1)
    # turning left: right (1,0) -> up (0,-1) -> left (-1,0) -> down (0,1)

    if turn == 1:  # turning right
        if direction.x == 1 and direction.y == 0:
            direction = Vec2D(0, 1)
        elif direction.x == 0 and direction.y == 1:
            direction = Vec2D(-1, 0)
        elif direction.x == -1 and direction.y == 0:
            direction = Vec2D(0, -1)
        elif direction.x == 0 and direction.y == -1:
            direction = Vec2D(1, 0)
    elif turn == -1:  # turning left
        if direction.x == 1 and direction.y == 0:
            direction = Vec2D(0, -1)
        elif direction.x == 0 and direction.y == -1:
            direction = Vec2D(-1, 0)
        elif direction.x == -1 and direction.y == 0:
            direction = Vec2D(0, 1)
        elif direction.x == 0 and direction.y == 1:
            direction = Vec2D(1, 0)
    return direction

def turn_snake(snake: Snake, turn: int) -> Snake:
    if not snake.alive:
        return snake
    new_direction = turn_direction(snake.direction, turn)
    return Snake(snake.positions, new_direction, snake.alive, snake.grow)

def grow_positions(positions: list[Vec2D], direction: Vec2D) -> list[Vec2D]:
    new_head = add_vecs(positions[0], direction)
    return [new_head] + positions

def move_snake(snake: Snake) -> Snake:
    if not snake.alive:
        return snake
    new_positions = grow_positions(snake.positions, snake.direction)
    if snake.grow > 0:
        return Snake(new_positions, snake.direction, snake.alive, snake.grow - 1)
    else:
        return Snake(new_positions[:-1], snake.direction, snake.alive, snake.grow)

def collision(snake: Snake, width: int, height: int) -> bool:
    head = snake.positions[0]
    # Check wall collision
    if head.x < 0 or head.x >= width or head.y < 0 or head.y >= height:
        return True
    # Check self collision
    if head in snake.positions[1:]:
        return True
    return False

def generate_item(game: Game) -> Item:

    while True:
        position = Vec2D(random.randint(0, game.width - 1), random.randint(0, game.height - 1))
        # item should not spawn on the snake
        if position not in game.snake.positions:
            energy = random.randint(1,5)
            return Item(position, energy)

def pick_item(items: list[Item], position: Vec2D) -> tuple[list[Item], int]:
    new_items = []
    total_energy = 0
    for item in items:
        if item.position == position:
            total_energy += item.energy
        else:
            new_items.append(item)
    return new_items, total_energy