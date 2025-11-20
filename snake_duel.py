import random
import time

DIRS = {
    "UP": (-1, 0),
    "DOWN": (1, 0),
    "LEFT": (0, -1),
    "RIGHT": (0, 1),
}
ALL_DIRS = ["UP", "DOWN", "LEFT", "RIGHT"]

def in_bounds(r, c):
    return 0 <= r < 10 and 0 <= c < 10

def print_grid(grid):
    for row in grid:
        print(" ".join(row))
    print()

def safe_moves(snake, opponent):
    head = snake[0]
    moves = []

    for d in ALL_DIRS:
        dr, dc = DIRS[d]
        nr, nc = head[0] + dr, head[1] + dc

        if not in_bounds(nr, nc):
            continue
        if (nr, nc) in snake[:-1]:
            continue
        if (nr, nc) in opponent:
            continue

        moves.append((nr, nc, d))

    return moves


def best_move(snake, opponent, food):
    moves = safe_moves(snake, opponent)

    if not moves:
        return None  # no move → snake dies

    moves.sort(key=lambda x: abs(x[0] - food[0]) + abs(x[1] - food[1]))
    return moves[0]


def smart_snake_duel():

    grid = [["." for _ in range(10)] for _ in range(10)]

    snakeA = [(2, 2)]
    snakeB = [(7, 7)]

    scoreA = 0
    scoreB = 0

    def spawn_food():
        while True:
            r = random.randint(0, 9)
            c = random.randint(0, 9)
            if (r, c) not in snakeA and (r, c) not in snakeB:
                return (r, c)

    food = spawn_food()
    step = 1

    print("\n--- SMART SNAKE DUEL (WINNER GUARANTEED) ---\n")

    while True:
        print(f"STEP {step}")

        grid = [["." for _ in range(10)] for _ in range(10)]
        grid[food[0]][food[1]] = "F"

        moveA = best_move(snakeA, snakeB, food)
        moveB = best_move(snakeB, snakeA, food)

        # ----- GUARANTEED WINNER LOGIC -----

        # BOTH cannot move → use scores to decide winner
        if moveA is None and moveB is None:
            if scoreA > scoreB:
                print("Snake A wins (higher score)!")
                break
            elif scoreB > scoreA:
                print("Snake B wins (higher score)!")
                break
            else:
                print("Both blocked! Random winner selected!")
                winner = random.choice(["A", "B"])
                print("Winner:", winner)
                break

        # Only A cannot move → B wins
        if moveA is None:
            print("Snake A is trapped → Snake B Wins 🏆")
            scoreB += 1
            break

        # Only B cannot move → A wins
        if moveB is None:
            print("Snake B is trapped → Snake A Wins 🏆")
            scoreA += 1
            break

        # Head-on collision → winner decided by score
        newA = (moveA[0], moveA[1])
        newB = (moveB[0], moveB[1])

        if newA == newB:
            if scoreA > scoreB:
                print("Head-on collision → Snake A survives!")
                break
            elif scoreB > scoreA:
                print("Head-on collision → Snake B survives!")
                break
            else:
                print("Head-on collision → Random winner!")
                winner = random.choice(["A", "B"])
                print("Winner:", winner)
                break

        # Update Snake A
        snakeA.insert(0, newA)
        if newA == food:
            scoreA += 1
            food = spawn_food()
        else:
            snakeA.pop()

        # Update Snake B
        snakeB.insert(0, newB)
        if newB == food:
            scoreB += 1
            food = spawn_food()
        else:
            snakeB.pop()

        # Draw snakes
        for (r, c) in snakeA:
            grid[r][c] = "A"
        for (r, c) in snakeB:
            if grid[r][c] == "A":
                grid[r][c] = "AB"
            else:
                grid[r][c] = "B"

        print_grid(grid)
        print(f"Score A: {scoreA} | Score B: {scoreB}")
        print("----------------------------------\n")

        step += 1
        time.sleep(0.4)

        if step > 100:
            print("Max steps reached → winner by score!")
            break

    print("\n--- FINAL SCORES ---")
    print("Snake A:", scoreA)
    print("Snake B:", scoreB)

    if scoreA > scoreB:
        print("Winner: Snake A 🏆")
    elif scoreB > scoreA:
        print("Winner: Snake B 🏆")
    else:
        print("Final Result: DRAW 🤝")


smart_snake_duel()















# import pygame
# import random
# import sys

# DIRS = {
#     "UP": (-1, 0),
#     "DOWN": (1, 0),
#     "LEFT": (0, -1),
#     "RIGHT": (0, 1),
# }
# ALL_DIRS = ["UP", "DOWN", "LEFT", "RIGHT"]

# def in_bounds(r, c):
#     return 0 <= r < 10 and 0 <= c < 10

# def safe_moves(snake, opponent):
#     head = snake[0]
#     moves = []

#     for d in ALL_DIRS:
#         dr, dc = DIRS[d]
#         nr, nc = head[0] + dr, head[1] + dc

#         if not in_bounds(nr, nc):
#             continue
#         if (nr, nc) in snake[:-1]:
#             continue
#         if (nr, nc) in opponent:
#             continue

#         moves.append((nr, nc, d))

#     return moves

# def best_move(snake, opponent, food):
#     moves = safe_moves(snake, opponent)

#     if not moves:
#         return None

#     moves.sort(key=lambda x: abs(x[0] - food[0]) + abs(x[1] - food[1]))
#     return moves[0]

# def smart_snake_duel_pygame():

#     pygame.init()
#     CELL = 60
#     screen = pygame.display.set_mode((10 * CELL, 10 * CELL))
#     pygame.display.set_caption("Smart Snake Duel - EXACT LOGIC (Pygame)")

#     clock = pygame.time.Clock()

#     snakeA = [(2, 2)]
#     snakeB = [(7, 7)]
#     scoreA = 0
#     scoreB = 0

#     def spawn_food():
#         while True:
#             r = random.randint(0, 9)
#             c = random.randint(0, 9)
#             if (r, c) not in snakeA and (r, c) not in snakeB:
#                 return (r, c)

#     food = spawn_food()
#     step = 1

#     while True:

#         # Quit event
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()

#         moveA = best_move(snakeA, snakeB, food)
#         moveB = best_move(snakeB, snakeA, food)

#         # EXACT SAME WINNER LOGIC
#         if moveA is None and moveB is None:
#             if scoreA > scoreB:
#                 print("Snake A wins (higher score)!")
#             elif scoreB > scoreA:
#                 print("Snake B wins (higher score)!")
#             else:
#                 print("Both blocked! Random winner!")
#                 print("Winner:", random.choice(["A", "B"]))
#             break

#         if moveA is None:
#             print("Snake A trapped → Snake B Wins")
#             break

#         if moveB is None:
#             print("Snake B trapped → Snake A Wins")
#             break

#         newA = (moveA[0], moveA[1])
#         newB = (moveB[0], moveB[1])

#         if newA == newB:
#             if scoreA > scoreB:
#                 print("Head-on: Snake A survives!")
#             elif scoreB > scoreA:
#                 print("Head-on: Snake B survives!")
#             else:
#                 print("Head-on: Random winner:", random.choice(["A", "B"]))
#             break

#         # UPDATE A (same as your code)
#         snakeA.insert(0, newA)
#         if newA == food:
#             scoreA += 1
#             food = spawn_food()
#         else:
#             snakeA.pop()

#         # UPDATE B (same as your code)
#         snakeB.insert(0, newB)
#         if newB == food:
#             scoreB += 1
#             food = spawn_food()
#         else:
#             snakeB.pop()

#         # -------------------------
#         # PYGAME DRAW (REPLACES print_grid)
#         screen.fill((0, 0, 0))

#         # Draw food
#         pygame.draw.rect(screen, (255, 215, 0),
#                          (food[1]*CELL, food[0]*CELL, CELL-2, CELL-2))

#         # Draw Snake A (blue)
#         for r, c in snakeA:
#             pygame.draw.rect(screen, (66, 135, 245),
#                              (c*CELL, r*CELL, CELL-2, CELL-2))

#         # Draw Snake B (red)
#         for r, c in snakeB:
#             pygame.draw.rect(screen, (245, 66, 66),
#                              (c*CELL, r*CELL, CELL-2, CELL-2))

#         pygame.display.flip()
#         # -------------------------

#         print(f"STEP {step} | Score A={scoreA} | Score B={scoreB}")

#         # Slow animation
#         clock.tick(3)          # 3 FPS slow
#         pygame.time.delay(350)

#         step += 1
#         if step > 150:
#             print("Max steps reached → Score winner")
#             break

#     print("\n--- FINAL SCORES ---")
#     print("Snake A:", scoreA)
#     print("Snake B:", scoreB)

#     if scoreA > scoreB:
#         print("Winner: Snake A")
#     elif scoreB > scoreA:
#         print("Winner: Snake B")
#     else:
#         print("DRAW")

#     pygame.time.delay(2000)
#     pygame.quit()


# smart_snake_duel_pygame()
