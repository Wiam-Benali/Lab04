class Cabina:
    def __init__(self, codice, num_letti, ponte, prezzo):
        self.codice = codice
        self.num_letti = num_letti
        self.ponte = ponte
        self.prezzo = float(prezzo)
        self.prenotata = False

    def __str__(self):
        return f'{self.codice}, {self.num_letti}, {self.ponte}, {self.prezzo}, {self.prenotata}'




class Ospita_Animali(Cabina):
    def __init__(self, codice, num_letti, ponte, prezzo, num_animali):
        super().__init__(codice, num_letti, ponte, prezzo)
        self.num_animali = int(num_animali)
        self.prezzo = float(prezzo)*(1+0.10*self.num_animali)

    def __str__(self):
        return f'{super().__str__()}, {self.num_animali}'


class Deluxe(Cabina):
    def __init__(self, codice, num_letti, ponte, prezzo, tipologia):
        super().__init__(codice, num_letti, ponte, prezzo)
        self.tipologia = tipologia
        self.prezzo = float(prezzo)*(1.20)

    def __str__(self):
        return f'{super().__str__()}, {self.tipologia}'