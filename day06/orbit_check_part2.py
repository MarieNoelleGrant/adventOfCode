# PART ONE -------------------------------------------------------------------------------
#   Compter tous les orbites (directes ou indirectes) du système solaire présenté (input_day6)
#   - Orbite direct = premier niveau, orbite indirect = niveaux imbriqués

list_all_planet_pairs = list()
list_orbital_transfers_you = ['YOU']
list_orbital_transfers_santa = ['SAN']


def construct_orbital_transfers(starting_point):
    """ Méthode qui construit l'itinéraire d'un point externe vers le centre du système. Modifie un tableau existant selon la valeur reçue en argument.

    :param starting_point:
    """
    orbit_level = 1
    still_going = True
    copy_list_all_planet_pairs = list_all_planet_pairs[:]

    if starting_point == 'santa':
        list_orbital_transfers = list_orbital_transfers_santa
    else:
        list_orbital_transfers = list_orbital_transfers_you

    while still_going:
        # ** Ajout d'un tableau vide à la suite du tableau des orbites
        for planet_pair in copy_list_all_planet_pairs:
            # ** Orbit level = position dans le tableau.
            if planet_pair[1] == list_orbital_transfers[orbit_level]:
                list_orbital_transfers.append(planet_pair[0])
                if planet_pair[0] == 'COM':
                    still_going = False
                copy_list_all_planet_pairs.pop(copy_list_all_planet_pairs.index(planet_pair))

                break

        orbit_level += 1


with open("input_day6.txt", "r") as inputFile:
    # Modification du texte de l'input en tableau, pour consultation plus facile
    for line in inputFile:
        planet_pair = line.split(")")
        planet_pair[1] = planet_pair[1].replace("\n", "")

        # Si la valeur == 'YOU', ou 'SAN' planète la plus éloignée.
        # Puisqu'une seule valeur sera nécessaire par niveau d'orbite, on concatenne simplement la valeur à la fin du tableau
        if planet_pair[1] == 'YOU':
            list_orbital_transfers_you.append(planet_pair[0])
        elif planet_pair[1] == 'SAN':
            list_orbital_transfers_santa.append(planet_pair[0])

        # On emmagasine la valeur des autres orbites pour consultation après.
        else:
            list_all_planet_pairs.append(planet_pair)


# On construit les deux tableaux pour l'itinéraire total
# Appel de la fonction construct_orbital_transfers
construct_orbital_transfers('santa')
construct_orbital_transfers('you')
# print(list_orbital_transfers_you)
# print(list_orbital_transfers_santa)

# On trouve la première planète commune aux deux routes
junction_found = False
for planet_1 in list_orbital_transfers_you:
    if junction_found:
        break
    for planet_2 in list_orbital_transfers_santa:
        if planet_1 == planet_2:
            junction_planet = planet_1
            junction_found = True
            break

# On reconstruit un nouveau tableau avec les deux fusionnés où l'intersection
# *** On s'assure d'inverser l'ordre d'un des deux tableaux avant.
list_orbital_transfers_santa.reverse()
index_junction_you = list_orbital_transfers_you.index(junction_planet)
index_junction_santa = list_orbital_transfers_santa.index(junction_planet)
full_route = list_orbital_transfers_you[:list_orbital_transfers_you.index(junction_planet)] + list_orbital_transfers_santa[list_orbital_transfers_santa.index(junction_planet):]

# Puisqu'on veut savoir les sauts nécessaires (et non le nombre d'arrêts), cela correspond au nombre d'arrêts entre le début et la fin, -1.
answer = len(full_route[1:len(full_route)-1]) - 1
print('The minimum number of orbital transfers is : ' + str(answer))
