def is_safe(report):
    # Check if the report is increasing or decreasing with valid differences
    increasing = all(1 <= report[i + 1] - report[i] <= 3 for i in range(len(report) - 1))
    decreasing = all(1 <= report[i] - report[i + 1] <= 3 for i in range(len(report) - 1))
    return increasing or decreasing

# File paths
input_file = "input.txt"
output_file = "output.txt"

# Read and process input
with open(input_file, "r") as f:
    reports = [list(map(int, line.strip().split())) for line in f]

# Count safe reports
safe_count = sum(1 for report in reports if is_safe(report))

# Write the result to the output file
with open(output_file, "w") as f:
    f.write(f"Total safe reports: {safe_count}\n")

print(f"Results have been written to {output_file}")
