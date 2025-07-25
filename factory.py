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

class TransportFactory:
    @staticmethod
    def get_transport(type_):
        if type_ == "bateau":
            return Bateau()
        elif type_ == "camion":
            return Camion()
        else:
            raise ValueError(f"Type de transport inconnu : {type_}")

# Exemple d'utilisation
if __name__ == "__main__":

    transport1 = TransportFactory.get_transport("bateau")
    print(transport1.livrer())

    transport2 = TransportFactory.get_transport("camion")
    print(transport2.livrer())
