import yaml
import re

def validate_bit_ranges(opcode, details):
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

def validate_arguments(opcode, details, argument_lookup):
    args = re.findall(r'{(\w+)}', details['format'])
    for arg in args:
        if arg not in argument_lookup:
            print(f"Error in {opcode}: Argument '{arg}' not found in argument lookup table.")
            return False
    return True

def validate_opcode(yaml_file, argument_lookup):
    with open(yaml_file, 'r') as file:
        opcodes = yaml.safe_load(file)

    for opcode, details in opcodes.items():
        print(f"Validating opcode: {opcode}")

        if not validate_bit_ranges(opcode, details):
            return False

        if not validate_arguments(opcode, details, argument_lookup):
            return False

    print("All opcodes are valid")
    return True

# I created an example look-up table to test code
argument_lookup = {
    'rs1': 'Source register 1',
    'rs2': 'Source register 2',
    'rd': 'Destination register',
    'imm': 'Immediate value',
}

# Usage
if validate_opcode('opcodes.yaml', argument_lookup):
    print("Validation successful.")
else:
    print("Validation failed.")
