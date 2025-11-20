import heapq
import math

# -------- A* Pathfinding ----------
def a_star(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    pq = []
    heapq.heappush(pq, (0 + dist(start, goal), 0, start, []))
    visited = set()

    while pq:
        est_total, cost, node, path = heapq.heappop(pq)

        if node in visited:
            continue
        visited.add(node)

        if node == goal:
            return path + [node]

        r, c = node
        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != "#":
                if (nr, nc) not in visited:
                    heapq.heappush(
                        pq,
                        (cost + 1 + dist((nr, nc), goal),
                         cost + 1,
                         (nr, nc),
                         path + [node])
                    )
    return None

def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# -------- Print Grid -------
def print_grid(grid):
    for row in grid:
        print(" ".join(row))
    print()

# -------- Game Simulation -------
def capture_the_flag():

    # 7x7 grid
    grid = [
        ["FA", ".", ".", ".", ".", ".", "FB"],
        [".", ".", ".", ".", ".", ".", "."],
        [".", "#", "#", "#", ".", ".", "."],
        [".", ".", "A", ".", ".", ".", "."],
        [".", ".", ".", ".", "B", ".", "."],
        [".", ".", ".", ".", ".", ".", "."],
        ["FA", ".", ".", ".", ".", ".", "FB"]
    ]

    # Flags fixed
    flagA = (0, 0)
    flagB = (0, 6)

    # Starting positions
    posA = (3, 2)
    posB = (4, 4)

    logs = []
    step = 1
    max_steps = 50

    print("\n--- CAPTURE THE FLAG ---\n")

    while step <= max_steps:

        logs.append(f"\nSTEP {step}")

        # Decide mode: attack or defend
        modeA = "ATTACK"
        modeB = "ATTACK"

        # Defense trigger radius
        if dist(posB, flagA) <= 2:
            modeA = "DEFEND"
        if dist(posA, flagB) <= 2:
            modeB = "DEFEND"

        logs.append(f"Agent A mode: {modeA}")
        logs.append(f"Agent B mode: {modeB}")

        # Decide targets
        targetA = flagB if modeA == "ATTACK" else posB
        targetB = flagA if modeB == "ATTACK" else posA

        # A* movement
        pathA = a_star(grid, posA, targetA)
        pathB = a_star(grid, posB, targetB)

        # Next step
        nextA = pathA[1] if pathA and len(pathA) > 1 else posA
        nextB = pathB[1] if pathB and len(pathB) > 1 else posB

        # Clear old positions
        grid[posA[0]][posA[1]] = "."
        grid[posB[0]][posB[1]] = "."

        # Update positions
        posA = nextA
        posB = nextB

        # Check capture conditions
        if posA == flagB:
            logs.append("Agent A captured Flag B! 🏆")
            winner = "Agent A"
            return winner, logs

        if posB == flagA:
            logs.append("Agent B captured Flag A! 🏆")
            winner = "Agent B"
            return winner, logs

        # Update grid
        grid[posA[0]][posA[1]] = "A"
        grid[posB[0]][posB[1]] = "B"

        # Print grid for each step
        print(f"STEP {step}")
        print_grid(grid)

        step += 1

    return "DRAW", logs


# ---- Run Game ----
winner, logs = capture_the_flag()

print("\n--- MATCH OVER ---")
print("Winner:", winner)
print("\n--- EVENT LOGS ---")
for l in logs:
    print(l)
