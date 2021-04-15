import sys

filename = ""

if len(sys.argv) != 2:
    print("Usage: python3 fileio.py <filename>")
    sys.exit(1)
else:
    filename = sys.argv[1]




# instruction set
HALT = 0
PRINT_BOB = 1
PRINT_NUM = 2
LOAD_REG = 3
PRINT_REG = 4
ADD = 6
MUL = 7
SUB = 8
PUSH = 9
POP = 10
CALL = 11
RET = 12


HLT = 0b00000001
LDI = 0b10000010
# PUSH = 0b01000101
# POP = 0b01000110

ram = [0] * 256 # primary memory
# ram = []
def load_prog(filename):
    try:
        address = 0 # ram address
        with open(filename) as f:
            for line in f:
                comment_split = line.split("#")
                num = comment_split[0].strip()
                if num == '':
                    continue

                ram[address] = int(num)
                address += 1
                
    except FileNotFoundError:
        print("file not found")
        sys.exit(2)

load_prog(filename)

def alu(op, opera, operb):
    if op == "ADD":
        registers[rega_index] += registers[regb_index]
        pc += 3
    elif op == "MUL":
        registers[rega_index] *= registers[regb_index]
        pc += 3
    elif op == "SUB":
        registers[rega_index] -= registers[regb_index]
        pc += 3

# cpu
running = True
pc = 0 # program counter index in to the ram to fetch and instruction

registers = [0] * 8 # the actual registers inside the cpu
sp = 7 # R7 === the actual stack pointer

# set our stack pointer to point at 0xf4
registers[sp] = 0xf4

# fetch decode execute cycle
while running:
    # fetch an instruction
    instruction = ram[pc]

    # decode
    if instruction == PRINT_BOB:
        # excute
        print("Bob")
        pc += 1

    elif instruction == PRINT_NUM:
        # excute
        num = ram[pc + 1]
        print(num)
        pc += 2
    
    elif instruction == LOAD_REG:
        reg_index = ram[pc + 1]
        num = ram[pc + 2]
        registers[reg_index] = num
        pc += 3

    elif instruction == PRINT_REG: # prn
        reg_index = ram[pc + 1]
        num = registers[reg_index]
        print(num)
        pc += 2

    elif instruction == ADD:
        rega_index = ram[pc + 1]
        regb_index = ram[pc + 2]
        alu("ADD", rega_index, regb_index)
        # registers[rega_index] += registers[regb_index]
        # pc += 3

    elif instruction == MUL:
        rega_index = ram[pc + 1]
        regb_index = ram[pc + 2]
        alu("MUL", rega_index, regb_index)
        # registers[rega_index] *= registers[regb_index]
        # pc += 3

    elif instruction == SUB:
        rega_index = ram[pc + 1]
        regb_index = ram[pc + 2]
        alu("SUB", rega_index, regb_index)
        # registers[rega_index] *= registers[regb_index]
        # pc += 3
    
    elif instruction == PUSH:
        reg_index = ram[pc + 1]
        val = registers[reg_index]
        # decrement stack pointer
        registers[sp] -= 1
        # set the ram at the address pointed to by the stack pointer to the value
        ram[registers[sp]] = val
        pc += 2
    
    elif instruction == POP:
        reg_index = ram[pc + 1]
        # set the given reg to the value at the ram address pointed to by the stack pointer
        registers[reg_index] = ram[registers[sp]]

        # increment the stack pointer
        registers[sp] += 1
        pc += 2

    elif instruction == HALT:
        # execute
        running = False
        sys.exit(0)

    elif instruction == CALL:
        # 1. push the address of the next instruction on to the stack
        address_to_return_to = pc + 2
        # decrement stack pointer
        registers[sp] -= 1
        # set the ram at the address pointed to by the stack pointer to the value
        ram[registers[sp]] = address_to_return_to
        
        # 2. set the pc to the address stored in the given register
        reg_index = ram[pc + 1]
        address_to_call = registers[reg_index]
        pc = address_to_call
    
    elif instruction == RET:
        pc = ram[registers[sp]]
        registers[sp] += 1

    else:
        print("Invalid Instruction")
        sys.exit(1)

