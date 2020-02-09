# PART TWO ------------------------------------------------------------------------------
inputFile = open("input_day2.txt", "r")
program = list()

for line in inputFile:
    number = ""
    for word in line:
        if word != "," and word != "\n":
            number += word
        else:
            program.append(int(number))
            number = ""


def rebuilt_intcode_program(program):
    initial_position = 0

    for i_noun in range(100):
        for i_verb in range(100):
            program_double = program[:]
            program_double[1] = i_noun
            program_double[2] = i_verb
            # print(program_double)

            initial_position = 0

            while initial_position < len(program_double)-4:
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
                    break
                else:
                    # ERROR!
                    print("An error has occurred. Input " + str(program_double[initial_position]) + " is not recognised.")
                    break
            if program_double[0] == 19690720:
                return list({i_noun, i_verb})


print(str(rebuilt_intcode_program(program)))

noun_verb_couple = rebuilt_intcode_program(program)
answer = 100 * noun_verb_couple[0] + noun_verb_couple[1]
print(answer)
