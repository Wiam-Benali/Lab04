class Cabina:
    def __init__(self, codice, num_letti, ponte, prezzo):
        self.codice = codice
        self.num_letti = num_letti
        self.ponte = ponte
        self.prezzo = float(prezzo)
        self.prenotata = False

    def __repr__(self):
        if not self.prenotata:
            return f'Codice = {self.codice}, Letti = {self.num_letti}, Ponte = {self.ponte},Prezzo = {self.prezzo}, Cabina non prenotata'
        else:
            return f'Codice = {self.codice}, Letti = {self.num_letti}, Ponte = {self.ponte},Prezzo = {self.prezzo}, Cabina prenotata'





class Ospita_Animali(Cabina):
    def __init__(self, codice, num_letti, ponte, prezzo, num_animali):
        super().__init__(codice, num_letti, ponte, prezzo)
        self.num_animali = int(num_animali)
        self.prezzo = float(prezzo)*(1+0.10*self.num_animali)

    def __repr__(self):
        return f'{super().__repr__()}, Num. Animali =  {self.num_animali}'


class Deluxe(Cabina):
    def __init__(self, codice, num_letti, ponte, prezzo, tipologia):
        super().__init__(codice, num_letti, ponte, prezzo)
        self.tipologia = tipologia
        self.prezzo = float(prezzo)*(1.20)

    def __repr__(self):
        return f'{super().__repr__()}, Tipologia = {self.tipologia}'