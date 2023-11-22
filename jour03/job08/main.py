def marche_puces(type, saison):
    if type == "fruits" and saison == "hiver":
        print("Orange, mandarine et kiwi.")
    elif type == "fruits" and saison == "ete":
        print("Poire, fraise, cassis.")
    elif type == "legume" and saison == "hiver":
        print("Carotte, topinambour, endive.")
    elif type == "legume" and saison == "ete":
        print("Artichaut, aubergine, navet.")
    else:
        print("Aucun produit correspondant trouvé.")

marche_puces("fruits", "hiver")
marche_puces("fruits", "ete")
marche_puces("legume", "hiver")
marche_puces("legume", "ete")

