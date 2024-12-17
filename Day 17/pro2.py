def run_program(program, A_init):
    A, B, C = A_init, 0, 0
    pointer = 0
    output = []

    while pointer < len(program):
        opcode = program[pointer]
        operand = program[pointer + 1]
        pointer += 2

        if opcode == 0:  # adv
            denominator = 2 ** (operand if operand < 4 else [A, B, C][operand - 4])
            A //= denominator

        elif opcode == 1:  # bxl
            B ^= operand

        elif opcode == 2:  # bst
            B = operand % 8

        elif opcode == 3:  # jnz
            if A != 0:
                pointer = operand

        elif opcode == 4:  # bxc
            B ^= C

        elif opcode == 5:  # out
            output.append(operand % 8)

        elif opcode == 6:  # bdv
            denominator = 2 ** (operand if operand < 4 else [A, B, C][operand - 4])
            B = A // denominator

        elif opcode == 7:  # cdv
            denominator = 2 ** (operand if operand < 4 else [A, B, C][operand - 4])
            C = A // denominator

    return output

def find_correct_A(program):
    A = 1
    while True:
        output = run_program(program, A)
        if output == program:
            return A
        A += 1

# Example usage
program = [0, 3, 5, 4, 3, 0]
correct_A = find_correct_A(program)
print(f"The correct initial value for A is: {correct_A}")
