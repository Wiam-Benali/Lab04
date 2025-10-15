import csv
from cabine import Cabina, Ospita_Animali, Deluxe
from passeggeri import Passeggero
from operator import attrgetter


class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self._nome = nome
        self.cabine = []
        self.passeggeri = []

    def __str__(self):
        return (f'{self._nome} \n{self.cabine} {self.passeggeri}')

    """Aggiungere setter e getter se necessari"""
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nuovo_nome):
        self._nome = nuovo_nome

    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        try:
            input_file = open(file_path,'r')
            reader = csv.reader(input_file)
            for riga in reader:
                codice = riga[0]
                if codice.startswith('CAB'):
                    if len(riga) == 5:
                        if riga[-1].isdigit():
                            codice, num_letti, ponte, prezzo, num_animali = riga
                            cabina = Ospita_Animali(codice, num_letti, ponte, prezzo, num_animali)
                        else:
                            codice, num_letti, ponte, prezzo, tipologia = riga
                            cabina = Deluxe(codice, num_letti, ponte, prezzo, tipologia)
                    else:
                        codice, num_letti, ponte, prezzo = riga
                        cabina = Cabina(codice, num_letti, ponte, prezzo)
                    self.cabine.append(cabina)
                else:
                    codice, nome, cognome = riga
                    passeggero = Passeggero(codice, nome, cognome)
                    self.passeggeri.append(passeggero)
            input_file.close()

            for c in self.cabine:
                print(c)
            for p in self.passeggeri:
                print(p)

        except FileNotFoundError:
            print("File not found")


    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        trovato_cabina = False
        for c in self.cabine:
            if c.codice.lower() == codice_cabina.strip().lower() and not c.prenotata:
                trovato_cabina = True

                passeggero_valido = False
                for p in self.passeggeri:
                    if p.codice.lower() == codice_passeggero.strip().lower() and p.cabina_prenotata == '':
                        passeggero_valido = True
                        c.prenotata = True
                        p.cabina_prenotata = codice_cabina.upper()


        if not trovato_cabina or not passeggero_valido:
            raise Exception('Cabina non trovato o passeggero non valido')


    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        return sorted(self.cabine, key=attrgetter('prezzo'))


    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        for p in self.passeggeri:
                print(p)

