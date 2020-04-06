# PART ONE -------------------------------------------------------------------------------

# *** Pour utiliser le fichier texte telquel ********************************************
program = list()
fresh_program = list()

id_to_verify = int(input('Please enter the ID of the system to test  --->  '))
if id_to_verify == 1:
    with open("input_day5.txt", "r") as inputFile:
        for line in inputFile:
            number = ""
            for word in line:
                if word != "," and word != "\n":
                    number += word
                else:
                    program.append(int(number))
                    fresh_program.append(int(number))
                    number = ""


def test_program(program):
    initial_position = 0
    while initial_position < len(program)-4:
        optcode = program[initial_position]
        parameter_list = list()

        # Ajout pour séparer les optcode et les mode des paramètres, si nécessaire
        if len(str(optcode)) != 1:
            parameters = str(optcode)[:-2]
            optcode = int(str(optcode)[-2:])
            for parameter in parameters:
                parameter_list.insert(0, int(parameter))
            while len(parameter_list) != 3:
                parameter_list.append(0)

        # Vérification du optcode correspondant
        # OPTCODE 1 & 2 --------------------------------------------------------------------------------
        if optcode == 1 or optcode == 2:
            # Vérification de la liste des modes des paramètres pour mette la valeur correspondante
            if len(parameter_list) != 0 and parameter_list[0] == 1:
                input_value1 = program[initial_position + 1]
            else:
                abs_position = abs(program[initial_position + 1])
                input_value1 = int(program[abs_position])

            if len(parameter_list) != 0 and parameter_list[1] == 1:
                input_value2 = program[initial_position + 2]
            else:
                abs_position = abs(program[initial_position + 2])
                input_value2 = int(program[abs_position])

            output_position = program[initial_position + 3]

            if optcode == 1:
                program[output_position] = input_value1 + input_value2
            elif optcode == 2:
                program[output_position] = input_value1 * input_value2

            # Add jump to next instruction
            initial_position += 4

        # OPTCODE 3 --------------------------------------------------------------------------------
        elif optcode == 3:
            output_position = program[initial_position + 1]
            new_input = input("Please enter new number to be memorised: ---> ")
            program[output_position] = new_input
            # Add jump to next instruction
            initial_position += 2

        # OPTCODE 4 --------------------------------------------------------------------------------
        elif optcode == 4:
            # Vérification de la liste des modes des paramètres pour mette la valeur correspondante
            if len(parameter_list) != 0 and parameter_list[0] == 1:
                number_to_output = program[initial_position + 1]
            else:
                number_to_output = int(program[program[initial_position + 1]])

            print(str(number_to_output))
            # Add jump to next instruction
            initial_position += 2

        # OPTCODE 99 --------------------------------------------------------------------------------
        elif optcode == 99:
            # Time to end the program
            break

        else:
            # ERROR!
            print("An error has occurred. Input " + str(program[initial_position]) + " is not recognised.")
            break

    return program


test_program(program)
