# PART TWO ------------------------------------------------------------------------------
program = list()

with open("input_day2.txt", "r") as inputFile:
    for line in inputFile:
        number = ""
        for word in line:
            if word != "," and word != "\n":
                number += word
            else:
                program.append(int(number))
                number = ""


def rebuilt_intcode_program(program):

    for i_noun in range(100):
        for i_verb in range(100):
            # On duplique le programme initial (pour toujours partir à neuf)
            program_double = program[:]
            # On remplace les valeurs des positions 1 et 2 par les variables des compteurs
            # Les boucles imbriquées nous donneront toutes les combinaisons possibles entre 0 et 99
            program_double[1] = i_noun
            program_double[2] = i_verb

            initial_position = 0

            while initial_position < len(program_double)-3:
                optcode = program_double[initial_position]
                input_value1 = program_double[program_double[initial_position + 1]]
                input_value2 = program_double[program_double[initial_position + 2]]
                output_position = program_double[initial_position+3]

                if optcode == 1:
                    # Time to add
                    program_double[output_position] = input_value1 + input_value2
                    initial_position += 4
                elif optcode == 2:
                    # Time to multiply
                    program_double[output_position] = input_value1 * input_value2
                    initial_position += 4
                elif optcode == 99:
                    # Time to end the program
                    # print("We've met a 99! initial_position = {}".format(initial_position))
                    break
                else:
                    # ERROR!
                    print("An error has occurred. Input " + str(program_double[initial_position]) + " is not recognised.")
                    break
            if program_double[0] == 19690720:
                return list({i_noun, i_verb})


noun_verb_couple = rebuilt_intcode_program(program)
print(noun_verb_couple)
answer = 100 * noun_verb_couple[1] + noun_verb_couple[0]
print(answer)
