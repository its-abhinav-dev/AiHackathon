from copy import deepcopy

ROWS, COLS = 7, 7
MAX_STEPS = 8   # time limit (you can change this)

def print_grid(grid):
    for row in grid:
        print(" ".join(row))
    print()

def get_neighbors(r, c):
    for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < ROWS and 0 <= nc < COLS:
            yield nr, nc

def simulate_maze_domination():
    # Initial maze
    # . = empty, # = wall, A/B = agents' starting territory
    grid = [
        ["A", ".", ".", "#", ".", ".", "B"],
        [".", ".", ".", "#", ".", ".", "."],
        [".", "#", ".", ".", ".", "#", "."],
        [".", ".", ".", ".", ".", ".", "."],
        [".", "#", ".", ".", ".", "#", "."],
        [".", ".", ".", "#", ".", ".", "."],
        ["A", ".", ".", "#", ".", ".", "B"]
    ]

    print("\n--- MAZE DOMINATION: INITIAL GRID ---\n")
    print_grid(grid)

    step = 1
    while step <= MAX_STEPS:
        print(f"STEP {step}")

        # Sets of cells each agent wants to claim this step
        targets_A = set()
        targets_B = set()

        # Scan grid and find expansion targets
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "A":
                    for nr, nc in get_neighbors(r, c):
                        if grid[nr][nc] == ".":  # only expand into free cells
                            targets_A.add((nr, nc))
                elif grid[r][c] == "B":
                    for nr, nc in get_neighbors(r, c):
                        if grid[nr][nc] == ".":
                            targets_B.add((nr, nc))

        # If no one can expand, stop early
        if not targets_A and not targets_B:
            print("No more expansion possible. Stopping early.\n")
            break

        # Create copy to update for this step
        new_grid = deepcopy(grid)

        # Resolve claims
        all_targets = targets_A.union(targets_B)
        for (r, c) in all_targets:
            if (r, c) in targets_A and (r, c) in targets_B:
                # Conflict: both trying to claim same cell
                new_grid[r][c] = "X"   # blocked, no one owns
            elif (r, c) in targets_A:
                new_grid[r][c] = "A"
            elif (r, c) in targets_B:
                new_grid[r][c] = "B"

        grid = new_grid

        print_grid(grid)
        step += 1

    # After simulation, calculate territory
    total_cells = ROWS * COLS
    count_A = sum(row.count("A") for row in grid)
    count_B = sum(row.count("B") for row in grid)
    count_X = sum(row.count("X") for row in grid)

    perc_A = (count_A / total_cells) * 100
    perc_B = (count_B / total_cells) * 100

    print("--- FINAL RESULT ---")
    print_grid(grid)
    print(f"Agent A cells: {count_A}")
    print(f"Agent B cells: {count_B}")
    print(f"Conflict cells (X): {count_X}")
    print(f"Total cells: {total_cells}")
    print(f"Agent A territory: {perc_A:.2f}%")
    print(f"Agent B territory: {perc_B:.2f}%")

    if count_A > count_B:
        print("Winner: Agent A 🏆 (more territory)")
    elif count_B > count_A:
        print("Winner: Agent B 🏆 (more territory)")
    else:
        print("Result: DRAW 🤝 (equal domination)")

simulate_maze_domination()
