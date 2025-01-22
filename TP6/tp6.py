import logging

# Configure logging
logging.basicConfig(filename="error.log", level=logging.ERROR)

# Exercice 1 : Division par Zéro
def safe_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        raise ZeroDivisionError("La division par zéro n'est pas autorisée.")
    else:
        print("La division a été effectuée avec succès.")
        return result
    finally:
        print("Fin de la fonction safe_division.")

# Exercice 2 : Vérification de Type
def convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        raise ValueError("La conversion de la valeur en entier a échoué.")

# Exercice 3 : Lecture de Fichier
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError as e:
        print("Erreur : Le fichier n'existe pas.")
        log_error(str(e))
    finally:
        print("Tentative de lecture du fichier terminée.")

# Exercice 4 : Exceptions Personnalisées
class NegativeAgeError(Exception):
    pass

def set_age(age):
    if age < 0:
        raise NegativeAgeError("L'âge ne peut pas être négatif.")
    print(f"L'âge est réglé sur {age} ans.")

# Exercice 5 : Multi-Exceptions
def process_input(user_input):
    try:
        value = int(user_input)
        result = 10 / value
        print(f"Résultat : {result}")
    except ValueError:
        print("Erreur : Entrée non convertible en entier.")
    except ZeroDivisionError:
        print("Erreur : Division par zéro.")

# Exercice 6 : Utilisation de `else` et `finally`
# (Déjà intégré dans safe_division ci-dessus)

# Exercice 7 : Journalisation des Exceptions
def log_error(message):
    logging.error(message)

# Exercice 8 : Tests Unitaires
# Tests unitaires dans la section séparée (non inclus dans ce fichier pour la concision)

# Exercice 9 : Gestion des Exceptions dans les Boucles
def get_positive_integer():
    while True:
        try:
            value = int(input("Entrez un entier positif : "))
            if value < 0:
                print("Erreur : Veuillez entrer un entier positif.")
                continue
            return value
        except ValueError:
            print("Erreur : Entrée non valide. Veuillez entrer un entier.")

# Exercice 10 : Combinez Tout
def main():
    try:
        filename = input("Entrez le nom du fichier à lire : ")
        content = read_file(filename)
        if content:
            print("Contenu du fichier :")
            print(content)

        user_input = get_positive_integer()
        print(f"Entier positif saisi : {user_input}")

        division_result = safe_division(user_input, 10)
        print(f"Résultat de la division : {division_result}")

    except Exception as e:
        log_error(f"Une erreur inattendue est survenue : {e}")
        print("Une erreur inattendue s'est produite.")

if __name__ == "__main__":
    main()
