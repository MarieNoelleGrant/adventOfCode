import math
from collections import Counter

# lower_limit = 199500
# higher_limit = 200000


def check_if_same_number(*args):
    check = False
    if args.count(args[0]) != 3:
        sum = 0
        multiplication = args[0] * len(args)

        for arg in args:
            sum += arg

        if sum == multiplication:
            check = True
    else:
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
        list_number_to_test = [int(i) for i in str(password_number_to_test)]
        # Counter nous transforme la liste en dict et nous retourne ici le nombre d'item identiques
        # On retransforme en liste par la suite pour pouvoir le manipuler.
        qte_of_diff_num = list(Counter(list_number_to_test).values())

        # 1. Si le numéro fourni est composé de six chiffres
        if len(list_number_to_test) == 6:
            # 2. Si le numéro founi n'est pas composé de deux chiffres répétés trois fois (ex. 444555 ), puisque cela ne fera jamais dans le motif voulu)
            if qte_of_diff_num.count(3) != 2:
                same_number_twice = False
                same_number_three = False
                always_goes_up = True
                int_cpt = 0
                int_same_number = 0
                number_to_not_repeat = 0
                number_found_twice = list()

                for number in list_number_to_test:
                    # 3. On vérifie les chiffres avant et/ou après, pour voir s'ils se répétent.
                    same_as_before = False
                    same_as_next = False
                    same_as_both = False
                    if int_cpt > 0:
                        same_as_before = check_if_same_number(number, list_number_to_test[int_cpt - 1])
                        if always_goes_up:
                            always_goes_up = check_if_higher_number(list_number_to_test[int_cpt - 1], number)
                        if int_cpt < 5:
                            same_as_next = check_if_same_number(number, list_number_to_test[int_cpt + 1])
                            same_as_both = check_if_same_number(list_number_to_test[int_cpt - 1], number, list_number_to_test[int_cpt + 1])
                    else:
                        same_as_next = check_if_same_number(number, list_number_to_test[int_cpt + 1])

                    # 3.1 Si le chiffre avant ou après est identique, mais pas les deux :
                    if same_as_before or same_as_next and not same_as_both:
                        # 3.1.1 Si le chiffre est différent d'un chiffre qu'on ne veut pas répéter :
                        if number != number_to_not_repeat:
                            same_number_twice = True
                            # *** On ajoute le chiffre à une liste de chiffres trouvés deux fois, ci ce n'est déjà fait :
                            if number not in number_found_twice:
                                number_found_twice.append(number)
                        # 3.1.2 Si non, si le chiffre ne correspond au chiffre qu'on ne veut pas répéter :
                        elif len(number_found_twice) != 0 and number_found_twice[int_same_number] == number_to_not_repeat:
                            same_number_twice = False
                            if number != number_to_not_repeat:
                                int_same_number += 1

                    # 3.2 Si les chiffres avant et après sont identiques :
                    if same_as_both:
                        same_number_three = True
                        number_to_not_repeat = number

                    int_cpt += 1

                # 4. Si le numéro comporte au moins une suite de deux chiffres qui ne font pas partie d'une suite de trois chiffres + que les chiffres augmentent toujours :
                if ((same_number_twice and always_goes_up) and not same_number_three) or (same_number_twice and always_goes_up and same_number_three):
                    list_possibilities.append(password_number_to_test)

            password_number_to_test += 1

    return list_possibilities


list_possible_passwords = calculate_possibilities(254032, 789860)
reponse = len(list_possible_passwords)
print(list_possible_passwords)
print("Le nombre de mots de passe possibles est : " + str(reponse))
