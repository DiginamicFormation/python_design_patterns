class Utilisateur:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def infos(self):
        return f"{self.nom} {self.prenom}"

# ce que vous écrivez
u1 = Utilisateur("LEE", "Lou")
print(u1.infos())

# ce que fais l'interpréteur Python
u2 = object.__new__(Utilisateur)        # création de l'instance
Utilisateur.__init__(u2, "LEE", "Lo")   # raison pour laquelle il existe le paramètre self
print(Utilisateur.infos(u2))            # raison pour laquelle il existe le paramètre self
