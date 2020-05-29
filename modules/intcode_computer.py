from os import path


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
    initial_position = 0
    relative_position = 0
    if args:
        if args[0] == 'day07':
            initial_position = args[4]

    # Variable si vérification des amp (day07)
    skip_to_next_program = False
    all_done = False

    number_to_test = 0

    while initial_position < len(program):
        if args:
            if args[0] == 'day07' and skip_to_next_program:
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
        if optcode in [1, 2, 5, 6, 7, 8]:
            # Vérification de la liste des modes des paramètres pour mette la valeur correspondante
            if len(parameter_list) != 0:
                # Valeurs selon le premier paramètre
                if parameter_list[0] == 1:
                    input_value1 = int(program[initial_position + 1])
                elif parameter_list[0] == 2:
                    abs_position = abs(relative_position + int(program[initial_position + 1]))
                    if len(program) < abs_position + 1:
                        program = add_index_list(program, abs_position + 1)
                    input_value1 = int(program[abs_position])
                else:
                    abs_position = abs(program[initial_position + 1])
                    if len(program) < abs_position + 1:
                        program = add_index_list(program, abs_position + 1)
                    input_value1 = int(program[abs_position])

                # Valeurs selon le deuxième paramètre
                if parameter_list[1] == 1:
                    input_value2 = int(program[initial_position + 2])
                elif parameter_list[1] == 2:
                    abs_position = abs(relative_position + int(program[initial_position + 2]))
                    if len(program) < abs_position + 1:
                        program = add_index_list(program, abs_position + 1)
                    input_value2 = int(program[abs_position])
                else:
                    abs_position = abs(program[initial_position + 2])
                    if len(program) < abs_position + 1:
                        program = add_index_list(program, abs_position + 1)
                    input_value2 = int(program[abs_position])

            # Valeurs par défault
            else:
                abs_position = abs(program[initial_position + 1])
                if len(program) < abs_position + 1:
                    program = add_index_list(program, abs_position + 1)
                input_value1 = int(program[abs_position])
                abs_position = abs(program[initial_position + 2])
                if len(program) < abs_position + 1:
                    program = add_index_list(program, abs_position + 1)
                input_value2 = int(program[abs_position])

            # OPTCODE 1, 2, 7 & 8 --------------------------------------------------------------------------------
            if optcode != 5 and optcode != 6:
                if len(parameter_list) != 0 and parameter_list[2] == 2:
                    output_position = relative_position + program[initial_position + 3]
                else:
                    output_position = program[initial_position + 3]

                if len(program) < output_position + 1:
                    program = add_index_list(program, output_position + 1)

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
                        if args[0] == 'day07':
                            current_phase_setting = int(args[1])
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
            if len(parameter_list) != 0 and parameter_list[0] == 2:
                abs_position = relative_position + int(program[initial_position + 1])
                if len(program) < abs_position + 1:
                    program = add_index_list(program, abs_position + 1)
                output_position = abs_position
            else:
                output_position = program[initial_position + 1]
            if args:
                new_input = 0
                if args[0] == 'day07':
                    current_phase_setting = int(args[1])
                    amp_input_signal = int(args[2])
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
            number_to_output = 0

            if len(parameter_list) != 0:
                if parameter_list[0] == 1:
                    number_to_output = program[initial_position + 1]
                elif parameter_list[0] == 2:
                    abs_position = relative_position + int(program[initial_position + 1])
                    number_to_output = int(program[abs_position])
            else:
                number_to_output = int(program[program[initial_position + 1]])
            number_to_test = number_to_output
            # *** SI PREMIER TEST DANS GENERAL_TESTS.PY
            # number_to_test = str(number_to_test)
            # number_to_test += str(number_to_output)

            # Add jump to next instruction
            initial_position += 2

            if args:
                break

        # OPTCODE 9 --------------------------------------------------------------------------------
        elif optcode == 9:
            # Vérification de la liste des modes des paramètres pour mette la valeur correspondante
            if len(parameter_list) != 0:
                if parameter_list[0] == 1:
                    # print("optcode 9 -> adding exact value of parameter to relative_position")
                    relative_position += program[initial_position + 1]
                elif parameter_list[0] == 2:
                    # print("optcode 9 -> adding value found at position relative_position + parameter, to relative_position")
                    abs_position = relative_position + int(program[initial_position + 1])
                    if len(program) < abs_position + 1:
                        program = add_index_list(program, abs_position + 1)
                    relative_position += int(program[abs_position])
                else:
                    # print("optcode 9 -> adding value found at position of parameter, to relative_position")
                    relative_position += int(program[program[initial_position + 1]])
            else:
                # print("optcode 9 -> adding value found at position of parameter, to relative_position")
                relative_position += int(program[program[initial_position + 1]])

            # Add jump to next instruction
            initial_position += 2

        # OPTCODE 99 --------------------------------------------------------------------------------
        elif optcode == 99:
            if args:
                if args[0] == 'day07':
                    number_to_test = args[2]
                    if args[3] == 4:
                        all_done = True

            # Time to end the program
            break

        else:
            # ERROR!
            print("An error has occurred. Input " + str(program[initial_position]) + " is not recognised.")
            break

        # input(f"The current variables are : value1 : {input_value1}, value2 : {input_value2}, output_position : {output_position}, value added : {program[output_position]}, current position : {initial_position}, and relative position : {relative_position}. Continue? (y) ----> ")

    if args:
        return number_to_test, all_done, program, initial_position
    else:
        return number_to_test


def add_index_list(program, new_index_range):
    # *** GESTION DES OUTPUT PLUS ÉLEVÉS QUE LE LENGTH ACTUEL
    addon_list = list()
    for i in range(0, ((new_index_range + 1) - len(program))):
        addon_list.append(0)
    program.extend(addon_list)

    return program
