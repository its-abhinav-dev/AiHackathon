from collections import deque
import copy

def bfs(grid, start):
    rows, cols = len(grid), len(grid[0])
    q = deque([(start[0], start[1], [])])
    visited = {(start[0], start[1])}

    while q:
        r, c, path = q.popleft()

        if grid[r][c] == "C":
            return path + [(r, c)]

        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    q.append((nr, nc, path + [(nr, nc)]))
    return None


def print_grid(grid):
    for row in grid:
        print(" ".join(row))
    print()


def treasure_grab():

    grid = [
        [".", "C", ".", ".", "C"],
        [".", ".", ".", "C", "."],
        ["A", ".", ".", ".", "B"],
        [".", "C", ".", ".", "."],
        ["C", ".", ".", "C", "."]
    ]

    posA = (2, 0)
    posB = (2, 4)

    scoreA = 0
    scoreB = 0
    step = 1

    print("\n--- TREASURE GRAB (REWRITTEN & FULLY FIXED) ---\n")

    while True:

        # Stop when no coins left
        if not any("C" in row for row in grid):
            break

        print(f"STEP {step}:")

        old_grid = copy.deepcopy(grid)   # snapshot for BFS & scoring

        # BFS paths
        pathA = bfs(old_grid, posA)
        pathB = bfs(old_grid, posB)

        nextA = pathA[0] if pathA else posA
        nextB = pathB[0] if pathB else posB

        # ⭐ SCORE USING OLD GRID ONLY
        coinA = (old_grid[nextA[0]][nextA[1]] == "C")
        coinB = (old_grid[nextB[0]][nextB[1]] == "C")

        if nextA == nextB and coinA:
            scoreA += 1
            scoreB += 1
        else:
            if coinA: scoreA += 1
            if coinB: scoreB += 1

        # ⭐ BUILD NEW GRID FROM SCRATCH
        new_grid = [["." for _ in range(5)] for _ in range(5)]

        # copy coins that were NOT collected
        for r in range(5):
            for c in range(5):
                if old_grid[r][c] == "C":
                    if (r, c) not in [nextA, nextB]:
                        new_grid[r][c] = "C"

        # update positions
        posA = nextA
        posB = nextB

        # place agents
        if posA == posB:
            new_grid[posA[0]][posA[1]] = "AB"
        else:
            new_grid[posA[0]][posA[1]] = "A"
            new_grid[posB[0]][posB[1]] = "B"

        grid = new_grid

        print_grid(grid)
        print(f"Score A: {scoreA}    Score B: {scoreB}")
        print("-------------------------------------------\n")

        step += 1

    print("\nALL COINS COLLECTED!\n")
    print("FINAL SCORES:")
    print(f"Agent A: {scoreA}")
    print(f"Agent B: {scoreB}")

    if scoreA > scoreB:
        print("Winner: Agent A 🏆")
    elif scoreB > scoreA:
        print("Winner: Agent B 🏆")
    else:
        print("Result: DRAW 🤝")


treasure_grab()


















# import pygame
# import copy
# from collections import deque
# import sys
# import time

# # -----------------------------
# # BFS to nearest coin
# # -----------------------------
# def bfs(grid, start):
#     rows, cols = len(grid), len(grid[0])
#     q = deque([(start[0], start[1], [])])
#     visited = {(start[0], start[1])}

#     while q:
#         r, c, path = q.popleft()

#         if grid[r][c] == "C":
#             return path + [(r, c)]

#         for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
#             nr, nc = r + dr, c + dc
#             if 0 <= nr < rows and 0 <= nc < cols:
#                 if (nr, nc) not in visited:
#                     visited.add((nr, nc))
#                     q.append((nr, nc, path + [(nr, nc)]))
#     return None


# # -----------------------------
# # PYGAME GRID DRAW FUNCTION
# # -----------------------------
# def draw_grid(screen, grid, size=80):
#     colors = {
#         ".": (30, 30, 30),
#         "C": (255, 215, 0),
#         "A": (66, 135, 245),
#         "B": (240, 77, 65),
#         "AB": (160, 32, 240)
#     }

#     for r in range(5):
#         for c in range(5):
#             cell = grid[r][c]
#             color = colors.get(cell, (255, 255, 255))

#             pygame.draw.rect(
#                 screen,
#                 color,
#                 pygame.Rect(c * size, r * size, size - 2, size - 2)
#             )


# # -----------------------------
# # MAIN GAME LOOP
# # -----------------------------
# def treasure_grab_pygame():

#     pygame.init()
#     cell_size = 80
#     screen = pygame.display.set_mode((cell_size * 5, cell_size * 5))
#     pygame.display.set_caption("Treasure Grab AI - Pygame Visualization")

#     clock = pygame.time.Clock()

#     # Initial grid
#     grid = [
#         [".", "C", ".", ".", "C"],
#         [".", ".", ".", "C", "."],
#         ["A", ".", ".", ".", "B"],
#         [".", "C", ".", ".", "."],
#         ["C", ".", ".", "C", "."]
#     ]

#     posA = (2, 0)
#     posB = (2, 4)

#     scoreA = 0
#     scoreB = 0

#     running = True
#     step = 1

#     while running:

#         # Exit window
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#                 pygame.quit()
#                 sys.exit()

#         # Stop if no coins left
#         if not any("C" in row for row in grid):
#             print("\nALL COINS COLLECTED!")
#             print("Final Score A:", scoreA)
#             print("Final Score B:", scoreB)
#             if scoreA > scoreB:
#                 print("Winner: Agent A")
#             elif scoreB > scoreA:
#                 print("Winner: Agent B")
#             else:
#                 print("DRAW")
#             time.sleep(2)
#             running = False
#             break

#         old_grid = copy.deepcopy(grid)

#         # BFS find coins
#         pathA = bfs(old_grid, posA)
#         pathB = bfs(old_grid, posB)

#         nextA = pathA[0] if pathA else posA
#         nextB = pathB[0] if pathB else posB

#         # Scoring using OLD grid
#         coinA = old_grid[nextA[0]][nextA[1]] == "C"
#         coinB = old_grid[nextB[0]][nextB[1]] == "C"

#         if nextA == nextB and coinA:
#             scoreA += 1
#             scoreB += 1
#         else:
#             if coinA: scoreA += 1
#             if coinB: scoreB += 1

#         # Build new grid
#         new_grid = [["." for _ in range(5)] for _ in range(5)]

#         # Replace coins except collected ones
#         for r in range(5):
#             for c in range(5):
#                 if old_grid[r][c] == "C" and (r, c) not in [nextA, nextB]:
#                     new_grid[r][c] = "C"

#         posA = nextA
#         posB = nextB

#         # Place agents
#         if posA == posB:
#             new_grid[posA[0]][posA[1]] = "AB"
#         else:
#             new_grid[posA[0]][posA[1]] = "A"
#             new_grid[posB[0]][posB[1]] = "B"

#         grid = new_grid

#         # Draw
#         screen.fill((0, 0, 0))
#         draw_grid(screen, grid, size=cell_size)
#         pygame.display.flip()

#         clock.tick(1)   # ⭐ FPS (speed) — 6 FPS = smooth, not too fast

#         step += 1


# # Run game
# treasure_grab_pygame()
