import math


def calc_fuel_needed(module_mass):
    all_fuel = 0
    # 1. Calcul du fuel de base pour la masse
    fuel_for_mass = math.floor(int(module_mass)/3)-2
    fuel_for_fuel = fuel_for_mass
    # 2. Calcul du fuel supplémentaire pour le fuel ajouté
    while fuel_for_fuel > 0:
        all_fuel += fuel_for_fuel
        fuel_for_fuel = math.floor(int(fuel_for_fuel) / 3) - 2

    return all_fuel


total_fuel = 0

# *** Pour refermer le fichier après utilisation :
with open("input_day1.txt", "r") as masses:
    for line in masses:
        fuel_per_module = calc_fuel_needed(line)
        total_fuel += fuel_per_module


print("The total fuel count is: " + str(total_fuel))
