from modules import intcode_computer

program_file = "day09/input_day9.txt"


def decode_sensorBoost():
    original_program = intcode_computer.create_program(program_file)
    boost_keycode = intcode_computer.test_program(original_program)

    return boost_keycode


print(decode_sensorBoost())
