from os import path

# positions_memory = [0, 0, 0, 0, 0]
# phase_1_done = [False, False, False, False, False]


def create_program(text_file):
    program = list()
    if path.exists(text_file):
        with open(text_file, "r") as inputFile:
            for line in inputFile:
                number = ""
                for word in line:
                    if word != "," and word != "\n":
                        number += word
                    else:
                        program.append(int(number))
                        number = ""
    else:
        program = text_file
    return program


def test_program(program, *args):
    if args:
        initial_position = args[3]
    else:
        initial_position = 0

    # Variable si vérification des amp (day07)
    skip_to_next_program = False
    all_done = False

    number_to_test = 0

    while initial_position < len(program):
        if skip_to_next_program:
            break

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
                    # print("optcode 1 -> adding both values")
                    program[output_position] = input_value1 + input_value2

                # OPTCODE 2 --------------------------------------------------------------------------------
                elif optcode == 2:
                    # print("optcode 2 -> multiplying both values")
                    program[output_position] = input_value1 * input_value2

                # OPTCODE 7 --------------------------------------------------------------------------------
                elif optcode == 7:
                    # if first parameter is less than the second, stores 1 in value of output_position
                    if input_value1 < input_value2:
                        # print("optcode 7 -> 1rst < 2nd, storing 1")
                        program[output_position] = 1
                    # else, stores 0
                    else:
                        # print("optcode 7 -> 1rst >= 2nd, storing 0")
                        program[output_position] = 0

                # OPTCODE 8 --------------------------------------------------------------------------------
                elif optcode == 8:
                    # if first parameter is equal to the second, stores 1 in value of output_position
                    if input_value1 == input_value2:
                        # print("optcode 8 -> equal values, storing 1")
                        program[output_position] = 1
                    # else, stores 0
                    else:
                        # print("optcode 8 -> values not equal, storing 0")
                        program[output_position] = 0

                # Add jump to next instruction
                initial_position += 4

            # OPTCODE 5 --------------------------------------------------------------------------------
            elif optcode == 5:
                # if first parameter is different than 0, changes initial_position to value of 2nd parameter
                if input_value1 != 0:
                    if args:
                        current_phase_setting = int(args[0])
                        if current_phase_setting in [5, 6, 7, 8, 9] and number_to_test != 0:
                            # print("optcode 5 -> leaving this program")
                            initial_position = int(input_value2)
                            skip_to_next_program = True
                        else:
                            # print("optcode 5 -> change initial position to 2nd parameter, phase between 5 and 9")
                            initial_position = int(input_value2)
                    else:
                        # print("optcode 5 -> change initial position to 2nd parameter")
                        initial_position = int(input_value2)
                # else, does nothing (skips ahead equivalent of the optcode + 2 parameters
                else:
                    # print("optcode 5 -> initial position += 3")
                    initial_position += 3

            # OPTCODE 6 --------------------------------------------------------------------------------
            elif optcode == 6:
                # if first parameter is equal to 0, changes initial_position to value of 2nd parameter
                if input_value1 == 0:
                    # print("optcode 6 -> initial position = 2nd parameter")
                    initial_position = int(input_value2)
                # else, does nothing (skips ahead equivalent of the optcode + 2 parameters
                else:
                    # print("optcode 6 -> initial position += 3")
                    initial_position += 3

        # OPTCODE 3 --------------------------------------------------------------------------------
        elif optcode == 3:
            # print("optcode 3 -> new input")
            output_position = program[initial_position + 1]
            if args:
                current_phase_setting = int(args[0])
                amp_input_signal = int(args[1])
                if initial_position < 4:
                    new_input = current_phase_setting
                else:
                    new_input = amp_input_signal
            else:
                new_input = input("Please enter new number to be memorised: ---> ")

            program[output_position] = int(new_input)
            # Add jump to next instruction
            initial_position += 2

        # OPTCODE 4 --------------------------------------------------------------------------------
        elif optcode == 4:
            # print("optcode 4 -> output")
            # Vérification de la liste des modes des paramètres pour mette la valeur correspondante
            if len(parameter_list) != 0 and parameter_list[0] == 1:
                number_to_output = program[initial_position + 1]
            else:
                number_to_output = int(program[program[initial_position + 1]])
                # print(f"Number to output : {number_to_output}")
            number_to_test = number_to_output
            # Add jump to next instruction
            initial_position += 2
            break

        # OPTCODE 99 --------------------------------------------------------------------------------
        elif optcode == 99:
            # print("optcode 99 -> out")
            if args:
                number_to_test = args[1]
                # print(args[2])
                if args[2] == 4:
                    all_done = True

            # Time to end the program
            break

        else:
            # ERROR!
            print("An error has occurred. Input " + str(program[initial_position]) + " is not recognised.")
            break

    # input("The current result is : " + str(number_to_test) + ". Continue? (y) ----> ")
    # print("out of the program")
    return number_to_test, all_done, program, initial_position
