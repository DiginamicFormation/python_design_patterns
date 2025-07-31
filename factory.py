from abc import ABC, abstractmethod

# Interface Transport
class Transport(ABC):
    @abstractmethod
    def livrer(self):
        pass

# Classe Bateau
class Bateau(Transport):
    def livrer(self):
        return "Livraison par bateau"

# Classe Camion
class Camion(Transport):
    def livrer(self):
        return "Livraison par camion"

class TransportFactoryInterface(ABC):
    @abstractmethod
    def get_transport(type_transport):
        pass
class TransportFactory(TransportFactoryInterface):
    @staticmethod
    def get_transport(type_transport):
        if type_transport == "bateau":
            return Bateau()
        elif type_transport == "camion":
            return Camion()
        else:
            raise ValueError(f"Type de transport inconnu : {type_transport}")

# Exemple d'utilisation
if __name__ == "__main__":

    transport1 = TransportFactory.get_transport("bateau")
    print(transport1.livrer())

    transport2 = TransportFactory.get_transport("camion")
    print(transport2.livrer())
