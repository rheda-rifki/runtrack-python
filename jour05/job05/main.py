def chiffrement_cesar(message, decalage):
    resultat = ""
    for caractere in message:
        if caractere.isalpha():
            # Gérer les majuscules
            if caractere.isupper():
                resultat += chr((ord(caractere) - ord('A' ) + decalage) % 26 + ord('A'))
            # Gérer les minuscules
            else:
                resultat += chr((ord(caractere) - ord('a' ) + decalage) % 26 + ord('a'))
        else:
            # Ne pas décaler les caractères non alphabétiques
            resultat += caractere
    return resultat

# Exemple d'utilisation avec un décalage de 3
message_original = "Bonjour, Cesar!"
decalage = 3
message_chiffre = chiffrement_cesar(message_original, decalage)

print(f"Message original : {message_original}")
print(f"Message chiffré : {message_chiffre}")
