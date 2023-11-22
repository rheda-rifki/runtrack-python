def time_to_text(minutes):
    if not isinstance(minutes, int) or minutes < 0:
        print("Veuillez entrer un nombre entier positif.")
        return

    heures = minutes // 60
    minutes_restantes = minutes % 60

    print(f"{heures} heures et {minutes_restantes} minutes.")


time_to_text(120)
time_to_text(75)
time_to_text(45)
time_to_text(-30) 
time_to_text(90.5)  
