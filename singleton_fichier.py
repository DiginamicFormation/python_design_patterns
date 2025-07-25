class ConfigLoader:
    _instance = None

    def __new__(cls, fichier_config="config.txt"):
        if cls._instance is None:
            print(f"Chargement du fichier de configuration : {fichier_config}")
            cls._instance = super(ConfigLoader, cls).__new__(cls)
            cls._instance._config = {}
            cls._instance._charger_config(fichier_config)
        return cls._instance

    def _charger_config(self, fichier_config):
        try:
            with open(fichier_config, "r") as f:
                for ligne in f:
                    ligne = ligne.strip()
                    if ligne and not ligne.startswith("#"):
                        if "=" in ligne:
                            cle, valeur = ligne.split("=", 1)
                            self._config[cle.strip()] = valeur.strip()
        except FileNotFoundError:
            print(f"⚠️ Fichier {fichier_config} introuvable. Dictionnaire vide.")

    def get(self, cle, default=None):
        return self._config.get(cle, default)

    def get_all(self):
        return dict(self._config)
