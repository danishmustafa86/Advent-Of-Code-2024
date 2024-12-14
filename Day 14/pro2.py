import re
from collections import defaultdict
import os

# Constants for grid dimensions
GRID_WIDTH = 100
GRID_HEIGHT = 100

# Parse the input file to extract robot positions and velocities
def parse_input(filename):
    if not os.path.exists(filename):
        raise FileNotFoundError(f"File not found: {filename}")
    
    robots = []
    pattern = re.compile(r"p=<\s*(-?\d+),\s*(-?\d+)>,\s*v=<\s*(-?\d+),\s*(-?\d+)>")
    
    with open(filename, "r") as file:
        for line in file:
            match = pattern.match(line.strip())
            if match:
                x, y, vx, vy = map(int, match.groups())
                robots.append(((x, y), (vx, vy)))
            else:
                print(f"Skipped line (no match): {line.strip()}")
    
    if not robots:
        raise ValueError("Error: No robots data to process. Check the input file format.")
    
    return robots

# Simulate the robots for a given number of seconds
def simulate_robots(robots, seconds):
    positions = defaultdict(int)

    for (x, y), (vx, vy) in robots:
        new_x = (x + vx * seconds) % GRID_WIDTH
        new_y = (y + vy * seconds) % GRID_HEIGHT
        positions[(new_x, new_y)] += 1

    return positions

# Find the fewest seconds for alignment in a condensed pattern
def find_alignment_time(robots, max_seconds=10000, threshold=20):
    for t in range(max_seconds):
        positions = simulate_robots(robots, t)
        x_coords = [x for x, _ in positions.keys()]
        y_coords = [y for _, y in positions.keys()]

        # Check if bounding box is small enough to indicate alignment
        if x_coords and y_coords and max(x_coords) - min(x_coords) < threshold and max(y_coords) - min(y_coords) < threshold:
            return t

    return -1  # No alignment found within the time limit

if __name__ == "__main__":
    input_file = r"D:\Programming\Advent Of Code 2024\Day 14\input.txt"
    
    try:
        # Parse input
        robots = parse_input(input_file)

        # Part 1: Compute Safety Factor after 100 seconds
        seconds = 100
        positions = simulate_robots(robots, seconds)

        # Initialize quadrant counts
        q1 = q2 = q3 = q4 = 0

        for (x, y), count in positions.items():
            # Skip robots on the axes
            if x == GRID_WIDTH // 2 or y == GRID_HEIGHT // 2:
                continue
            if x > GRID_WIDTH // 2 and y < GRID_HEIGHT // 2:
                q1 += count
            elif x < GRID_WIDTH // 2 and y < GRID_HEIGHT // 2:
                q2 += count
            elif x < GRID_WIDTH // 2 and y > GRID_HEIGHT // 2:
                q3 += count
            elif x > GRID_WIDTH // 2 and y > GRID_HEIGHT // 2:
                q4 += count

        safety_factor = q1 * q2 * q3 * q4
        print(f"Safety Factor after 100 seconds: {safety_factor}")

        # Part 2: Find the alignment time
        alignment_time = find_alignment_time(robots)

        if alignment_time != -1:
            print(f"Fewest number of seconds for alignment: {alignment_time}")
        else:
            print("No alignment found within the time limit.")
    except Exception as e:
        print(e)
