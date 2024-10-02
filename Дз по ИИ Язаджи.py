import random

def create_grid(size):
  """Создает пустую сетку заданного размера."""
  return [[0 for _ in range(size)] for _ in range(size)]

def add_new_tile(grid):
  """Добавляет новую плитку со значением 2 или 4 в пустую ячейку."""
  empty_cells = [(i, j) for i in range(len(grid)) for j in range(len(grid)) if grid[i][j] == 0]
  if empty_cells:
    i, j = random.choice(empty_cells)
    grid[i][j] = random.choice([2, 4])

def move_tiles(grid, direction):
  """Перемещает плитки в указанном направлении."""
  if direction == "up":
    for j in range(len(grid)):
      for i in range(1, len(grid)):
        if grid[i][j] != 0:
          k = i
          while k > 0 and grid[k - 1][j] == 0:
            grid[k - 1][j] = grid[k][j]
            grid[k][j] = 0
            k -= 1
  elif direction == "down":
    for j in range(len(grid)):
      for i in range(len(grid) - 2, -1, -1):
        if grid[i][j] != 0:
          k = i
          while k < len(grid) - 1 and grid[k + 1][j] == 0:
            grid[k + 1][j] = grid[k][j]
            grid[k][j] = 0
            k += 1
  elif direction == "left":
    for i in range(len(grid)):
      for j in range(1, len(grid)):
        if grid[i][j] != 0:
          k = j
          while k > 0 and grid[i][k - 1] == 0:
            grid[i][k - 1] = grid[i][k]
            grid[i][k] = 0
            k -= 1
  elif direction == "right":
    for i in range(len(grid)):
      for j in range(len(grid) - 2, -1, -1):
        if grid[i][j] != 0:
          k = j
          while k < len(grid) - 1 and grid[i][k + 1] == 0:
            grid[i][k + 1] = grid[i][k]
            grid[i][k] = 0
            k += 1

def merge_tiles(grid, direction):
  """Сливает плитки одинакового значения в указанном направлении."""
  if direction == "up":
    for j in range(len(grid)):
      for i in range(1, len(grid)):
        if grid[i][j] != 0 and grid[i - 1][j] == grid[i][j]:
          grid[i - 1][j] *= 2
          grid[i][j] = 0
  elif direction == "down":
    for j in range(len(grid)):
      for i in range(len(grid) - 2, -1, -1):
        if grid[i][j] != 0 and grid[i + 1][j] == grid[i][j]:
          grid[i + 1][j] *= 2
          grid[i][j] = 0
  elif direction == "left":
    for i in range(len(grid)):
      for j in range(1, len(grid)):
        if grid[i][j] != 0 and grid[i][j - 1] == grid[i][j]:
          grid[i][j - 1] *= 2
          grid[i][j] = 0
  elif direction == "right":
    for i in range(len(grid)):
      for j in range(len(grid) - 2, -1, -1):
        if grid[i][j] != 0 and grid[i][j + 1] == grid[i][j]:
          grid[i][j + 1] *= 2
          grid[i][j] = 0

def is_game_over(grid):
  """Проверяет, закончилась ли игра."""
  # Проверяем, есть ли пустые ячейки
  if any(0 in row for row in grid):
    return False

  # Проверяем, можно ли слить плитки
  for i in range(len(grid)):
    for j in range(len(grid)):
      if i > 0 and grid[i][j] == grid[i - 1][j]:
        return False
      if i < len(grid) - 1 and grid[i][j] == grid[i + 1][j]:
        return False
      if j > 0 and grid[i][j] == grid[i][j - 1]:
        return False
      if j < len(grid) - 1 and grid[i][j] == grid[i][j + 1]:
        return False

  return True

def print_grid(grid):
  """Печатает сетку."""
  for row in grid:
    print(row)

def play_game():
  """Запускает игру 2048."""
  grid_size = 4
  grid = create_grid(grid_size)
  add_new_tile(grid)
  add_new_tile(grid)

  while True:
    print_grid(grid)
    direction = input("Введите направление (up, down, left, right) или q для выхода: ")

    if direction == "q":
      break

    if direction in ("up", "down", "left", "right"):
      move_tiles(grid, direction)
      merge_tiles(grid, direction)
      move_tiles(grid, direction)
      add_new_tile(grid)

      if is_game_over(grid):
        print_grid(grid)
        print("Игра окончена!")
        break

if __name__ == "__main__":
  play_game()