def contient_e(chaine):
    return 'e' in chaine.lower()

# Exemples d'utilisation
chaine1 = "Hello, World!"
chaine2 = "Python"
chaine3 = "Bonjour"

if contient_e(chaine1):
    print(f'La chaîne "{chaine1}" contient le caractère "e".')
else:
    print(f'La chaîne "{chaine1}" ne contient pas le caractère "e".')

if contient_e(chaine2):
    print(f'La chaîne "{chaine2}" contient le caractère "e".')
else:
    print(f'La chaîne "{chaine2}" ne contient pas le caractère "e".')

if contient_e(chaine3):
    print(f'La chaîne "{chaine3}" contient le caractère "e".')
else:
    print(f'La chaîne "{chaine3}" ne contient pas le caractère "e".')
