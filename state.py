from abc import ABC, abstractmethod
class VideoEtat(ABC):

    @abstractmethod
    def action(self):
        pass

class EtatLecture(VideoEtat):
    def action(self):
        print("Video en lecture")

class EtatPause(VideoEtat):
    def action(self):
        print("Video en pause")

class EtatArret(VideoEtat):
    def action(self):
        print("Video en arrêt")

class Video:

    def __init__(self):
        self._etat = EtatArret()

    @property
    def etat(self):
        return self._etat

    @etat.setter
    def etat(self, valeur):
        self._etat = valeur

    def action(self):
        self._etat.action()

if __name__ == "__main__":

    video = Video()
    video.action()

    video.etat = EtatLecture()
    video.action()

    video.etat = EtatPause()
    video.action()
