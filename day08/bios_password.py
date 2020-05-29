# PART ONE -------------------------------------------------------------------------------
#   Trouver quelle couche du code/image contient le moins de fois le digit 0
#   Multiplier la quantité du digit 1 par la quantité du digit 2 sur ce layer

# PART TWO -------------------------------------------------------------------------------
#   Si 0 = black, 1 = white, 2 = transparent, et que les layer sont superposés avec le 1e sur le dessus, dernier en dessous,
#   Quel seront les couleurs qui parraîtront au final/quel sera le code une fois décodé ?
#   (devrait contenir que des 1 et des 0!)


horizontal_pixels = 25
vertical_pixels = 6
numbers_per_layer = horizontal_pixels * vertical_pixels
list_numbers = list()
list_layers = list()

with open("input_day8.txt", "r") as inputFile:
    for line in inputFile:
        list_numbers = list()
        for number in line:
            if number != '\n':
                list_numbers.append(int(number))


def seperate_layers():
    nb_layers_total = round(len(list_numbers) / numbers_per_layer)
    for i in range(1, nb_layers_total + 1):
        int_start = (i - 1) * numbers_per_layer
        int_end = numbers_per_layer * i
        layer_list = list_numbers[int_start:int_end]
        list_layers.append(layer_list)


def find_layer_less_zeros():
    seperate_layers()
    less_number_zeros = list()
    for layer in list_layers:
        nb_zeros_in_layer = layer.count(0)
        if not less_number_zeros:
            less_number_zeros.append(nb_zeros_in_layer)
            less_number_zeros.append(layer)
        else:
            if nb_zeros_in_layer < less_number_zeros[0]:
                less_number_zeros[0] = nb_zeros_in_layer
                less_number_zeros[1] = layer

    return less_number_zeros


def decode_image():
    seperate_layers()
    decoded_img = ''
    for index_pixel in range(0, numbers_per_layer):
        for index_liste in range(0, len(list_layers)):
            if list_layers[index_liste][index_pixel] != 2:
                if list_layers[index_liste][index_pixel] == 0:
                    decoded_img += ' '
                else:
                    decoded_img += '|'

                if (index_pixel + 1) % 25 == 0:
                    decoded_img += '\n'

                break

    return decoded_img


# ---  Steps for part 1 ------------------------
layer_with_less_zeros = find_layer_less_zeros()
# print(layer_with_less_zeros)
result_multiplication_1_2 = layer_with_less_zeros[1].count(1) * layer_with_less_zeros[1].count(2)
# print(result_multiplication_1_2)

# ---  Steps for part 2 ------------------------
print(decode_image())

