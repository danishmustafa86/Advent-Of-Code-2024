def is_safe(report):
    """
    Checks if a report is safe without any modifications.
    A report is safe if all numbers are either consistently increasing
    or consistently decreasing with differences between 1 and 3.
    """
    inc, dec = 0, 0
    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        if not 1 <= diff <= 3:
            inc += 1
        if not 1 <= -diff <= 3:
            dec += 1
    return inc <= 0 or dec <= 0

def is_safe_with_dampener(report):
    """
    Checks if a report can be made safe by removing one level.
    Tries removing each level and checks if the modified report is safe.
    """
    # If the report is already safe, return True
    if is_safe(report):
        return True
    
    # Try removing each level and check if the resulting report is safe
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]  # Remove the i-th level
        if is_safe(modified_report):
            return True
    
    # If no single removal makes the report safe, return False
    return False

# File paths
input_file = "input.txt"
output_file = "output.txt"

# Read and process input
with open(input_file, "r") as f:
    reports = [list(map(int, line.strip().split())) for line in f]

# Count safe reports, including those made safe by the Problem Dampener
safe_count = sum(1 for report in reports if is_safe_with_dampener(report))

# Write the result to the output file
with open(output_file, "w") as f:
    f.write(f"Total safe reports: {safe_count}\n")

print(f"Results have been written to {output_file}")
