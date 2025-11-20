import time
import random

# Directions
DIRS = [(1,0),(-1,0),(0,1),(0,-1)]

def in_bounds(r, c):
    return 0 <= r < 10 and 0 <= c < 10

def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def print_grid(predator, prey):
    grid = [["." for _ in range(10)] for _ in range(10)]
    pr, pc = predator
    er, ec = prey
    grid[pr][pc] = "P"
    grid[er][ec] = "E"

    for row in grid:
        print(" ".join(row))
    print()

# 🔥 RANDOM PREDATOR MOVEMENT
def predator_move(predator):
    r, c = predator
    possible = []

    for dr, dc in DIRS:
        nr, nc = r + dr, c + dc
        if in_bounds(nr, nc):
            possible.append((nr, nc))

    return random.choice(possible)

# 🧠 SMART PREY MOVEMENT (No Oscillation)
def prey_move(prey, predator, last_pos):
    best = None
    bestDist = -1
    r, c = prey
    moved = False

    for dr, dc in DIRS:
        nr, nc = r + dr, c + dc
        if in_bounds(nr, nc):

            # Prevent oscillation
            if (nr, nc) == last_pos:
                continue

            d = dist((nr, nc), predator)
            if d > bestDist:
                bestDist = d
                best = (nr, nc)
                moved = True

    # No alternative escape → allow returning to last_pos
    if not moved:
        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if in_bounds(nr, nc):
                return (nr, nc)

    return best


def predator_prey_sim():

    predator = (0, 0)
    prey = (9, 9)
    last_prey_pos = prey

    print("\n--- PREDATOR–PREY (Random Predator + Smart Prey) ---\n")

    for step in range(1, 51):

        print(f"STEP {step}")
        print_grid(predator, prey)

        if predator == prey:
            print("Predator caught the prey! 🦁🏆")
            return

        # Prey moves first
        new_prey = prey_move(prey, predator, last_prey_pos)
        last_prey_pos = prey
        prey = new_prey

        # Predator moves randomly
        predator = predator_move(predator)

        if predator == prey:
            print_grid(predator, prey)
            print("Predator caught the prey! 🦁🏆")
            return

        time.sleep(0.3)

    print("\nPrey survived 50 steps → Prey Wins! 🐇✨")


# Run simulation
predator_prey_sim()














# import pygame
# import random
# import sys
# import time

# # Directions
# DIRS = [(1,0),(-1,0),(0,1),(0,-1)]

# def in_bounds(r, c):
#     return 0 <= r < 10 and 0 <= c < 10

# def dist(a, b):
#     return abs(a[0] - b[0]) + abs(a[1] - b[1])

# # 🔥 RANDOM PREDATOR MOVEMENT
# def predator_move(predator):
#     r, c = predator
#     possible = []

#     for dr, dc in DIRS:
#         nr, nc = r + dr, c + dc
#         if in_bounds(nr, nc):
#             possible.append((nr, nc))

#     return random.choice(possible)

# # 🧠 SMART PREY MOVEMENT (No oscillation)
# def prey_move(prey, predator, last_pos):
#     best = None
#     bestDist = -1
#     r, c = prey
#     moved = False

#     for dr, dc in DIRS:
#         nr, nc = r + dr, c + dc
#         if in_bounds(nr, nc):

#             if (nr, nc) == last_pos:
#                 continue

#             d = dist((nr, nc), predator)
#             if d > bestDist:
#                 bestDist = d
#                 best = (nr, nc)
#                 moved = True

#     if not moved:  # No alternative escape
#         for dr, dc in DIRS:
#             nr, nc = r + dr, c + dc
#             if in_bounds(nr, nc):
#                 return (nr, nc)

#     return best


# # -----------------------------
# # 🔵 PYGAME VISUAL SIMULATION
# # -----------------------------
# def predator_prey_sim_pygame():

#     pygame.init()
#     CELL = 60
#     screen = pygame.display.set_mode((10 * CELL, 10 * CELL))
#     pygame.display.set_caption("Predator–Prey Simulation (Your Exact Logic)")

#     clock = pygame.time.Clock()

#     predator = (0, 0)
#     prey = (9, 9)
#     last_prey_pos = prey

#     step = 1

#     print("\n--- PREDATOR–PREY (ANIMATED) ---\n")

#     running = True

#     while running:

#         # Quit window
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()

#         # DRAW GRID
#         screen.fill((30, 30, 30))

#         # Draw predator
#         pygame.draw.rect(screen, (255, 80, 80),
#                          (predator[1]*CELL, predator[0]*CELL, CELL-2, CELL-2))

#         # Draw prey
#         pygame.draw.rect(screen, (80, 255, 80),
#                          (prey[1]*CELL, prey[0]*CELL, CELL-2, CELL-2))

#         pygame.display.flip()

#         # Catch check
#         if predator == prey:
#             print(f"STEP {step}")
#             print("Predator caught the prey! 🦁🏆")
#             time.sleep(2)
#             running = False
#             break

#         # ------- PREY MOVES (same logic) -------
#         new_pre = prey_move(prey, predator, last_prey_pos)
#         last_prey_pos = prey
#         prey = new_pre

#         # ------- PREDATOR MOVES (same logic) -------
#         predator = predator_move(predator)

#         # Catch check
#         if predator == prey:
#             print(f"STEP {step}")
#             print("Predator caught the prey! 🦁🏆")
#             time.sleep(2)
#             running = False
#             break

#         print(f"STEP {step} | Predator={predator} | Prey={prey}")
        
#         clock.tick(3)           # Slow and readable
#         pygame.time.delay(300)  # Extra delay
#         step += 1

#         if step > 50:
#             print("Prey survived → PREY WINS 🐇✨")
#             time.sleep(2)
#             running = False
#             break

#     pygame.quit()


# predator_prey_sim_pygame()
