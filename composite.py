from abc import ABC, abstractmethod

class Entite(ABC):
    def __init__(self, id: int, nom: str):
        self.id = id
        self.nom = nom

    @abstractmethod
    def afficher(self, indent=0):
        pass

class Personne(Entite):
    def __init__(self, id: int, nom: str, prenom: str, email: str):
        super().__init__(id, nom)
        self.prenom = prenom
        self.email = email

    def afficher(self, indent=0):
        prefix = "  " * indent
        print(f"{prefix}Personne : {self.prenom} {self.nom} ({self.email})")

class Departement(Entite):
    def __init__(self, id: int, nom: str, code: str):
        super().__init__(id, nom)
        self.code = code
        self.entites = []

    def ajouter_entite(self, entite: Entite):
        self.entites.append(entite)

    def afficher(self, indent=0):
        prefix = "  " * indent
        print(f"{prefix}Département : {self.nom} (code: {self.code})")
        for entite in self.entites:
            entite.afficher(indent + 1)

if __name__ == "__main__":
    alice = Personne(1, "Durand", "Alice", "alice@example.com")
    bob = Personne(2, "Martin", "Bob", "bob@example.com")
    claire = Personne(3, "Lemoine", "Claire", "claire@example.com")

    dev = Departement(10, "Développement", "DEV")
    dev.ajouter_entite(bob)

    rh = Departement(20, "Ressources Humaines", "RH")
    rh.ajouter_entite(claire)

    entreprise = Departement(0, "Entreprise", "ENT")
    entreprise.ajouter_entite(dev)  # exemple : Alice fait aussi partie du comité
    entreprise.ajouter_entite(rh)
    entreprise.ajouter_entite(alice)

    print("== Affichage par département ==")
    dev.afficher()
    rh.afficher()

    print("\n== Affichage global ==")
    entreprise.afficher()
