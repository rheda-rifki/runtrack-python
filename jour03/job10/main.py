def verifier_pair_impair(nombre):
    if not isinstance(nombre, int) or nombre < 0:
        print("Veuillez entrer un nombre entier positif.")
        return

    if nombre % 2 == 0:
        print(f"Le nombre {nombre} est pair.")
    else:
        print(f"Le nombre {nombre} est impair.")

verifier_pair_impair(4)
verifier_pair_impair(7)
verifier_pair_impair(12)
verifier_pair_impair(-5) 
verifier_pair_impair(3.5) 