# PART ONE -------------------------------------------------------------------------------
#   Compter tous les orbites (directes ou indirectes) du système solaire présenté (input_day6)
#   - Orbite direct = premier niveau, orbite indirect = niveaux imbriqués

list_all_planet_pairs = list()
list_nested_orbits = [['COM']]
orbit_level = 1

with open("input_day6.txt", "r") as inputFile:
    # Modification du texte de l'input en tableau, pour consultation plus facile
    for line in inputFile:
        planet_pair = line.split(")")
        planet_pair[1] = planet_pair[1].replace("\n", "")

        # Si la valeur == 'COM', planète la plus au centre du système.
        # On emmagasine la valeur des planètes en orbite autour de celle-ci dans le niveau 1 (position 1) du tableau.
        if planet_pair[0] == 'COM':
            try:
                list_nested_orbits[1].append(planet_pair[1])
            except IndexError:
                list_nested_orbits.append([])
                list_nested_orbits[1].append(planet_pair[1])
        # On emmagasine la valeur des autres orbites pour consultation après.
        else:
            list_all_planet_pairs.append(planet_pair)

# Construction des autres niveaux d'orbites dans le tableau list_nested_orbits.
# À chaque fois qu'une planète est associée au niveau d'orbite, le couple correspondant est enlevé du tableau général list_all_planet_pairs.
# Lorsque ce tableau est vide, c'est que toutes les planètes ont été assignées.
while len(list_all_planet_pairs) != 0:
    ele_to_pop = list()
    # ** Ajout d'un tableau vide à la suite du tableau des orbites
    list_nested_orbits.append([])
    for planet_pair in list_all_planet_pairs:
        # ** Orbit level = position dans le tableau.
        if planet_pair[0] in list_nested_orbits[orbit_level]:
            list_nested_orbits[orbit_level + 1].append(planet_pair[1])
            # ** Ajout des paires à supprimer du tableau global dans un tableau, pour le supprimer qu'à la fin, et éviter des erreurs à la lecture de la boucle
            ele_to_pop.append(planet_pair)

    orbit_level += 1
    for ele in ele_to_pop:
        list_all_planet_pairs.pop(list_all_planet_pairs.index(ele))


# Le nombre d'orbites total d'une planète équivault à sa position dans le tableau.
# On multiplie ensuite par le nombre de planètes présentes à ce niveau d'orbite.
# Et finalement on additionne ce nombre au nombre d'orbites déjà calculés.
nombre_orbites_totaux = 0
for i in range(0, len(list_nested_orbits)):
    nombre_orbites_totaux += i*len(list_nested_orbits[i])

print(list_nested_orbits)
print(nombre_orbites_totaux)
