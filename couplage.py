from abc import ABC, abstractmethod

class Individu:
    def __ini__(self):
        pass

# Interface pour découpler
class IndividuFactoryInterface(ABC):
    @abstractmethod
    def creer_individu(self):
        pass

class IndividuFactoryHomme(IndividuFactoryInterface):
    def creer_individu(self):
        """
        Factory Method pour créer un individu
        avec ses jambes déjà initialisées
        """
        return Individu()

class IndividuFactoryFemme(IndividuFactoryInterface):
    def creer_individu(self):
        """
        Factory Method pour créer un individu
        avec ses jambes déjà initialisées
        """
        return Individu()

class Service:
    def __init__(self, factory: IndividuFactoryInterface):
        """
        Injection de dépendance pour faible couplage
        Le Service ne dépend plus de la Factory concrète
        """
        self.factory = factory

    def traitement(self):
        individu = self.factory.creer_individu()

service = Service(IndividuFactoryHomme())
individu1 = service.traitement();

service = Service(IndividuFactoryFemme())
individu2 = service.traitement();
