class Config:
    _instance = None  # attribut de classe (équivalent d'un attribut static)

    # Création d'un dictionnaire clé/valeur
    _data = {}
    def __new__(cls):
        if cls._instance is None:
            print("Création de l'unique instance Singleton")
            cls._instance = super(Config, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        # Vérifie si self possède un attribut self._init
        # Si l'attribut n'existe pas alors getattr retourne False et dans ce cas on passe à l'étape d'initialisation
        # sinon getattr retourne True et dans ce cas on sort de la méthode
        if getattr(self, "_init", False):
            return
        print("Initialisation")
        self._init = True

        self._data = {}

        # Lecture du fichier en read only
        with open("config.ini", "r") as f:

            # f est un itérable donc on peut boucler dessus
            for ligne in f:
                # suppression des espaces superflus.
                ligne = ligne.strip()

                # Le test permet d'ignorer par exemple les lignes de commentaires
                if "=" in ligne:
                    # Unpacking ou dépaquettage
                    # le paramètre 1 signifie qu'on se limite à une seule coupure, dans le cas où par exemple
                    # la valeur de la clé contiendrait un signe =
                    cle, valeur = ligne.split("=", 1)
                    # On insère la valeur dans le dictionnaire
                    self._data[cle.strip()] = valeur.strip()

    # Méthode permettant de récupérer une propriété du fichier
    def get_propriete(self, key):
        return self._data[key]

if __name__ == "__main__":

    singleton = Config()
    print(singleton.get_propriete("db.url"))

    singleton2 = Config()
    print(singleton2.get_propriete("db.url"))
