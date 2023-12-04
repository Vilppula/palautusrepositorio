class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo

    def aseta_arvo(self, arvo):
        self._arvo = arvo

    def hae_arvo(self):
        return self._arvo
    

class BinaariOperaatio:
    def __init__(self, sovelluslogiikka, syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.syote = syote

    def suorita(self):
        pass

class Summa(BinaariOperaatio):
    def __init__(self, sovelluslogiikka, syote):
        super().__init__(sovelluslogiikka, syote)
    
    def suorita(self):
        self.sovelluslogiikka.aseta_arvo(int(self.syote()) + self.sovelluslogiikka.hae_arvo())


class Erotus(BinaariOperaatio):
    def __init__(self, sovelluslogiikka, syote):
        super().__init__(sovelluslogiikka, syote)
    
    def suorita(self):
        self.sovelluslogiikka.aseta_arvo(self.sovelluslogiikka.hae_arvo()-int(self.syote()))

class Nollaus(BinaariOperaatio):
    def __init__(self, sovelluslogiikka, syote):
        super().__init__(sovelluslogiikka, syote)
    
    def suorita(self):
        self.sovelluslogiikka.aseta_arvo(0)
