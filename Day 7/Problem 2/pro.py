from itertools import product

def evaluate_equation(numbers, operators):
    """
    Evaluate the equation formed by inserting the operators (+, *, ||) into the numbers list.
    Operators are evaluated left-to-right, ignoring mathematical precedence.
    """
    expression = str(numbers[0])  # Start with the first number as a string
    for i in range(len(operators)):
        if operators[i] == '+':
            expression = str(int(expression) + numbers[i + 1])
        elif operators[i] == '*':
            expression = str(int(expression) * numbers[i + 1])
        elif operators[i] == '||':
            expression += str(numbers[i + 1])  # Concatenate the numbers as strings
    return int(expression)  # Convert the final result back to an integer

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
    Determine which equations can be made true by inserting +, *, or || operators.
    """
    total_calibration = 0

    for test_value, numbers in equations:
        num_positions = len(numbers) - 1  # Number of operator positions
        found_solution = False

        # Generate all combinations of +, *, and || operators for the given positions
        for ops in product(['+', '*', '||'], repeat=num_positions):
            try:
                if evaluate_equation(numbers, ops) == test_value:
                    total_calibration += test_value
                    found_solution = True
                    break
            except Exception:
                continue  # Skip invalid evaluations

    return total_calibration

def main():
    input_file = "input.txt"
    output_file = "output.txt"

    # Read input data
    equations = parse_input(input_file)
    
    # Calculate the result
    result = find_solvable_equations(equations)
    
    # Write result to output file
    with open(output_file, 'w') as file:
        file.write(str(result) + '\n')
    
    print(f"Total Calibration Result written to {output_file}")

if __name__ == "__main__":
    main()
