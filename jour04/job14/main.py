def est_separateur(caractere):
    separateurs = [' ', ',', '.', ';', ':', '!', '?']
    return caractere in separateurs

def my_long_word(longueur_min, phrase):
    mot_actuel = ""
    mots_longueur_min = []

    for caractere in phrase:
        if not est_separateur(caractere):
            mot_actuel += caractere
        elif len(mot_actuel) > longueur_min:
            mots_longueur_min.append(mot_actuel)
            mot_actuel = ""
        else:
            mot_actuel = ""

    if len(mot_actuel) > longueur_min:
        mots_longueur_min.append(mot_actuel)

    phrase_sortie = ' '.join(mots_longueur_min)

    return phrase_sortie

longueur_minimale = 3
phrase_entree = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"

resultat = my_long_word(longueur_minimale, phrase_entree)

print("Output :", resultat)
