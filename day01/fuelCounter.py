import math

# inputFile = open("input_day1.txt", "r")


def calc_fuel_needed(module_mass):
    fuel_needed = math.floor(int(module_mass)/3)-2
    return fuel_needed


total_fuel = 0

# *** Pour refermer le fichier après utilisation :
with open("input_day1.txt", "r") as masses:
    for line in masses:
        fuel_per_module = calc_fuel_needed(line)
        total_fuel += fuel_per_module

# *** Ou encore :
# inputFile.close()

print("The total fuel count is: " + str(total_fuel))
