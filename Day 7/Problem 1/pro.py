# import itertools

# inputfile = "input.txt"
# outputfile = "output.txt"

# # Parse the input file
# with open(inputfile, "r") as file:
#     arr = [line.strip().split(": ") for line in file.readlines()]
#     hsh = {int(line[0]): list(map(int, line[1].split())) for line in arr}

# # Function to check if a given sequence of numbers and operators produces the target value
# def evaluate_expression(numbers, operators):
#     result = numbers[0]
#     for i, op in enumerate(operators):
#         if op == '+':
#             result += numbers[i + 1]
#         elif op == '*':
#             result *= numbers[i + 1]
#     return result

# # Calculate the total calibration result
# ansSum = 0
# for target, numbers in hsh.items():
#     n = len(numbers) - 1  # Number of operator positions
#     valid = False
    
#     # Try all possible combinations of + and * operators
#     for ops in itertools.product("+-*", repeat=n):
#         if evaluate_expression(numbers, ops) == target:
#             valid = True
#             break
    
#     # Add to total sum if the equation is valid
#     if valid:
#         ansSum += target

# # Write the output to the file
# with open(outputfile, "w") as file:
#     file.write(str(ansSum))

# print("Total Calibration Result:", ansSum)























from itertools import product

def evaluate_equation(numbers, operators):
    """
    Evaluate the equation formed by inserting the operators into the numbers list.
    """
    expression = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            expression += numbers[i + 1]
        elif operators[i] == '*':
            expression *= numbers[i + 1]
    return expression

def parse_input(file_path):
    """
    Parse the input file to extract test values and number lists.
    """
    equations = []
    with open(file_path, 'r') as file:
        for line in file:
            if not line.strip():
                continue
            test_value, numbers = line.split(':')
            test_value = int(test_value.strip())
            numbers = list(map(int, numbers.strip().split()))
            equations.append((test_value, numbers))
    return equations

def find_solvable_equations(equations):
    """
    Determine which equations can be made true by inserting + or * operators.
    """
    total_calibration = 0

    for test_value, numbers in equations:
        num_positions = len(numbers) - 1
        found_solution = False

        # Generate all combinations of + and * operators for the given positions
        for ops in product(['+', '*'], repeat=num_positions):
            if evaluate_equation(numbers, ops) == test_value:
                total_calibration += test_value
                found_solution = True
                break

    return total_calibration

def main(input_file, output_file):
    equations = parse_input(input_file)
    result = find_solvable_equations(equations)
    
    # Write the result to the output file
    with open(output_file, 'w') as file:
        file.write(f"{result}\n")
    
    print(f"Total Calibration Result written to {output_file}")

if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output.txt"
    main(input_file, output_file)
