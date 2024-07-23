#USING OOP CONCEPTS

import yaml
import re

class OpcodeValidator:
    def __init__(self, yaml_file, argument_lookup):
        self.yaml_file = yaml_file
        self.argument_lookup = argument_lookup
        self.opcodes = self.load_opcodes()

    def load_opcodes(self):
        with open(self.yaml_file, 'r') as file:
            return yaml.safe_load(file)

    def validate_bit_ranges(self, opcode, details):
        encoding = ['-'] * 32
        for match in re.findall(r'(\d+)\.\.(\d+)=(\d+)', details['encoding']):
            msb, lsb, value = int(match[0]), int(match[1]), int(match[2])
            if msb < lsb:
                print(f"Error in {opcode}: MSB ({msb}) is less than LSB ({lsb}).")
                return False
            if value >= (1 << (msb - lsb + 1)):
                print(f"Error in {opcode}: Value ({value}) exceeds the range for bits {msb}..{lsb}.")
                return False
            for ind in range(lsb, msb + 1):
                if encoding[31 - ind] != '-':
                    print(f"Error in {opcode}: Overlapping bits in range {msb}..{lsb}.")
                    return False
                encoding[31 - ind] = str((value >> (ind - lsb)) & 1)
        return True

    def validate_arguments(self, opcode, details):
        args = re.findall(r'{(\w+)}', details['format'])
        for arg in args:
            if arg not in self.argument_lookup:
                print(f"Error in {opcode}: Argument '{arg}' not found in argument lookup table.")
                return False
        return True

    def validate_opcodes(self):
        for opcode, details in self.opcodes.items():
            print(f"Validating opcode: {opcode}")

            if not self.validate_bit_ranges(opcode, details):
                return False

            if not self.validate_arguments(opcode, details):
                return False

        print("All opcodes are valid")
        return True

argument_lookup = {
    'rs1': 'Source register 1',
    'rs2': 'Source register 2',
    'rd': 'Destination register',
    'imm': 'Immediate value',
}

validator = OpcodeValidator('opcodes.yaml', argument_lookup)
if validator.validate_opcodes():
    print("Validation successful.")
else:
    print("Validation failed.")
