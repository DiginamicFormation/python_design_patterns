class StringBuilder:
    def __init__(self):
        self.str=""

    def append(self, objet):
        if objet is not None:
            self.str+=objet.__str__()
        return self

    def build(self):
        return self.str

sb = StringBuilder()
chaine = (sb.append("Coucou")
           .append(8)
           .append("dljihd")
           .build())
print(chaine)
