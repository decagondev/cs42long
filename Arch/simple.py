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


HLT = 0b00000001
LDI = 0b10000010

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



    elif instruction == HALT:
        # execute
        running = False
        sys.exit(0)
    
    else:
        print("Invalid Instruction")
        sys.exit(1)

