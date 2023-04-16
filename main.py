import random
MIN = 1
MAX = 10

def poser_question():
    nombre_de_vie = 4
    nombre_magique = random.randint(MIN, MAX)

    while nombre_de_vie > 0:
        print("")
        resp = input(f"Devinez le nombre magique, entre {MIN} et {MAX} (il vous reste {nombre_de_vie} vies) : ")

        try:
            res = int(resp)
            if res < MIN or res > MAX:
                print(f"ERRUR: Vous devez rentrer un nombre entre {MIN} et {MAX}.")
                print("")
            else:
                if res < nombre_magique:
                    print("Le nombre magique est plus grand")
                elif res > nombre_magique:
                    print("Le nombre magique est plus petit")
                else:
                    print("BRAVO ! Vous avez trouvé le nombre magique.")
                    return

                nombre_de_vie = nombre_de_vie-1
        except:
            print("ERREUR: Vous devez écrire un nombre.")

    if nombre_de_vie == 0:
        print(" ")
        print(f"Désolé, vous avez perdu, le nombre magique était : {nombre_magique}")


poser_question()