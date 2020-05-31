from os import path
from math import gcd

asteroid_positions = list()
text_file = 'input_day10'


def construct_asteroid_positions(file):
    test_input = ''
    length_lines = 0
    length_columns = 0
    if path.exists(file):
        with open(file, "r") as inputFile:
            for Y, line in enumerate(inputFile):
                length_columns += 1
                for X, word in enumerate(line):
                    if length_columns == 1 and word != '\n':
                        length_lines += 1
                    if word == '#':
                        asteroid_positions.append([X, Y])
    # else:
    #     for Y, line in enumerate(file):
    #         test_input += line
    #         for X, word in enumerate(line):
    #             if word == '#' and word != '\n' and word != ' ':
    #                 asteroid_positions.append([X, Y])

    return length_lines, length_columns


# def compare_other_asteroids(position_xy, width):
#     index_of_asteroid = asteroid_positions.index(position_xy)
#
#     copy_asteroids_before = asteroid_positions[:index_of_asteroid]
#     copy_asteroids_after = asteroid_positions[index_of_asteroid:]
#     list_reverse = list(reversed(copy_asteroids_before))
#
#     all_asteroids_seen = asteroid_positions[:]
#
#     for other_asteroid in list_reverse:
#         if other_asteroid != position_xy:
#             distance = [other_asteroid[0] - position_xy[0], other_asteroid[1] - position_xy[1]]
#             if distance[0] == 0:
#                 if distance[1] < 0:
#                     distance[1] = int(distance[1] / distance[1] * -1)
#                 else:
#                     distance[1] = int(distance[1] / distance[1])
#             elif distance[1] == 0:
#                 if distance[0] < 0:
#                     distance[0] = int(distance[0] / distance[0] * -1)
#                 else:
#                     distance[0] = int(distance[0] / distance[0])
#             else:
#                 if distance[0] % distance[1] == 0 or distance[1] % distance[0] == 0:
#                     denominator = gcd(distance[0], distance[1])
#                     distance = [distance[0] / denominator, distance[1] / denominator]
#
#             for i in range(1, width - 1):
#                 y_a_verifier = (distance[1] * i) + other_asteroid[1]
#                 x_a_verifier = (distance[0] * i) + other_asteroid[0]
#                 position_check = [x_a_verifier, y_a_verifier]
#
#                 if position_check in all_asteroids_seen:
#                     all_asteroids_seen.remove(position_check)
#         else:
#             all_asteroids_seen.remove(other_asteroid)
#
#     for asteroid_after in copy_asteroids_after:
#         if asteroid_after != position_xy:
#             distance = [asteroid_after[0] - position_xy[0], asteroid_after[1] - position_xy[1]]
#             if distance[0] == 0:
#                 if distance[1] < 0:
#                     distance[1] = int(distance[1] / distance[1] * -1)
#                 else:
#                     distance[1] = int(distance[1] / distance[1])
#             elif distance[1] == 0:
#                 if distance[0] < 0:
#                     distance[0] = int(distance[0] / distance[0] * -1)
#                 else:
#                     distance[0] = int(distance[0] / distance[0])
#             else:
#                 if distance[0] % distance[1] == 0 or distance[1] % distance[0] == 0:
#                     denominator = gcd(distance[0], distance[1])
#                     distance = [distance[0]/denominator, distance[1]/denominator]
#
#             for i in range(1, width - 1):
#                 y_a_verifier = (distance[1] * i) + asteroid_after[1]
#                 x_a_verifier = (distance[0] * i) + asteroid_after[0]
#                 position_check = [x_a_verifier, y_a_verifier]
#                 if position_check in all_asteroids_seen:
#                     all_asteroids_seen.remove(position_check)
#         else:
#             all_asteroids_seen.remove(asteroid_after)
#
#     nb_asteroids = len(all_asteroids_seen)
#     return nb_asteroids, all_asteroids_seen


def compare_other_asteroids(position_xy, width, compare_asteroid, all_asteroids_seen):

    if compare_asteroid != position_xy:
        distance = [compare_asteroid[0] - position_xy[0], compare_asteroid[1] - position_xy[1]]
        if distance[0] == 0:
            if distance[1] < 0:
                distance[1] = int(distance[1] / distance[1] * -1)
            else:
                distance[1] = int(distance[1] / distance[1])
        elif distance[1] == 0:
            if distance[0] < 0:
                distance[0] = int(distance[0] / distance[0] * -1)
            else:
                distance[0] = int(distance[0] / distance[0])
        else:
            # check if commun denominator
            denominator = gcd(abs(distance[0]), abs(distance[1]))

            if denominator != 1:
                distance = [int(distance[0] / denominator), int(distance[1] / denominator)]

        for i in range(1, width - 1):
            y_a_verifier = (distance[1] * i) + compare_asteroid[1]
            x_a_verifier = (distance[0] * i) + compare_asteroid[0]
            position_check = [x_a_verifier, y_a_verifier]

            if position_check in all_asteroids_seen:
                all_asteroids_seen.remove(position_check)
    else:
        all_asteroids_seen.remove(compare_asteroid)

    return all_asteroids_seen


def initialisation(*args):
    best_asteroid_sighting = 0
    best_asteroid = list()
    list_asteroids = list()

    if args:
        width, height = construct_asteroid_positions(args)
    else:
        width, height = construct_asteroid_positions(text_file)

    for an_asteroid in asteroid_positions:
        # an_asteroid = [15, 17]
        index_of_asteroid = asteroid_positions.index(an_asteroid)
        copy_asteroids_before = asteroid_positions[:index_of_asteroid]
        copy_asteroids_after = asteroid_positions[index_of_asteroid:]
        list_reverse = list(reversed(copy_asteroids_before))

        all_asteroids_seen = asteroid_positions[:]

        for asteroid_before in list_reverse:
            all_asteroids_seen = compare_other_asteroids(an_asteroid, width, asteroid_before, all_asteroids_seen)
        for asteroid_after in copy_asteroids_after:
            all_asteroids_seen = compare_other_asteroids(an_asteroid, width, asteroid_after, all_asteroids_seen)

        nb_asteroids = len(all_asteroids_seen)

        if nb_asteroids >= best_asteroid_sighting:
            best_asteroid_sighting = nb_asteroids
            best_asteroid = an_asteroid
            list_asteroids = all_asteroids_seen

    print(best_asteroid)
    # print(list_asteroids)
    return best_asteroid_sighting


part1_answer = initialisation()
print(part1_answer)
