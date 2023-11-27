def my_sort(lst):
    """
    Trie une liste en utilisant le tri à bulles et retourne la liste triée.
    
    Arguments :
    lst -- La liste à trier.
    
    Returns :
    list -- La liste triée.
    """
    n = len(lst) 
    coups = 0     

    tri_effectue = False
    while not tri_effectue:
        tri_effectue = True  

        for i in range(n - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]

                tri_effectue = False

                coups += 1

    print("Nombre total de coups nécessaires pour trier la liste :", coups)

    return lst

ma_liste = [5, 2, 9, 1, 5, 6]
liste_triee = my_sort(ma_liste)

print("Liste triée :", liste_triee)
