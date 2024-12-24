import re

def process_instructions(input_file, output_file):
    # Step 1: Read input from the file
    with open(input_file, "r") as file:
        corrupted_memory = file.read()

    # Step 2: Initialize variables
    mul_enabled = True  # Initially, mul instructions are enabled
    results = []

    # Step 3: Updated regular expression to match do(), don't(), and mul(X, Y)
    pattern = r"(do\(\))|(don't\(\))|mul\((\d{1,3}),(\d{1,3})\)"

    # Step 4: Find all matches for mul, do, and don't instructions
    matches = re.findall(pattern, corrupted_memory)
    # print("Matches found:", matches)  # Debug print

    # Step 5: Process each match and handle the enabling/disabling of mul
    for match in matches:
        # match[0] = do(), match[1] = don't(), match[2] = mul num1, match[3] = mul num2
        if match[0]:  # do()
            # Enable future mul instructions
            mul_enabled = True
            print("Enabled mul instructions.")  # Debug print
        elif match[1]:  # don't()
            # Disable future mul instructions
            mul_enabled = False
            print("Disabled mul instructions.")  # Debug print
        elif match[2]:  # mul(X, Y)
            # Only process mul if enabled
            if mul_enabled:
                # Extract the numbers from the mul instruction and calculate the result
                num1 = int(match[2])
                num2 = int(match[3])
                result = num1 * num2
                results.append(result)
                print(f"Added {result} to results.")  # Debug print

    # Step 6: Calculate the sum of the results
    total_sum = sum(results)
    print("Total sum of multiplications:", total_sum)  # Debug print

    # Step 7: Write the output to the file
    with open(output_file, "w") as file:
        file.write(f"The total sum of all enabled multiplications is: {total_sum}\n")

    print("Result has been written to output.txt")

# Example usage
input_file = "input.txt"
output_file = "output.txt"
process_instructions(input_file, output_file)
