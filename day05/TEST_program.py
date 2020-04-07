# PART ONE -------------------------------------------------------------------------------
#   - Ajout des parameter modes + notation alternative du optcode si paramètres
#   - Ajout de deux nouveaux optcodes (3 et 4)

# PART TWO -------------------------------------------------------------------------------
#   - Ajout de quatre nouveaux optcode (5, 6, 7 et 8)


# *** Pour utiliser le fichier texte telquel ********************************************
program = list()
fresh_program = list()

id_to_verify = int(input('Please enter the ID of the system to test  --->  '))
if id_to_verify == 1 or id_to_verify == 5:
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
    # Variable pour les tests seulement
    number_to_test = 9999
    while initial_position < len(program) - 1:
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

        # *** Regroupement des optcode qui prennent deux où plus paramètres
        # OPTCODE 1, 2, 5, 6, 7, 8 --------------------------------------------------------------------------------
        if optcode != 3 and optcode != 4 and optcode != 99:
            # Vérification de la liste des modes des paramètres pour mette la valeur correspondante
            if len(parameter_list) != 0 and parameter_list[0] == 1:
                input_value1 = int(program[initial_position + 1])
            else:
                abs_position = abs(program[initial_position + 1])
                input_value1 = int(program[abs_position])

            if len(parameter_list) != 0 and parameter_list[1] == 1:
                input_value2 = int(program[initial_position + 2])
            else:
                abs_position = abs(program[initial_position + 2])
                input_value2 = int(program[abs_position])

            # OPTCODE 1, 2, 7 & 8 --------------------------------------------------------------------------------
            if optcode != 5 and optcode != 6:
                output_position = program[initial_position + 3]
                # OPTCODE 1 --------------------------------------------------------------------------------
                if optcode == 1:
                    program[output_position] = input_value1 + input_value2

                # OPTCODE 2 --------------------------------------------------------------------------------
                elif optcode == 2:
                    program[output_position] = input_value1 * input_value2

                # OPTCODE 7 --------------------------------------------------------------------------------
                elif optcode == 7:
                    # if first parameter is less than the second, stores 1 in value of output_position
                    if input_value1 < input_value2:
                        program[output_position] = 1
                    # else, stores 0
                    else:
                        program[output_position] = 0

                # OPTCODE 8 --------------------------------------------------------------------------------
                elif optcode == 8:
                    # if first parameter is equal to the second, stores 1 in value of output_position
                    if input_value1 == input_value2:
                        program[output_position] = 1
                    # else, stores 0
                    else:
                        program[output_position] = 0

                # Add jump to next instruction
                initial_position += 4

            # OPTCODE 5 --------------------------------------------------------------------------------
            elif optcode == 5:
                # if first parameter is different than 0, changes initial_position to value of 2nd parameter
                if input_value1 != 0:
                    initial_position = int(input_value2)
                # else, does nothing (skips ahead equivalent of the optcode + 2 parameters
                else:
                    initial_position += 3

            # OPTCODE 6 --------------------------------------------------------------------------------
            elif optcode == 6:
                # if first parameter is equal to 0, changes initial_position to value of 2nd parameter
                if input_value1 == 0:
                    initial_position = int(input_value2)
                # else, does nothing (skips ahead equivalent of the optcode + 2 parameters
                else:
                    initial_position += 3

        # OPTCODE 3 --------------------------------------------------------------------------------
        elif optcode == 3:
            output_position = program[initial_position + 1]
            new_input = input("Please enter new number to be memorised: ---> ")
            program[output_position] = int(new_input)
            # Add jump to next instruction
            initial_position += 2

        # OPTCODE 4 --------------------------------------------------------------------------------
        elif optcode == 4:
            # Vérification de la liste des modes des paramètres pour mette la valeur correspondante
            if len(parameter_list) != 0 and parameter_list[0] == 1:
                number_to_output = program[initial_position + 1]
            else:
                number_to_output = int(program[program[initial_position + 1]])
            number_to_test = number_to_output
            print(number_to_output)
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

    # return program
    # return number_to_test


test_program(program)
