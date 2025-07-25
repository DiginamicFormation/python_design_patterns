class Singleton:
    _instance = None  # attribut de classe (équivalent d'un attribut static)

    def __new__(cls):
        if cls._instance is None:
            print("Création de l'unique instance Singleton")
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        # Cette méthode peut être appelée plusieurs fois,
        # mais l'instance est unique
        self.valeur = 42

if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()

    print(f"Valeur dans s1 : {s1.valeur}")
    s2.valeur = 99
    print(f"Valeur dans s1 après modification via s2 : {s1.valeur}")
    print(f"s1 est s2 ? {s1 is s2}")
