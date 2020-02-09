# PART ONE -------------------------------------------------------------------------------

# *** Pour tester ***********************************************************************
# testProgram = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
# program = testProgram.copy()
# Le copy fonctionne comme le slice, mais seulement dans python 3

# *** Pour utiliser le fichier texte telquel ********************************************
inputFile = open("input_day2.txt", "r")
program = list()
fresh_program = list()

for line in inputFile:
    number = ""
    for word in line:
        if word != "," and word != "\n":
            number += word
        else:
            program.append(int(number))
            fresh_program.append(int(number))
            number = ""

# *** Pour modifier les chiffres à la première et deuxième position *********************
program[1] = 12
program[2] = 2


def rebuilt_intcode_program(program):
    initial_position = 0
    while initial_position < len(program)-4:
        optcode = program[initial_position]
        input_value1 = program[program[initial_position + 1]]
        input_value2 = program[program[initial_position + 2]]
        output_position = program[initial_position+3]

        if optcode == 1:
            # Time to add
            program[output_position] = input_value1 + input_value2
            initial_position += 4
        elif optcode == 2:
            # Time to multiply
            program[output_position] = input_value1 * input_value2
            initial_position += 4
        elif optcode == 99:
            # Time to end the program
            break
        else:
            # ERROR!
            print("An error has occurred. Input " + str(program[initial_position]) + " is not recognised.")
            break

    return program


print(str(rebuilt_intcode_program(program)))



