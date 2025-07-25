# Dépendances simples
class Ingredient:
    def __init__(self, nom, masse):
        self.nom = nom
        self.masse = masse

    def __repr__(self):
        return f"{self.nom} ({self.masse}g)"

class Additif:
    def __init__(self, nom):
        self.nom = nom

    def __repr__(self):
        return self.nom

class Allergene:
    def __init__(self, nom):
        self.nom = nom

    def __repr__(self):
        return self.nom

# Produit final
class Produit:
    def __init__(self):
        self.nom = None
        self.marque = None
        self.categorie = None
        self.ingredients = []
        self.additifs = []
        self.allergenes = []
        self.score_nutritionnel = None

    def __repr__(self):
        return (f"Produit(nom={self.nom}, marque={self.marque}, catégorie={self.categorie},\n"
                f"        ingrédients={self.ingredients},\n"
                f"        additifs={self.additifs},\n"
                f"        allergènes={self.allergenes},\n"
                f"        score_nutritionnel={self.score_nutritionnel})")

# Builder avec interface fluide
class ProduitBuilder:
    def __init__(self):
        self._produit = Produit()

    def definir_infos(self, nom, marque, categorie):
        self._produit.nom = nom
        self._produit.marque = marque
        self._produit.categorie = categorie
        return self  # fluent interface

    def ajout_ingredient(self, nom_ingredient, masse):
        self._produit.ingredients.append(Ingredient(nom_ingredient, masse))
        return self

    def ajout_additif(self, nom_additif):
        self._produit.additifs.append(Additif(nom_additif))
        return self

    def ajout_allergene(self, nom_allergene):
        self._produit.allergenes.append(Allergene(nom_allergene))
        return self

    def score_nutritionnelle(self, score):
        self._produit.score_nutritionnel = score
        return self

    def build(self):
        return self._produit

# Exemple d'utilisation
if __name__ == "__main__":
    builder = ProduitBuilder()
    produit = (builder
        .definir_infos("Pizza 4 fromages", "ItaliDelice", "Plats préparés")
        .ajout_ingredient("Fromage", 120)
        .ajout_ingredient("Tomate", 80)
        .ajout_additif("E250")
        .ajout_allergene("Lactose")
        .score_nutritionnelle("C")
        .build()
    )

    print(produit)
