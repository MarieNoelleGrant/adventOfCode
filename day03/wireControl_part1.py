import math


centralPort = [0, 0]

# with open("wireMap.txt", "w+") as wireMap:
#     for i in range(2000):
#         if i == 999:
#             wireMap.write("."*999+"o"+"."*999+"\n")
#         else:
#             wireMap.write("."*2000+"\n")

first_wire = list([0,0])
second_wire = list([0,0])
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

b_position_f = centralPort[:]
position_coordinates_f = list()
position_coordinates_s = list()


def create_coordinates(array, newArray):
    for coordinates_f in array:

        direction = coordinates_f[0]
        coordinates_f = coordinates_f.strip(direction)
        distance = int(coordinates_f)

        if direction == "R":
            for i in range(distance):
                new_position_f = b_position_f[:]
                new_position_f[1] += 1
                b_position_f[1] += 1
                newArray.append(new_position_f)

        elif direction == "L":
            for i in range(distance):
                new_position_f = b_position_f[:]
                new_position_f[1] -= 1
                b_position_f[1] -= 1
                newArray.append(new_position_f)

        elif direction == "U":
            for i in range(distance):
                new_position_f = b_position_f[:]
                new_position_f[0] -= 1
                b_position_f[0] -= 1
                newArray.append(new_position_f)

        elif direction == "D":
            for i in range(distance):
                new_position_f = b_position_f[:]
                new_position_f[0] += 1
                b_position_f[0] += 1
                newArray.append(new_position_f)


create_coordinates(first_wire, position_coordinates_f)
create_coordinates(second_wire, position_coordinates_s)
list_intersections = list()

# for coordinates_s in position_coordinates_s:
#     for coordinates_f in position_coordinates_f:
#         if coordinates_s == coordinates_f:
#             list_intersections.append(coordinates_f)
#             break
intCpt = 0
# list_intersections = [coordinates_s for coordinates_s in position_coordinates_s if coordinates_s in position_coordinates_f]

for coordinates_s in position_coordinates_s:
    intCpt += 1
    if coordinates_s in position_coordinates_f:
        list_intersections.append(coordinates_s)
        print("still going : " + str(intCpt))


# print(list(set(position_coordinates_s).intersection(position_coordinates_f)))
# print(list_intersections)

with open("intersections.txt", "w+") as intersections:
    intersections.write(str(list_intersections))
