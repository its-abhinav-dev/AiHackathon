import random
import heapq
import time

# Directions
DIRS = [(1,0),(-1,0),(0,1),(0,-1)]

# Manhattan distance
def h(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

# A* Algorithm
def a_star(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    pq = []
    heapq.heappush(pq, (h(start, goal), 0, start, []))
    visited = set()

    while pq:
        est, g, node, path = heapq.heappop(pq)

        if node in visited:
            continue
        visited.add(node)

        if node == goal:
            return path + [node]

        r, c = node
        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] != "#" and (nr, nc) not in visited:
                    heapq.heappush(
                        pq, (g+1 + h((nr,nc), goal), g+1, (nr,nc), path+[node])
                    )

    return None


def print_grid(grid):
    for row in grid:
        print(" ".join(row))
    print()


# -------- MAIN GAME ----------
def grid_racing_ai():

    rows, cols = 10, 10

    # Generate grid with random obstacles
    grid = [["." for _ in range(cols)] for _ in range(rows)]

    # Random obstacles
    for _ in range(18):
        r = random.randint(0, rows-1)
        c = random.randint(0, cols-1)
        if (r, c) not in [(0,0),(9,0),(5,9)]:
            grid[r][c] = "#"

    # START & GOAL
    startA = (0, 0)
    startB = (9, 0)
    goal = (5, 9)

    grid[startA[0]][startA[1]] = "A"
    grid[startB[0]][startB[1]] = "B"
    grid[goal[0]][goal[1]] = "G"

    print("\n--- GRID RACING AI ---\n")
    print("Initial Grid:")
    print_grid(grid)

    # Compute A* paths
    pathA = a_star(grid, startA, goal)
    pathB = a_star(grid, startB, goal)

    if pathA is None:
        print("Agent A has no path! DNF ❌")
    if pathB is None:
        print("Agent B has no path! DNF ❌")

    # If both fail
    if pathA is None and pathB is None:
        print("\nNo winner — both agents stuck.")
        return

    print("\n--- RACE STARTS ---\n")

    # Race simulation
    timeA = None
    timeB = None

    posA = startA
    posB = startB

    step = 1

    while True:
        print(f"STEP {step}")

        # Clear agent positions (not obstacles or goal)
        if posA != startA: grid[posA[0]][posA[1]] = "."
        if posB != startB: grid[posB[0]][posB[1]] = "."

        # Move A
        if pathA and len(pathA) > 1:
            posA = pathA.pop(1)
            grid[posA[0]][posA[1]] = "A"
            if posA == goal and timeA is None:
                timeA = step

        # Move B
        if pathB and len(pathB) > 1:
            posB = pathB.pop(1)
            grid[posB[0]][posB[1]] = "B"
            if posB == goal and timeB is None:
                timeB = step

        print_grid(grid)
        print(f"TimeA: {timeA}   TimeB: {timeB}")
        print("----------------------------------\n")

        step += 1
        time.sleep(0.5)

        # End when both reach or stuck
        if timeA is not None and timeB is not None:
            break
        if (not pathA or pathA == [goal]) and (not pathB or pathB == [goal]):
            break

    print("\n--- RACE FINISHED ---")

    if timeA is None and timeB is None:
        print("No one reached goal.")
    elif timeA is None:
        print("Agent B Wins! 🏆")
    elif timeB is None:
        print("Agent A Wins! 🏆")
    else:
        if timeA < timeB:
            print("Agent A Wins! 🏁🏆")
        elif timeB < timeA:
            print("Agent B Wins! 🏁🏆")
        else:
            print("DRAW — both reached at same time")

    print(f"\nFinal Times:\nA = {timeA}\nB = {timeB}")


# Run game
grid_racing_ai()
