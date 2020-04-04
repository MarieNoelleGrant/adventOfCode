import math
from os import path


centralPort = [0, 0]

first_wire = list([0, 0])
second_wire = list([0, 0])


# -------------------------------------------------------------------
# Fonctions 'utilitaires'
# --------------------------------------------------------------------
def calcul_manhattan_distance(liste_coordonnees):
    plus_petite_distance = 0
    for intersection in liste_coordonnees:
        # calcul de la manhattan distance
        distance_calculee = abs(0 - intersection[0]) + abs(0 - intersection[1])

        if plus_petite_distance == 0:
            plus_petite_distance = distance_calculee
        else:
            if distance_calculee < plus_petite_distance:
                plus_petite_distance = distance_calculee

    return plus_petite_distance


def create_coordinates(array):
    b_position_f = [0, 0]
    newArray = list()
    for coordinates_f in array:

        direction = coordinates_f[0]
        coordinates_f = coordinates_f.strip(direction)
        distance = int(coordinates_f)

        if direction == "R":
            for i in range(distance):
                new_position_f = b_position_f[:]
                new_position_f[0] += 1
                b_position_f[0] += 1
                newArray.append(new_position_f)

        elif direction == "L":
            for i in range(distance):
                new_position_f = b_position_f[:]
                new_position_f[0] -= 1
                b_position_f[0] -= 1
                newArray.append(new_position_f)

        elif direction == "U":
            for i in range(distance):
                new_position_f = b_position_f[:]
                new_position_f[1] += 1
                b_position_f[1] += 1
                newArray.append(new_position_f)

        elif direction == "D":
            for i in range(distance):
                new_position_f = b_position_f[:]
                new_position_f[1] -= 1
                b_position_f[1] -= 1
                newArray.append(new_position_f)

    return newArray


def creation_intersections(liste_1, liste_2):
    liste_intersections = list()
    intCpt = 0
    print("Création des intersections commencée")
    for coordinates_s in liste_2:
        intCpt += 1
        if coordinates_s in liste_1:
            liste_intersections.append(coordinates_s)
            print("still going : " + str(intCpt))

    return liste_intersections


# -------------------------------------------------------------------
# Pour créer le fichier des intersections qu'une seule fois
# --------------------------------------------------------------------
if not path.exists('intersections.txt'):
    with open("input_day3.txt", "r") as inputText:
        i = 0
        for i, line in enumerate(inputText):
            if i == 0:
                first_wire = line.split(",")
                first_wire[-1] = first_wire[-1].strip("\n")
            else:
                second_wire = line.split(",")
                second_wire[-1] = second_wire[-1].strip("\n")
            i += 1

    position_coordinates_f = create_coordinates(first_wire)
    position_coordinates_s = create_coordinates(second_wire)
    list_intersections = creation_intersections(position_coordinates_f, position_coordinates_s)

    with open("intersections.txt", "w+") as intersections:
        intersections.write(str(list_intersections))

with open("intersections.txt", "r") as points_intersection:
    intersections_liste = eval(points_intersection.read())

reponse = calcul_manhattan_distance(intersections_liste)

print('Le point le plus près selon la distance manhattan est : ' + str(reponse))

