def read_input_file(file_path):
    """Reads input data from a file and returns two lists."""
    l1, l2 = [], []
    with open(file_path, 'r') as file:
        for line in file:
            nums = list(map(int, line.strip().split()))
            l1.append(nums[0])  # First number goes to l1
            l2.append(nums[1])  # Second number goes to l2
    return l1, l2

def write_output_file(file_path, output):
    """Writes the result to an output file."""
    with open(file_path, 'w') as file:
        file.write(f"Result: {output}\n")

def fun(l1, l2):
    """Calculates the sum of absolute differences between two sorted lists."""
    ans = []
    for i in range(len(l1)):
        ans.append(abs(l1[i] - l2[i]))
    return sum(ans)

# File paths
input_file = 'input.txt'  # Replace with your input file path
output_file = 'output.txt'  # Replace with your desired output file path

# Read input
l1, l2 = read_input_file(input_file)

# Sort the lists
l1.sort()
l2.sort()

# Calculate the result
result = fun(l1, l2)

# Write the result
write_output_file(output_file, result)
