from os import path
import itertools

from modules import intcode_computer

program_file = "day07/input_day7.txt"

# On crée une liste de toutes les posibilités à vérifier
possible_numbers = [0, 1, 2, 3, 4]
if not path.exists('day07/combinations.txt'):
    all_combinations = list()
    for c in itertools.permutations(possible_numbers, 5):
        combination = str(c).replace("(", "").replace(")", "")
        combination = combination.split(", ")
        intcpt = 0
        for number in combination:
            combination[intcpt] = int(number)
            intcpt += 1
        all_combinations.append(combination)
    with open("day07/combinations.txt", "w+") as combinations:
        combinations.write(str(all_combinations))
else:
    with open("day07/combinations.txt", "r") as combinations:
        all_combinations = eval(combinations.read())


def find_max_thruster_signal(text_file, list_combinations):
    highest_thruster_signal = 0
    all_amp_programs = list()
    for i in range(0, 5):
        # pour tests
        # all_amp_programs.append(text_file)
        # pour vrai
        all_amp_programs.append(intcode_computer.create_program(text_file))

    # *** max_thruster_signal correspond au output final de l'amp E, une fois passé par tous les autres
    max_thruster_signal = ""
    for one_combination in list_combinations:
        amp_output = 0
        loops = 0
        for one_number in one_combination:
            amp_output = intcode_computer.test_program(all_amp_programs[loops], one_number, amp_output)
            # max_thruster_signal = max_thruster_signal + str(amp_output)
            max_thruster_signal = amp_output
            loops += 1

        if max_thruster_signal > highest_thruster_signal:
            highest_thruster_signal = max_thruster_signal

    return highest_thruster_signal


print(find_max_thruster_signal(program_file, all_combinations))


