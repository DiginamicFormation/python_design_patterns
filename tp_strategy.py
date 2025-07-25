from abc import ABC, abstractmethod

class StrategieTri(ABC):
    @abstractmethod
    def trier(self, produits):
        pass

class TriParPrix(StrategieTri):
    def trier(self, produits):
        return sorted(produits, key=lambda p: p.prix)

class TriParNom(StrategieTri):
    def trier(self, produits):
        return sorted(produits, key=lambda p: p.nom.lower())

class TriParScore(StrategieTri):
    def trier(self, produits):
        return sorted(produits, key=lambda p: p.score_nutritionnel)


class Produit:
    def __init__(self, nom, prix, score_nutritionnel):
        self.nom = nom
        self.prix = prix
        self.score_nutritionnel = score_nutritionnel

    def __str__(self):
        return f"{self.nom} - {self.prix}€ - score {self.score_nutritionnel}"

class GestionnaireProduits:
    def __init__(self):
        self.produits = []
        self.strategie = TriParNom()

    def ajouter(self, produit: Produit):
        self.produits.append(produit)

    def afficher(self):
        produits_tries = self.strategie.trier(self.produits)
        for p in produits_tries:
            print(p)

    def changer_strategie(self, nouvelle_strategie: StrategieTri):
        self.strategie = nouvelle_strategie

if __name__ == "__main__":
    produits = [
        Produit("Chips", 2.5, 30),
        Produit("Yaourt", 1.0, 80),
        Produit("Soda", 1.8, 10)
    ]

    gestionnaire = GestionnaireProduits()
    for p in produits:
        gestionnaire.ajouter(p)

    print("\nTri par nom :")
    gestionnaire.afficher()

    print("\nTri par prix :")
    gestionnaire.changer_strategie(TriParPrix())
    gestionnaire.afficher()

    print("\nTri par score nutritionnel :")
    gestionnaire.changer_strategie(TriParScore())
    gestionnaire.afficher()
