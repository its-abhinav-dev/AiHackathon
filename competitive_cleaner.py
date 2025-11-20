from collections import deque

# BFS to nearest dirty cell 'D'
def bfs_to_dirt(grid, start):
    rows, cols = len(grid), len(grid[0])
    q = deque([(start[0], start[1], [])])
    visited = set([(start[0], start[1])])

    while q:
        r, c, path = q.popleft()

        # Found dirt
        if grid[r][c] == "D":
            return path + [(r, c)]

        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if (nr, nc) not in visited and grid[nr][nc] != "#":
                    visited.add((nr, nc))
                    q.append((nr, nc, path + [(nr, nc)]))

    return None  # no reachable dirt


def print_grid(grid):
    for row in grid:
        print(" ".join(row))
    print()


def print_leaderboard(scoreA, scoreB, total_dirt):
    print("\n--- LEADERBOARD ---")

    total_cleaned = scoreA + scoreB
    percA = (scoreA / total_dirt * 100) if total_dirt > 0 else 0
    percB = (scoreB / total_dirt * 100) if total_dirt > 0 else 0

    # Simple text bar chart
    barA = "#" * int(percA // 5)   # max 20 chars
    barB = "#" * int(percB // 5)

    print(f"Total dirt cleaned: {total_cleaned} / {total_dirt}\n")

    print(f"Agent A: {scoreA} cells ({percA:.2f}%)")
    print(f"[{barA}]")
    print()
    print(f"Agent B: {scoreB} cells ({percB:.2f}%)")
    print(f"[{barB}]")
    print()

    if scoreA > scoreB:
        print("Winner: Agent A 🏆")
    elif scoreB > scoreA:
        print("Winner: Agent B 🏆")
    else:
        print("Result: DRAW 🤝")


def competitive_cleaner():

    # Initial grid (you can change pattern)
    grid = [
        ["D", "D", ".", ".", "D", "D", "D"],
        [".", "D", ".", "D", ".", ".", "D"],
        ["A", ".", "D", ".", "D", ".", "."],
        [".", ".", ".", ".", ".", "D", "."],
        [".", "D", ".", "D", ".", ".", "D"],
        [".", ".", "D", ".", "D", ".", "."],
        ["D", "D", ".", ".", "D", "B", "D"]
    ]

    rows, cols = len(grid), len(grid[0])

    # Initial positions of agents
    posA = None
    posB = None

    total_dirt_initial = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "A":
                posA = (r, c)
            elif grid[r][c] == "B":
                posB = (r, c)
            if grid[r][c] == "D":
                total_dirt_initial += 1

    scoreA = 0
    scoreB = 0
    step = 1

    print("\n--- COMPETITIVE CLEANER ---\n")
    print("Initial Grid:")
    print_grid(grid)
    print(f"Total dirt cells: {total_dirt_initial}\n")

    while True:
        # Check if any dirt left
        any_dirt = any("D" in row for row in grid)
        if not any_dirt:
            print("No more dirt to clean. Stopping.\n")
            break

        print(f"STEP {step}")

        # Find paths to nearest dirt
        pathA = bfs_to_dirt(grid, posA)
        pathB = bfs_to_dirt(grid, posB)

        # Decide next move (one step along the path)
        nextA = posA
        nextB = posB

        if pathA and len(pathA) > 0:
            # First element in path is already the target node; 
            # if you want one-step movement, choose path[0]
            nextA = pathA[0]
        if pathB and len(pathB) > 0:
            nextB = pathB[0]

        # Clear current positions
        grid[posA[0]][posA[1]] = "."
        grid[posB[0]][posB[1]] = "."

        # Move agents
        posA = nextA
        posB = nextB

        # Cleaning logic
        cleanedA = False
        cleanedB = False

        # IMPORTANT: check original dirt before overwriting
        if grid[posA[0]][posA[1]] == "D":
            scoreA += 1
            cleanedA = True
        if grid[posB[0]][posB[1]] == "D":
            scoreB += 1
            cleanedB = True

        # If both land on same dirty cell at same time → both get a point
        if posA == posB and cleanedA and cleanedB:
            print("Both agents cleaned the same cell! +1 each")

        # Remove dirt from those cells
        if cleanedA:
            grid[posA[0]][posA[1]] = "."
        if cleanedB:
            grid[posB[0]][posB[1]] = "."

        # Place agents on grid
        if posA == posB:
            grid[posA[0]][posA[1]] = "AB"
        else:
            grid[posA[0]][posA[1]] = "A"
            grid[posB[0]][posB[1]] = "B"

        print_grid(grid)
        print(f"Score A: {scoreA}   Score B: {scoreB}")
        print("-------------------------------------\n")

        step += 1
        if step > 100:  # safety break
            print("Step limit reached. Stopping.\n")
            break

    # Final leaderboard
    print_leaderboard(scoreA, scoreB, total_dirt_initial)


# Run the simulation
competitive_cleaner()















# from collections import deque
# import matplotlib.pyplot as plt

# # BFS to nearest dirty cell 'D'
# def bfs_to_dirt(grid, start):
#     rows, cols = len(grid), len(grid[0])
#     q = deque([(start[0], start[1], [])])
#     visited = set([(start[0], start[1])])

#     while q:
#         r, c, path = q.popleft()

#         # Found dirt
#         if grid[r][c] == "D":
#             return path + [(r, c)]

#         for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
#             nr, nc = r + dr, c + dc
#             if 0 <= nr < rows and 0 <= nc < cols:
#                 if (nr, nc) not in visited and grid[nr][nc] != "#":
#                     visited.add((nr, nc))
#                     q.append((nr, nc, path + [(nr, nc)]))

#     return None  # no reachable dirt


# def print_grid(grid):
#     for row in grid:
#         print(" ".join(row))
#     print()


# # ===========================
# #  MATPLOTLIB LEADERBOARD
# # ===========================
# def print_leaderboard(scoreA, scoreB, total_dirt):
#     print("\n--- LEADERBOARD ---")

#     total_cleaned = scoreA + scoreB
#     percA = (scoreA / total_dirt * 100) if total_dirt > 0 else 0
#     percB = (scoreB / total_dirt * 100) if total_dirt > 0 else 0

#     print(f"Agent A cleaned: {scoreA} cells ({percA:.2f}%)")
#     print(f"Agent B cleaned: {scoreB} cells ({percB:.2f}%)")

#     # --------- MATPLOTLIB VISUALIZATION ---------
#     agents = ['Agent A', 'Agent B']
#     scores = [scoreA, scoreB]
#     colors = ['skyblue', 'salmon']

#     plt.figure(figsize=(7, 5))
#     bars = plt.bar(agents, scores, color=colors)

#     plt.xlabel("Agents")
#     plt.ylabel("Cells Cleaned")
#     plt.title("Competitive Cleaner - Leaderboard")

#     # Add numbers above bars
#     for bar in bars:
#         yval = bar.get_height()
#         plt.text(bar.get_x() + bar.get_width()/2 - 0.1, yval + 0.2, int(yval))

#     plt.ylim(0, max(scores) + 2)
#     plt.show()


# # ===========================
# #     MAIN CLEANER GAME
# # ===========================
# def competitive_cleaner():

#     # Initial grid
#     grid = [
#         ["D", "D", ".", ".", "D", "D", "D"],
#         [".", "D", ".", "D", ".", ".", "D"],
#         ["A", ".", "D", ".", "D", ".", "."],
#         [".", ".", ".", ".", ".", "D", "."],
#         [".", "D", ".", "D", ".", ".", "D"],
#         [".", ".", "D", ".", "D", ".", "."],
#         ["D", "D", ".", ".", "D", "B", "D"]
#     ]

#     rows, cols = len(grid), len(grid[0])

#     posA = None
#     posB = None
#     total_dirt_initial = 0

#     for r in range(rows):
#         for c in range(cols):
#             if grid[r][c] == "A":
#                 posA = (r, c)
#             elif grid[r][c] == "B":
#                 posB = (r, c)
#             if grid[r][c] == "D":
#                 total_dirt_initial += 1

#     scoreA = 0
#     scoreB = 0
#     step = 1

#     print("\n--- COMPETITIVE CLEANER ---\n")
#     print("Initial Grid:")
#     print_grid(grid)
#     print(f"Total dirt cells: {total_dirt_initial}\n")

#     while True:
#         # Check if any dirt left
#         any_dirt = any("D" in row for row in grid)
#         if not any_dirt:
#             print("No more dirt to clean. Stopping.\n")
#             break

#         print(f"STEP {step}")

#         # Find paths to nearest dirt
#         pathA = bfs_to_dirt(grid, posA)
#         pathB = bfs_to_dirt(grid, posB)

#         # One-step movement
#         nextA = posA if not pathA else pathA[0]
#         nextB = posB if not pathB else pathB[0]

#         # Clear old positions
#         grid[posA[0]][posA[1]] = "."
#         grid[posB[0]][posB[1]] = "."

#         # Move agents
#         posA = nextA
#         posB = nextB

#         cleanedA = cleanedB = False

#         # Clean before overwriting
#         if grid[posA[0]][posA[1]] == "D":
#             scoreA += 1
#             cleanedA = True

#         if grid[posB[0]][posB[1]] == "D":
#             scoreB += 1
#             cleanedB = True

#         if posA == posB and cleanedA and cleanedB:
#             print("Both agents cleaned the same cell! +1 each")

#         # Remove dirt
#         if cleanedA:
#             grid[posA[0]][posA[1]] = "."
#         if cleanedB:
#             grid[posB[0]][posB[1]] = "."

#         # Place agents
#         if posA == posB:
#             grid[posA[0]][posA[1]] = "AB"
#         else:
#             grid[posA[0]][posA[1]] = "A"
#             grid[posB[0]][posB[1]] = "B"

#         print_grid(grid)
#         print(f"Score A: {scoreA}   Score B: {scoreB}")
#         print("-------------------------------------\n")

#         step += 1
#         if step > 100:
#             print("Step limit reached. Stopping.\n")
#             break

#     # Show final leaderboard
#     print_leaderboard(scoreA, scoreB, total_dirt_initial)


# # Run the game
# competitive_cleaner()
