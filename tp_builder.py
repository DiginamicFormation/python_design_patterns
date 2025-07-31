from tp_factory import ElementFactory, TypeElement, Unite


class Categorie:
    def __init__(self, nom):
        self.nom = nom

    def __str__(self):
        return f"Catégorie : {self.nom}"


class Marque:
    def __init__(self, nom):
        self.nom = nom

    def __str__(self):
        return f"Marque : {self.nom}"


class Produit:

    def __init__(self):
        self.nom = None
        self.marque = None
        self.categorie = None
        self.grade = None
        self.ingredients = []
        self.additifs = []
        self.allergenes = []

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, nom):
        self._nom = nom

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, nom):
        self._grade = nom

    @property
    def marque(self):
        return self._marque

    @marque.setter
    def marque(self, marque):
        self._marque = marque

    @property
    def categorie(self):
        return self._categorie

    @categorie.setter
    def categorie(self, categorie):
        self._categorie = categorie

    def __str__(self):
        chaine = f"{self.nom} - {self.categorie} - {self.marque}"
        chaine += f"\nScore : {self.grade}"
        if self.ingredients:
            chaine += "\n  Ingrédients :"
            for ing in self.ingredients:
                chaine += f"\n    - {ing}"

        if self.additifs:
            chaine += "\n  Additifs :"
            for add in self.additifs:
                chaine += f"\n    - {add}"

        if self.allergenes:
            chaine += "\n  Allergènes :"
            for allg in self.allergenes:
                chaine += f"\n    - {allg}"

        return chaine


class ProduitBuilder:
    def __init__(self):
        self.produit = Produit()

    def infos(self, nom, nom_categorie, nom_marque):
        self.produit.nom = nom
        self.produit.categorie = Categorie(nom_categorie)
        self.produit.marque = Marque(nom_marque)
        return self

    def grade(self, grade):
        self.produit.grade = grade
        return self

    def add_ingredient(self, nom, valeur, unite):
        self.produit.ingredients.append(ElementFactory.get_element(TypeElement.INGREDIENT, nom, valeur, unite))
        return self

    def add_additif(self, nom, valeur, unite):
        self.produit.additifs.append(ElementFactory.get_element(TypeElement.ADDITIF, nom, valeur, unite))
        return self

    def add_allergene(self, nom, valeur, unite):
        self.produit.allergenes.append(ElementFactory.get_element(TypeElement.ALLERGENE, nom, valeur, unite))
        return self

    def build(self):
        # Les contrôles de validation du produit
        if not self.produit.nom:
            raise ValueError("Le nom est obligatoire. Veuillez utiliser la méthode infos pour le définir")
        if not self.produit.categorie:
            raise ValueError("La catégorie est obligatoire. Veuillez utiliser la méthode infos pour la définir")
        if not self.produit.marque:
            raise ValueError("La marque est obligatoire. Veuillez utiliser la méthode infos pour la définir")
        if not self.produit.grade:
            raise ValueError(
                "Le grade alimentaire (A à F) est obligatoire. Veuillez utiliser la méthode grade pour le définir")
        if self.produit.grade not in {"A", "B", "C", "D", "E", "F"}:
            raise ValueError("Le grade doit être une lettre de A à F.")
        # au moins 1 ingrédient obligatoire
        if len(self.produit.ingredients) == 0:
            raise ValueError(
                "Le produit doit posséder au moins 1 ingrédient. Veuillez utiliser la méthode add_ingredient pour en ajouter un.")

        return self.produit


if __name__ == "__main__":
    pb = ProduitBuilder()
    produit = (pb.infos("Barre chocolatée", "Confiserie", "Lu")
               .grade("F")
               .add_ingredient("Sucre", 50, Unite.GRAMME)
               .add_ingredient("Chocolat", 30, Unite.GRAMME)
               .add_ingredient("Lait", 20, Unite.GRAMME)
               .add_additif("E111", 14, Unite.MILLIGRAMME)
               .build())
    print(produit)
