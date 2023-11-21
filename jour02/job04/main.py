def afficher_tables_multiplication(N):
    if N <= 0:
        print("Veuillez entrer un entier supérieur à zéro.")
        return

    print(f"Tables de multiplication de 1 à {N} :")
    for i in range(1, N + 1):
        print(f"\nTable de multiplication de {i} :")
        for j in range(1, 11):
            produit = i * j
            print(f"{i} x {j} = {produit}")

if __name__ == "__main__":
    try:
        N = int(input("Entrez un entier supérieur à zéro (N) : "))
        afficher_tables_multiplication(N)
    except ValueError:
        print("Veuillez entrer un entier valide.")
