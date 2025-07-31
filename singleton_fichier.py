class ConfigLoader:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print(f"Création de l'instance")
            cls._instance = object.__new__(cls)
            cls._instance.__initialized=False
        return cls._instance

    def __init__(self):
        if self.__initialized:
            return
        print(f"Chargement du fichier de configuration")
        self.__initialized = True
        self.__config={}
        self.__charger_fichier_config()

    def __charger_fichier_config(self):
        try:
            with open("config.ini", "r") as f:
                for ligne in f:
                    ligne = ligne.strip()
                    if ligne and not ligne.startswith("#"):
                        if "=" in ligne:
                            cle, valeur = ligne.split("=", 1)
                            self.__config[cle.strip()] = valeur.strip()
        except FileNotFoundError:
            print(f"Fichier config.ini introuvable. Dictionnaire vide.")

    def get(self, cle):
        return self.__config.get(cle)

if __name__ == "__main__":
    c1 = ConfigLoader()
    print(c1.get("db.url"))

    c2 = ConfigLoader()
    print(c2.get("db.url"))
