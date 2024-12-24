import re

# Step 1: Input and output file names
input_file = "input.txt"
output_file = "output.txt"

# Step 2: Read input from input.txt
with open(input_file, "r") as file:
    corrupted_memory = file.read()

# Step 3: Regular expression to find valid `mul(X,Y)`
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

# Step 4: Find all valid matches
matches = re.findall(pattern, corrupted_memory)

# Step 5: Compute the results of valid multiplications
results = [int(x) * int(y) for x, y in matches]

# Step 6: Calculate the sum of all results
total_sum = sum(results)

# Step 7: Write the result to output.txt
with open(output_file, "w") as file:
    file.write(f"The total sum of all valid multiplications is: {total_sum}\n")

print("Result has been written to output.txt")
