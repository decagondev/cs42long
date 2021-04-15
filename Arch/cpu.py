"""CPU functionality."""

import sys

LDI = 0b10000010
PRN = 0b01000111
PRA  = 0b01001000
HLT = 0b00000001
POP  = 0b01000110
PUSH = 0b01000101
ADD  = 0b10100000
SUB  = 0b10100001
MUL  = 0b10100010
DIV  = 0b10100011
CALL = 0b01010000
RET = 0b00010001

SP = 7

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.pc = 0
        self.reg = [0] * 8
        self.ram = [0] * 256
        self.reg[7] = 0xf4

        self.sets_pc = False

        self.running = False
    

    # Helper Methods
    def ram_read(self, mar):
        return self.ram[mar]

    def ram_write(self, mar, mdr):
        self.ram[mar] = mdr

    def push_val(self, val):
        self.reg[SP] -= 1
        self.ram_write(self.reg[7], val)
        
    def pop_val(self):
        val = self.ram[self.reg[7]]
        self.reg[SP] += 1

        return val

    def load(self, filename):
        """Load a program into memory."""

        address = 0
        with open(filename) as fp:
            for line in fp:

                # split the line on the hash sign
                comment_split = line.split("#")

                # strip the whitespace on element zero (the instruction)
                num = comment_split[0].strip()

                if num == '':  # ignore blanks
                    continue

                # turn the number string in to an integer
                val = int(num, 2)
                # print(val)

                self.ram_write(address, val)
                address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        elif op == "SUB":
            self.reg[reg_a] -= self.reg[reg_b]
        elif op == "MUL":
            self.reg[reg_a] *= self.reg[reg_b]
        elif op == "DIV":
            self.reg[reg_a] /= self.reg[reg_b]
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        # running loop
        self.running = True

        while self.running:
            # fetch
            ir = self.ram[self.pc]
            opa = self.ram[self.pc + 1]
            opb = self.ram[self.pc + 2]
            self.sets_pc = ((ir >> 4) & 0b1) == 1

            # decode instruction size
            opcode_size = (ir >> 6) + 1

            
            # decode
            if ir == HLT:
                # execute
                self.running = False
                sys.exit(0)
            
            # decode
            elif ir == LDI:
                # execute
                # get the reg index.
                reg_index = opa
                # get the num.
                num = opb
                # put the number in the registers list at the index of reg_index
                self.reg[reg_index] = num

            # elif ir == PUSH:
            #     # print("PUSH")

            #     # Decrement the Stack Pointer
            #     self.reg[SP] -= 1

            #     # Copy the value at the given register to the address in memory pointed to by the Stack Pointer.
            #     self.ram[self.reg[SP]] = self.reg[opa]

            elif ir == ADD:
                self.alu("ADD", opa, opb)

            elif ir == SUB:
                self.alu("SUB", opa, opb)
            
            elif ir == MUL:
                self.alu("MUL", opa, opb)

            elif ir == DIV:
                self.alu("MUL", opa, opb)

            elif ir == PUSH:
                self.push_val(self.reg[opa])

            elif ir == POP:
                self.reg[opa] = self.pop_val()

            elif ir == CALL:
                self.push_val(self.pc + 2)
                self.pc = self.reg[opa]

            elif ir == RET:
                self.pc = self.pop_val()

                

            # decode
            elif ir == PRN:
                # execute
                # get reg index.
                reg_index = opa
                print(self.reg[reg_index])

            elif ir == PRA:
                print(chr(self.reg[opa]), end='')
           

            # decode
            else:
                print(f"Unknown instruction {ir}")
                sys.exit(1)

            if not self.sets_pc:
                self.pc += opcode_size
            else:
                pass

if __name__ == "__main__":
    
    """Main."""

    import sys

    cpu = CPU()

    cpu.load()
    cpu.run()