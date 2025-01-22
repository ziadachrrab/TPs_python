import os
from datetime import datetime
from math import sqrt

def main():
    # Répertoire courant
    current_directory = os.getcwd()
    print(f"Répertoire courant : {current_directory}")

    # Date et heure actuelles
    now = datetime.now()
    print(f"Date et heure actuelles : {now}")

    # Racine carrée
    try:
        number = float(input("Entrez un nombre : "))
        print(f"La racine carrée de {number} est {sqrt(number)}")
    except ValueError:
        print("Veuillez entrer un nombre valide.")

if __name__ == "__main__":
    main()
