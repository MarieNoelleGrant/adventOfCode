import math
from os import path


# -------------------------------------------------------------------
# Fonctions 'utilitaires'
# --------------------------------------------------------------------
def calcul_manhattan_distance(liste_coordonnees):
    """ Fonction qui calcule la distance manhattan de chaque coordonnées de la liste reçue en argument.
    Renvoie la distance la plus courte.

    :param liste_coordonnees
    :return plus_petite_distance
    """

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


def create_coordinates(liste_deplacements):
    """ Fonction qui crée les coordonnées individuelles de chaque déplacement, selon les valeurs reçues dans le tableau en argument.

    :param liste_deplacements
    :return new_array_coordonnees
    """

    b_position = [0, 0]
    new_array_coordonnees = list()
    for coordinates in liste_deplacements:

        direction = coordinates[0]
        coordinates = coordinates.strip(direction)
        distance = int(coordinates)

        if direction == "R":
            for i in range(distance):
                new_position = b_position[:]
                new_position[0] += 1
                b_position[0] += 1
                new_array_coordonnees.append(new_position)

        elif direction == "L":
            for i in range(distance):
                new_position = b_position[:]
                new_position[0] -= 1
                b_position[0] -= 1
                new_array_coordonnees.append(new_position)

        elif direction == "U":
            for i in range(distance):
                new_position = b_position[:]
                new_position[1] += 1
                b_position[1] += 1
                new_array_coordonnees.append(new_position)

        elif direction == "D":
            for i in range(distance):
                new_position = b_position[:]
                new_position[1] -= 1
                b_position[1] -= 1
                new_array_coordonnees.append(new_position)

    return new_array_coordonnees


def creation_intersections(liste_1, liste_2):
    """ Fonction qui vérifie si des coordonnées sont communes aux deux listes.
    Si c'est le cas, emmagasine la valeur de l'intersection dans un nouveau tableau.

    :param liste_1
    :param liste_2
    :return: liste_intersections
    """

    liste_intersections = list()
    intCpt = 0
    print("Création des intersections commencée")
    for coordinates_s in liste_2:
        intCpt += 1
        if coordinates_s in liste_1:
            liste_intersections.append(coordinates_s)
            print("still going : " + str(intCpt))

    return liste_intersections


def calcul_nb_pas_optimal(liste_coor_1, liste_coor_2, liste_intersections):
    """ Fonction qui vérifie le nombre de pas parcourru pour chaque intersection.
    Puisque chaque coordonnée du tableau 1 ou 2 correspond à un pas, on additionne simplement les index représentant chaque intersection dans les listes respectives

    :param liste_coor_1
    :param liste_coor_2
    :param liste_intersections
    :return: nb_pas_optimal
    """

    nb_pas_optimal = 0
    for intersection in liste_intersections:
        nb_pas_fil_1 = liste_coor_1.index(intersection) + 1
        nb_pas_fil_2 = liste_coor_2.index(intersection) + 1
        nb_pas_calcul = nb_pas_fil_1 + nb_pas_fil_2

        if nb_pas_optimal == 0 or nb_pas_calcul < nb_pas_optimal:
            nb_pas_optimal = nb_pas_calcul

    return nb_pas_optimal


# -------------------------------------------------------------------
# Pour créer le fichier des intersections qu'une seule fois
# --------------------------------------------------------------------
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

    if not path.exists('intersections.txt'):
        list_intersections = creation_intersections(position_coordinates_f, position_coordinates_s)
        with open("intersections.txt", "w+") as intersections:
            intersections.write(str(list_intersections))

with open("intersections.txt", "r") as points_intersection:
    intersections_liste = eval(points_intersection.read())

intersection_moins_pas = calcul_nb_pas_optimal(position_coordinates_f, position_coordinates_s, intersections_liste)
print(intersection_moins_pas)

