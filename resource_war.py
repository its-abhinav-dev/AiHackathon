import random
from collections import deque

# -------- BFS to nearest resource ----------
def bfs(grid, start):
    rows, cols = len(grid), len(grid[0])
    q = deque([(start[0], start[1], [])])
    visited = set([(start[0], start[1])])

    while q:
        r, c, path = q.popleft()

        if grid[r][c] == "R":
            return path + [(r, c)]

        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    q.append((nr, nc, path + [(nr, nc)]))
    return None


# -------- Print grid ----------
def print_grid(grid):
    for row in grid:
        print(" ".join(row))
    print()


# -------- Simulation ----------
def resource_war():

    # 7x7 grid
    grid = [
        [".",".",".",".",".",".","."],
        [".",".",".",".",".",".","."],
        [".",".","R",".",".",".","."],
        [".",".",".","A",".",".","."],
        [".",".",".",".","B",".","."],
        [".",".",".",".",".",".","."],
        [".",".",".",".",".",".","."]
    ]

    posA = (3, 3)
    posB = (4, 4)

    scoreA = 0
    scoreB = 0

    total_resources = 10   # total resources that can spawn
    step = 1
    max_steps = 40

    print("\n--- RESOURCE WAR ---\n")

    while step <= max_steps:

        print(f"STEP {step}")

        # Spawn new resource every 3 steps (if remaining)
        if step % 3 == 0 and total_resources > 0:
            while True:
                r = random.randint(0, 6)
                c = random.randint(0, 6)
                if grid[r][c] == ".":
                    grid[r][c] = "R"
                    total_resources -= 1
                    print(f"New Resource spawned at ({r},{c})")
                    break

        # ---- BFS pathfinding ----
        pathA = bfs(grid, posA)
        pathB = bfs(grid, posB)

        nextA = pathA[0] if pathA else posA
        nextB = pathB[0] if pathB else posB

        # Remove old positions
        grid[posA[0]][posA[1]] = "."
        grid[posB[0]][posB[1]] = "."

        # Move agents
        posA = nextA
        posB = nextB

        collectedA = False
        collectedB = False

        # Resource collection
        if grid[posA[0]][posA[1]] == "R":
            scoreA += 1
            collectedA = True

        if grid[posB[0]][posB[1]] == "R":
            scoreB += 1
            collectedB = True

        # If both reach same resource
        if collectedA and collectedB and posA == posB:
            print("Both agents reached the same resource! +1 each")

        # Remove resource
        if collectedA or collectedB:
            grid[posA[0]][posA[1]] = "."
            grid[posB[0]][posB[1]] = "."

        # Place agents
        if posA == posB:
            grid[posA[0]][posA[1]] = "AB"
        else:
            grid[posA[0]][posA[1]] = "A"
            grid[posB[0]][posB[1]] = "B"

        print_grid(grid)
        print(f"Score A: {scoreA}   Score B: {scoreB}")
        print("------------------------------------\n")

        step += 1

    # Final result
    print("\n--- GAME OVER ---")
    print("Final Statistics:")
    print(f"Agent A collected: {scoreA}")
    print(f"Agent B collected: {scoreB}")

    if scoreA > scoreB:
        print("Winner: Agent A 🏆")
    elif scoreB > scoreA:
        print("Winner: Agent B 🏆")
    else:
        print("Result: DRAW 🤝")


resource_war()
