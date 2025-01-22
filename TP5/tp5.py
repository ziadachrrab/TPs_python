import os
import csv
import json
import shutil


# Exercice 1 : Lecture de fichiers
def lecture_fichier():
    with open("exemple.txt", "w") as file:
        file.write("Ligne 1\nLigne 2\nLigne 3\nLigne 4\nLigne 5\n")
    with open("exemple.txt", "r") as file:
        for idx, line in enumerate(file, start=1):
            print(f"{idx}: {line.strip()}")


# Exercice 2 : Écriture dans un fichier
def ecriture_fichier():
    phrases = [input(f"Entrez la phrase {i + 1} : ") for i in range(3)]
    with open("phrases.txt", "w") as file:
        file.write("\n".join(phrases) + "\n")


# Exercice 3 : Ajout à un fichier
def ajout_fichier():
    while True:
        add_more = input("Voulez-vous ajouter d'autres phrases ? (oui/non) : ").lower()
        if add_more == "oui":
            with open("phrases.txt", "a") as file:
                phrase = input("Entrez une nouvelle phrase : ")
                file.write(phrase + "\n")
        else:
            break


# Exercice 4 : Traitement de fichiers CSV
def traitement_csv():
    with open("contacts.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Nom", "Âge", "Ville"])
        writer.writerows([
            ["Alice", 30, "Paris"],
            ["Bob", 25, "Lyon"],
            ["Charlie", 35, "Marseille"]
        ])
    with open("contacts.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"Nom : {row['Nom']}, Âge : {row['Âge']}, Ville : {row['Ville']}")


# Exercice 5 : Écriture et lecture de fichiers JSON
def traitement_json():
    etudiants = [
        {"Nom": "Alice", "Âge": 20, "Note": 15},
        {"Nom": "Bob", "Âge": 22, "Note": 14},
        {"Nom": "Charlie", "Âge": 21, "Note": 16}
    ]
    with open("etudiants.json", "w") as file:
        json.dump(etudiants, file, indent=4)
    with open("etudiants.json", "r") as file:
        data = json.load(file)
        for etudiant in data:
            print(f"Nom : {etudiant['Nom']}, Âge : {etudiant['Âge']}, Note : {etudiant['Note']}")


# Exercice 6 : Renommer et supprimer des fichiers
def renommer_supprimer():
    os.rename("phrases.txt", "anciennes_phrases.txt")
    os.remove("anciennes_phrases.txt")


# Exercice 7 : Copie et déplacement de fichiers
def copier_deplacer():
    with open("journal.txt", "w") as file:
        file.write("Ceci est un journal.\nUne autre ligne de texte.\n")
    shutil.copy("journal.txt", "journal_copie.txt")
    os.makedirs("archives", exist_ok=True)
    shutil.move("journal_copie.txt", "archives/journal_copie.txt")


# Exercice 8 : Gestion des erreurs
def gestion_erreurs():
    try:
        with open("inexistant.txt", "r") as file:
            content = file.read()
    except FileNotFoundError:
        print("Erreur : Le fichier 'inexistant.txt' n'existe pas.")


# Exercice 9 : Statistiques de fichier
def statistiques_fichier():
    with open("exemple.txt", "r") as file:
        lines = file.readlines()
    nb_lines = len(lines)
    nb_words = sum(len(line.split()) for line in lines)
    nb_chars = sum(len(line) for line in lines)
    print(f"Nombre de lignes : {nb_lines}")
    print(f"Nombre de mots : {nb_words}")
    print(f"Nombre de caractères : {nb_chars}")


# Exercice 10 : Application finale
def application_finale():
    FILENAME = "contacts.csv"

    def add_contact():
        with open(FILENAME, "a", newline="") as file:
            writer = csv.writer(file)
            name = input("Nom : ")
            age = input("Âge : ")
            city = input("Ville : ")
            writer.writerow([name, age, city])

    def show_contacts():
        if not os.path.exists(FILENAME):
            print("Aucun contact trouvé.")
            return
        with open(FILENAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(", ".join(row))

    def search_contact():
        name = input("Entrez le nom à rechercher : ")
        with open(FILENAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == name:
                    print(", ".join(row))
                    return
        print("Contact non trouvé.")

    def delete_contact():
        name = input("Entrez le nom du contact à supprimer : ")
        contacts = []
        with open(FILENAME, "r") as file:
            reader = csv.reader(file)
            contacts = [row for row in reader if row[0] != name]
        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(contacts)

    while True:
        print("\nMenu :")
        print("1. Ajouter un contact")
        print("2. Afficher tous les contacts")
        print("3. Rechercher un contact")
        print("4. Supprimer un contact")
        print("5. Quitter")
        choice = input("Votre choix : ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            show_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            break
        else:
            print("Choix invalide.")


# Menu principal
def main():
    while True:
        print("\nMenu Principal :")
        print("1. Lecture de fichiers")
        print("2. Écriture dans un fichier")
        print("3. Ajout à un fichier")
        print("4. Traitement de fichiers CSV")
        print("5. Traitement JSON")
        print("6. Renommer et supprimer des fichiers")
        print("7. Copier et déplacer des fichiers")
        print("8. Gestion des erreurs")
        print("9. Statistiques de fichier")
        print("10. Application finale")
        print("11. Quitter")
        choix = input("Votre choix : ")
        if choix == "1":
            lecture_fichier()
        elif choix == "2":
            ecriture_fichier()
        elif choix == "3":
            ajout_fichier()
        elif choix == "4":
            traitement_csv()
        elif choix == "5":
            traitement_json()
        elif choix == "6":
            renommer_supprimer()
        elif choix == "7":
            copier_deplacer()
        elif choix == "8":
            gestion_erreurs()
        elif choix == "9":
            statistiques_fichier()
        elif choix == "10":
            application_finale()
        elif choix == "11":
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")


if __name__ == "__main__":
    main()
