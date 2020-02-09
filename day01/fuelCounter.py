import math

inputFile = open("input_day1.txt", "r")


def calc_fuel_needed(module_mass):
    fuel_needed = math.floor(int(module_mass)/3)-2
    return fuel_needed


total_fuel = 0
for line in inputFile:
    fuel_per_module = calc_fuel_needed(line)
    total_fuel += fuel_per_module

print("The total fuel count is: " + str(total_fuel))
