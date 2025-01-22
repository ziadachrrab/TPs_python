class Vehicule:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee

    def afficher_info(self):
        return f"Vehicule : {self.marque} {self.modele}, Annee : {self.annee}"


class Moteur:
    def __init__(self, puissance, type_moteur):
        self.puissance = puissance
        self.type_moteur = type_moteur

    def afficher_moteur(self):
        return f"Moteur : {self.puissance} chevaux, Type : {self.type_moteur}"


class Voiture(Vehicule, Moteur):
    def __init__(self, marque, modele, annee, puissance, type_moteur, nombre_de_places):
        Vehicule.__init__(self, marque, modele, annee)
        Moteur.__init__(self, puissance, type_moteur)
        self.nombre_de_places = nombre_de_places

    def afficher_info(self):
        return (
            f"{Vehicule.afficher_info(self)}, "
            f"{Moteur.afficher_moteur(self)}, "
            f"Nombre de places : {self.nombre_de_places}"
        )


class Moto(Vehicule, Moteur):
    def __init__(self, marque, modele, annee, puissance, type_moteur, type_moto):
        Vehicule.__init__(self, marque, modele, annee)
        Moteur.__init__(self, puissance, type_moteur)
        self.type_moto = type_moto

    def afficher_info(self):
        return (
            f"{Vehicule.afficher_info(self)}, "
            f"{Moteur.afficher_moteur(self)}, "
            f"Type de moto : {self.type_moto}"
        )


# Creation des instances
voiture = Voiture("Toyota", "Corolla", 2022, 120, "Essence", 5)
moto = Moto("Yamaha", "MT-07", 2021, 74, "Essence", "Sport")

# Affichage des informations
print(voiture.afficher_info())
print(moto.afficher_info())