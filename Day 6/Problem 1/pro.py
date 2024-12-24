def guard_patrol(grid):
    # Parse the grid to find the guard's initial position and direction
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    direction_order = ['^', '>', 'v', '<']  # For turning right (90 degrees clockwise)
    rows, cols = len(grid), len(grid[0])
    
    # Locate the guard's starting position and direction
    guard_pos = None
    guard_dir = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in directions:
                guard_pos = (r, c)
                guard_dir = grid[r][c]
                break
        if guard_pos:
            break

    visited = set()
    visited.add(guard_pos)

    while True:
        # Calculate next position based on current direction
        dr, dc = directions[guard_dir]
        nr, nc = guard_pos[0] + dr, guard_pos[1] + dc
        
        if 0 <= nr < rows and 0 <= nc < cols:
            # Within bounds
            if grid[nr][nc] == '#':
                # Obstacle in front, turn right
                current_idx = direction_order.index(guard_dir)
                guard_dir = direction_order[(current_idx + 1) % 4]
            else:
                # Move forward
                guard_pos = (nr, nc)
                visited.add(guard_pos)
        else:
            # Out of bounds, stop the simulation
            break

    return len(visited)

# Read input from input.txt
with open('input.txt', 'r') as infile:
    grid = [list(line.strip()) for line in infile]

# Run the guard_patrol function
path_length = guard_patrol(grid)

# Write the result to output.txt
with open('output.txt', 'w') as outfile:
    outfile.write(f"{path_length}\n")
