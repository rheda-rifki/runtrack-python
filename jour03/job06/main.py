def verifier_nombre(nombre):
    if nombre > 0:
        print("positif")
    elif nombre < 0:
        print("negatif")
    else:
        print("le nombre est nul")

verifier_nombre(5)
verifier_nombre(-3)
verifier_nombre(0)
