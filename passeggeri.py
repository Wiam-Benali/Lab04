class Passeggero:
    def __init__(self, codice, nome, cognome):
        self.codice = codice
        self.nome = nome
        self.cognome = cognome
        self.cabina_prenotata = ''

    def __str__(self):
        if self.cabina_prenotata != '':
            return f'{self.codice}, {self.nome}, {self.cognome},  Cabina prenotata:  {self.cabina_prenotata}'
        else:
            return f'{self.codice} {self.nome} {self.cognome} Nessuna cabina prenotata'