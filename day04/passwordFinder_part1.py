import math

# lower_limit = 199500
# higher_limit = 200000


def check_if_same_number(number_1, number_2):
    check = False
    sum = number_1 + number_2
    multiplication = number_1 * 2

    if sum == multiplication:
        check = True

    return check


def check_if_higher_number(number_1, number_2):
    check = True
    if number_2 - number_1 < 0:
        check = False

    return check


def calculate_possibilities(lower_limit, higher_limit):
    total_range_possible = higher_limit - lower_limit
    password_number_to_test = lower_limit
    list_possibilities = list()

    for i in range(total_range_possible):
        # On transforme le nombre en list, pour pouvoir faire des opérations
        list_password_number_to_test = [int(i) for i in str(password_number_to_test)]

        if len(list_password_number_to_test) == 6:
            same_number_twice = False
            always_goes_up = True
            int_cpt = 0
            for number in list_password_number_to_test:
                same_as_before = False
                same_as_next = False
                if int_cpt != 5:
                    same_as_next = check_if_same_number(number, list_password_number_to_test[int_cpt + 1])
                if int_cpt != 0:
                    same_as_before = check_if_same_number(list_password_number_to_test[int_cpt - 1], number)
                    if always_goes_up:
                        always_goes_up = check_if_higher_number(list_password_number_to_test[int_cpt - 1], number)

                if same_as_before or same_as_next:
                    same_number_twice = True

                int_cpt += 1

            if same_number_twice and always_goes_up:
                list_possibilities.append(password_number_to_test)

        password_number_to_test += 1

    return list_possibilities


# list_possible_passwords = calculate_possibilities(254032, 789860)
# reponse = len(list_possible_passwords)
# print("Le nombre de mots de passe possibles est : " + str(reponse))
