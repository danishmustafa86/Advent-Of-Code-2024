from collections import *
from functools import *
from itertools import *
from math import *
import re

def ints(s):
    return list(map(int, re.findall(r'-?\d+', s)))

# Initialize program with correct values
program = [2,4,1,7,7,5,0,3,1,7,4,1,5,5,3,0]  # Using the program from comment
ip = 0
A = 50230824
B = C = 0

def combo(x):
    if x == 0: return 0
    if x == 1: return 1
    if x == 2: return 2
    if x == 3: return 3
    if x == 4: return A
    if x == 5: return B
    if x == 6: return C
    return None

def step():
    global ip, A, B, C
    if ip >= len(program):
        raise IndexError("Program counter out of bounds")
    
    instr = program[ip]
    opcode = program[ip + 1]
    ip += 2
    
    try:
        if instr == 0:
            A = A // (2 ** combo(opcode))
        elif instr == 1:
            B = B ^ opcode
        elif instr == 2:
            B = combo(opcode) % 8
        elif instr == 3:
            if A != 0:
                ip = opcode
        elif instr == 4:
            B = B ^ C
        elif instr == 5:
            return combo(opcode) % 8
        elif instr == 6:
            B = A // (2 ** combo(opcode))
        elif instr == 7:
            C = A // (2 ** combo(opcode))
    except Exception as e:
        print(f"Error in instruction {instr} with opcode {opcode}: {e}")
        raise

def run(a):
    global A, B, C, ip
    ip = 0
    A = a
    B = 0
    C = 0
    result = []
    
    while ip < len(program):
        try:
            x = step()
            if x is not None:
                result.append(x)
        except IndexError:
            break
        except Exception as e:
            print(f"Error during execution with A={A}: {e}")
            break
    return result

def main():
    a = 35282534841844
    prev = 0
    count = 0
    target = [2,4,1,7,7,5,0,3,1,7,4,1,5,5,3,0]
    
    while count < 1000:  # Limit iterations to prevent infinite loop
        x = run(a)
        if x[:6] == [2, 4, 1, 2, 7, 5]:
            print(f"Found partial match: a={a}, len={len(x)}, diff={a-prev}, output={x}")
            prev = a
        if x == target:
            print(f"Found exact match at a={a}")
            return a
        a += 2097152
        count += 1
    print("No solution found within iteration limit")

if __name__ == "__main__":
    result = main()