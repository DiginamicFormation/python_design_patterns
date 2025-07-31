from abc import ABC, abstractmethod
from enum import Enum

class Unite(Enum):
    MICROGRAMME = "micro-grammes"
    MILLIGRAMME = "milligrammes"
    GRAMME = "grammes"

class ElementValidator:
    @staticmethod
    def validate(attribut, valeur, types):
        if not isinstance(valeur, types):
            raise TypeError(f"Le champ '{attribut}' doit être de type : {types}.")

class Element(ABC):
    def __init__(self, nom: str, valeur: float, unite: Unite):
        ElementValidator.validate("nom", nom, str)
        ElementValidator.validate("valeur", valeur, (int, float))
        ElementValidator.validate("unite", unite, Unite)
        self.nom = nom
        self.valeur = valeur
        self.unite = unite

    def __str__(self):
            return f"{self.nom} - Quantité : {self.valeur} {self.unite.value}"

class Ingredient(Element):
    def __str__(self):
        return f"Ingrédient : "+super().__str__()

class Allergene(Element):
    def __str__(self):
        return f"Allergène : "+super().__str__()

class Additif(Element):
    def __str__(self):
        return f"Additif : "+super().__str__()

class TypeElement(Enum):
    INGREDIENT = 1
    ADDITIF = 2
    ALLERGENE = 3

class ElementFactory:

    @staticmethod
    def get_element(type_element: TypeElement, nom, valeur, unite: Unite):
        if type_element == TypeElement.INGREDIENT:
            return Ingredient(nom, valeur, unite)
        elif type_element == TypeElement.ALLERGENE:
            return Allergene(nom, valeur, unite)
        elif type_element == TypeElement.ADDITIF:
            return Additif(nom, valeur, unite)
        else:
            raise ValueError(f"Type d'élément inconnu : {type_element}")

if __name__ == "__main__":
    sucre = ElementFactory.get_element(TypeElement.INGREDIENT, "Sucre", 25.5, Unite.GRAMME)
    sesame = ElementFactory.get_element(TypeElement.ALLERGENE, "Graines de sésame", 10, Unite.MILLIGRAMME)
    additif = ElementFactory.get_element(TypeElement.ADDITIF, "Colorant alimentaire", 120, Unite.MICROGRAMME)

    print(sucre)
    print(sesame)
    print(additif)

    try:
        additif2 = ElementFactory.get_element(None, "Colorant alimentaire", 120, Unite.MICROGRAMME)
    except ValueError as e:
        print(e)
