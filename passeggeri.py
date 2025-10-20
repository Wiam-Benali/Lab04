class Passeggero:
    def __init__(self, codice, nome, cognome):
        self.codice = codice
        self.nome = nome
        self.cognome = cognome
        self.cabina_prenotata = ''

    def __repr__(self):
        if self.cabina_prenotata != '':
            return f'Codice = {self.codice}, Nome = {self.nome}, Coognome = {self.cognome},  Cabina prenotata:  {self.cabina_prenotata}'
        else:
            return f'Codice = {self.codice}, Nome = {self.nome}, Coognome = {self.cognome}, Nessuna cabina prenotata'