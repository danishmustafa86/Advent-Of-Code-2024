def count_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    word = "XMAS"
    word_len = len(word)
    directions = [
        (0, 1), (0, -1),  # Horizontal
        (1, 0), (-1, 0),  # Vertical
        (1, 1), (-1, -1), # Diagonal (top-left to bottom-right)
        (1, -1), (-1, 1)  # Diagonal (top-right to bottom-left)
    ]
    
    count = 0
    
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    # Iterate through each cell in the grid
    for r in range(rows):
        for c in range(cols):
            # Check if this cell can be the starting point for "XMAS"
            for dx, dy in directions:
                found = True
                for k in range(word_len):
                    nr, nc = r + k * dx, c + k * dy
                    if not is_valid(nr, nc) or grid[nr][nc] != word[k]:
                        found = False
                        break
                if found:
                    count += 1

    return count

# Main function to handle file I/O
def main():
    # Read input from input.txt
    with open("input.txt", "r") as file:
        grid = [line.strip() for line in file.readlines()]
    
    # Count occurrences of XMAS
    result = count_xmas(grid)
    
    # Write output to output.txt
    with open("output.txt", "w") as file:
        file.write(str(result) + "\n")

if __name__ == "__main__":
    main()
