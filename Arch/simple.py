import sys
# instruction set
HALT = 0
PRINT_BOB = 1
PRINT_NUM = 2
LOAD_REG = 3
PRINT_REG = 4
ADD = 6

# ram = [0] * 256 # primary memory
ram = [
    PRINT_BOB, # 0
    PRINT_BOB, # 1
    PRINT_NUM, # 2
    120, # 3
    LOAD_REG, # 4
    0, # 5
    30, # 6
    LOAD_REG, # 4
    1, # 5
    20, # 6
    PRINT_REG, # 7
    0, # 8
    HALT # 9
]

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

    elif instruction == PRINT_REG:
        reg_index = ram[pc + 1]
        num = registers[reg_index]
        print(num)
        pc += 2

    elif instruction == ADD:
        rega_index = ram[pc + 1]
        regb_index = ram[pc + 2]
        registers[rega_index] += registers[regb_index]
        pc += 3



    elif instruction == HALT:
        # execute
        running = False
        sys.exit(0)
    
    else:
        print("Invalid Instruction")
        sys.exit(1)

