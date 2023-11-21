alphabet = "abcdefghijklmnopqrstuvwxyz"

def generate_pyramid(n):
    for i in range(n):
        print(alphabet[:i+1])

# Utilisation du programme pour créer une suite pyramidale de 10 caractères
generate_pyramid(len(alphabet))
