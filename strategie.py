from abc import ABC, abstractmethod

class StrategieCalcul(ABC):
    @abstractmethod
    def calculer(self, produit) -> float:
        pass

class StrategieCalories(StrategieCalcul):
    def calculer(self, produit):
        return produit.calories / 100  # exemple simplifié

class StrategieLipides(StrategieCalcul):
    def calculer(self, produit):
        return produit.lipides * 2  # exemple fictif

class StrategieCalculFactory:

    @staticmethod
    def get_type(type_):
        if type_ == "DEFAUT":
            return StrategieCalories()
        elif type_ == "LIPIDES":
            return StrategieLipides()
        else:
            raise Exception("type de stratégie inconnu")

class Produit:
    def __init__(self, nom, calories, lipides):
        self.nom = nom
        self.calories = calories
        self.lipides = lipides

class CalculScoreNutritif:
    def __init__(self):
        self.strategie = StrategieCalculFactory.get_type("DEFAUT")

    def calculer(self, produit: Produit) -> float:
        return self.strategie.calculer(produit)

    def modifier_strategie(self, type_):
        self.strategie = StrategieCalculFactory.get_type(type_)

if __name__ == "__main__":

    calcul = CalculScoreNutritif()
    produit = Produit("Pizza", 1000, 500)

    print(calcul.calculer(produit))
    calcul.modifier_strategie("LIPIDES")
    print(calcul.calculer(produit))
