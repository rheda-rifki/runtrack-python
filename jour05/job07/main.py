def arrondir_notes(notes):
    notes_arrondies = []

    for note in notes:
        if note < 40:
            # Échec au test, pas d'arrondi
            notes_arrondies.append(note)
        else:
            # Arrondir la note aux multiples de 5 si nécessaire
            difference = 5 - (note % 5)
            if difference < 3:
                note_arrondie = note + difference
            else:
                note_arrondie = note

            # Limiter la note maximale à 100
            notes_arrondies.append(min(note_arrondie, 100))

    return notes_arrondies

# Exemple d'utilisation
notes_originales = [35, 82, 67, 93, 45]
notes_arrondies = arrondir_notes(notes_originales)

# Afficher le résultat
print("Notes originales :", notes_originales)
print("Notes arrondies  :", notes_arrondies)
