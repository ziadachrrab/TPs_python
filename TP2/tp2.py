# ex1

class dog:
    def __init__(self, name, age, race):
        self.name = name,
        self.age = age
        self.race = race

    def aboyer(self):
        print("Woof!")

chien = dog("Jack", 3, "Pitbulll")
chien.aboyer()

# ------------------------------------------------------------------------------------------------------------------------------------------------

#  ex2

class Voiture:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee

    def afficher_info(self):
        print(f"Voiture: {self.marque} {self.modele}, Année: {self.annee}")

voiture1 = Voiture("Toyota", "Corolla", 2020)
voiture2 = Voiture("Ford", "Mustang", 2019)
voiture1.afficher_info()
voiture2.afficher_info()

# ------------------------------------------------------------------------------------------------------------------------------------------------

#  ex3

class CompteBancaire:
    def __init__(self, titulaire, solde=0):
        self.titulaire = titulaire
        self.solde = solde

    def deposer(self, montant):
        self.solde += montant
        print(f"Dépôt de {montant} effectué. Nouveau solde: {self.solde}")

    def retirer(self, montant):
        if montant <= self.solde:
            self.solde -= montant
            print(f"Retrait de {montant} effectué. Nouveau solde: {self.solde}")
        else:
            print("Fonds insuffisants pour le retrait.")

    def afficher_solde(self):
        print(f"Solde actuel: {self.solde}")

compte = CompteBancaire("Alice", 1000)
compte.afficher_solde()
compte.deposer(500)
compte.retirer(200)
compte.retirer(1500)
# ------------------------------------------------------------------------------------------------------------------------------------------------

# ex4

class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.amis = []

    def se_presenter(self):
        print(f"Bonjour, je suis {self.prenom} {self.nom}, j'ai {self.age} ans.")

    def ajouter_ami(self, ami):
        self.amis.append(ami)
        print(f"{ami.prenom} a été ajouté à la liste des amis.")

    def afficher_amis(self):
        print("Mes amis :")
        for ami in self.amis:
            print(f"{ami.prenom} {ami.nom}")

class Etudiant(Personne):
    def __init__(self, nom, prenom, age, matricule):
        super().__init__(nom, prenom, age)
        self.matricule = matricule

    def etudier(self):
        print(f"{self.prenom} {self.nom} est en train d'étudier.")

etudiant = Etudiant("Dupont", "Jean", 20, "123456")
etudiant.se_presenter()
etudiant.etudier()
# ------------------------------------------------------------------------------------------------------------------------------------------------

#  ex5

class Animal:
    def faire_du_bruit(self):
        pass

class Chien(Animal):
    def faire_du_bruit(self):
        print("Le chien aboie.")

class Chat(Animal):
    def faire_du_bruit(self):
        print("Le chat miaule.")
        
chien = Chien()
chat = Chat()
chien.faire_du_bruit()
chat.faire_du_bruit()
# ------------------------------------------------------------------------------------------------------------------------------------------------

# ex6

class Rectangle:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def calculer_surface(self):
        return self.largeur * self.hauteur

    def calculer_perimetre(self):
        return 2 * (self.largeur + self.hauteur)

rectangle = Rectangle(5, 10)
print(f"Surface: {rectangle.calculer_surface()}")
print(f"Périmètre: {rectangle.calculer_perimetre()}")
# ------------------------------------------------------------------------------------------------------------------------------------------------

# ex7

class Livre:
    def __init__(self, titre, auteur, annee_publication):
        self.titre = titre
        self.auteur = auteur
        self.annee_publication = annee_publication

class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)
        print(f"Livre '{livre.titre}' ajouté à la bibliothèque.")

    def afficher_livres(self):
        for livre in self.livres:
            print(f"{livre.titre} par {livre.auteur} ({livre.annee_publication})")

bibliotheque = Bibliotheque()
livre1 = Livre("1984", "George Orwell", 1949)
livre2 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 1943)
bibliotheque.ajouter_livre(livre1)
bibliotheque.ajouter_livre(livre2)
bibliotheque.afficher_livres()

# ex8
personne1 = Personne("Dupont", "Jean", 30)
personne2 = Personne("Martin", "Alice", 28)
personne1.ajouter_ami(personne2)
personne1.afficher_amis()

        