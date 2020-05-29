from os import path
from itertools import cycle, permutations

from modules import intcode_computer

program_file = "day07/input_day7.txt"

# On crée une liste de toutes les posibilités à vérifier
# *** Possibilité pour le part 1
# possible_numbers = [0, 1, 2, 3, 4]
# *** Possibilité pour le part 2
possible_numbers = [5, 6, 7, 8, 9]
if not path.exists('day07/combinations.txt'):
    all_combinations = list()
    for c in permutations(possible_numbers, 5):
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
    combinations_checked = 0
    all_combinations = len(list_combinations)
    position_memory_og = [0, 0, 0, 0, 0]
    # *** max_thruster_signal correspond au output final de l'amp E, une fois passé par tous les autres
    original_program = intcode_computer.create_program(text_file)
    # original_program = text_file
    # print(original_program)

    for one_combination in list_combinations:
        # print('debut boucle combinaisons')
        position_memory = position_memory_og[:]
        all_amp_programs = list()
        for i in range(0, 5):
            # pour tests
            # all_amp_programs.append(text_file[:])
            # pour vrai
            all_amp_programs.append(original_program[:])
        loops = 0
        full_cycles = 0
        all_done = False

        while not all_done:
            amp_output = 0
            for one_number in cycle(one_combination):
                if loops == 5:
                    loops = 0
                    full_cycles += 1
                    # print(f"Full cycles : {full_cycles}")

                program_number = loops
                # print(amp_output)
                amp_output, all_done, new_program, position_memory[loops] = intcode_computer.test_program(all_amp_programs[loops], 'day07', one_number, amp_output, program_number, position_memory[loops])
                # On enregistre le programme en cours pour le réutiliser, si on est dans un contexte de feedback loop (part 2)
                all_amp_programs[loops] = new_program[:]
                # print(all_done)
                loops += 1
                if all_done:
                    # print('all_done!')
                    break

        max_thruster_signal = amp_output
        # print(f"max_thruster_signal = {max_thruster_signal}")

        if max_thruster_signal > highest_thruster_signal:
            highest_thruster_signal = max_thruster_signal

        combinations_checked += 1
        print(f"Checked {combinations_checked}/{all_combinations}")

    return highest_thruster_signal
    # return max_thruster_signal


answer = find_max_thruster_signal(program_file, all_combinations)
# answer = find_max_thruster_signal(program_file, [[5, 6, 7, 8, 9]])
# answer = find_max_thruster_signal(program_file, [[5, 6, 7, 8, 9], [5, 6, 7, 9, 8], [5, 6, 8, 7, 9], [5, 6, 8, 9, 7], [5, 6, 9, 7, 8], [5, 6, 9, 8, 7]])
print(answer)


