# ex1

from abc import ABC, abstractmethod
import math

class forme(ABC):
    @abstractmethod
    def calculer_surface(self):
        pass

class cercle(forme):
    def __init__(self, rayon):
        self.rayon = rayon

    def calculer_surface(self):
        math.pi * (self.rayon ** 2)

class rectangle(forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def calculer_surface(self):
      return self.largeur * self.hauteur
        
# --------------------------------------------------------------------------

# ex2        

class personne:
    def _init_(self, nom, prenom, age):
        self._nom = nom
        self._prenom = prenom
        self._age = age

    def get_nom(self):
        return self._nom
    
    def set_nom(self, nom):
      self.__nom = nom

    def get_prenom(self):
      return self.__prenom

    def set_prenom(self, prenom):
      self.__prenom = prenom

    def get_age(self):
      return self.__age

    def set_age(self, age):
      if age >= 0:
          self.__age = age
      else:
          raise ValueError("L'âge ne peut pas être négatif.")

# --------------------------------------------------------------------------

# ex3

def afficher_surface(formes):
  for forme in formes:
      print(f"La surface est : {forme.calculer_surface()}")

formes = [Cercle(5), Rectangle(4, 6)]
afficher_surface(formes)

# --------------------------------------------------------------------------

# ex4

class Produit:
  def __init__(self, nom, prix):
      self.__nom = nom
      self.__prix = prix

  def get_nom(self):
      return self.__nom

  def get_prix(self):
      return self.__prix

  def appliquer_remise(self, pourcentage):
      if self.__prix > 100:
          self.__prix -= self.__prix * (pourcentage / 100)

# --------------------------------------------------------------------------

# ex5

class Employe:
  def __init__(self, nom, prenom, salaire):
      self.nom = nom
      self.prenom = prenom
      self.salaire = salaire

class Manager(Employe):
  def __init__(self, nom, prenom, salaire):
      super().__init__(nom, prenom, salaire)
      self.employes_supervises = []

  def ajouter_employe(self, employe):
      self.employes_supervises.append(employe)

  def afficher_employes(self):
      for employe in self.employes_supervises:
          print(f"{employe.nom} {employe.prenom}, Salaire: {employe.salaire}")

# --------------------------------------------------------------------------

# ex6

class Commande:
  def __init__(self, produit, quantite):
      self.produit = produit
      self.quantite = quantite

class Panier:
  def __init__(self):
      self.commandes = []

  def ajouter_commande(self, commande):
      self.commandes.append(commande)

  def calculer_total(self):
      total = 0
      for commande in self.commandes:
          total += commande.produit.get_prix() * commande.quantite
      return total

# --------------------------------------------------------------------------

# ex7

class Vehicule(ABC):
  @abstractmethod
  def deplacer(self):
      pass

class Voiture(Vehicule):
  def deplacer(self):
      return "La voiture roule sur la route."

class Bicyclette(Vehicule):
  def deplacer(self):
      return "La bicyclette avance en pédalant."

