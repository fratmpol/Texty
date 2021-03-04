class Base:

    def __init__(self, test):
        self.i = test

    # Funzione ricerca lista
    # restituisce l'indice dell'elemento della lista cercato, se nonlo trova restituisce -1
    # INPUT: lista in cui cercare \\ elemeto da cercare
    # OUTPUT: indice dell'emento cercato nella lista \\ -1 se non trova l'elemento
    def search(self, list_in = None, to_search=None ):
        for i in range(len(list_in)):
            if list_in[i] == to_search:
                return i
        return -1

    # Funzione conversione true false
    # funzione che restituisce true or false in base ad un input testuale
    # INPUT: testo da conertire
    # OUTPUT: True \\ False
    def tf(self, input):
        if input == "True" or input == "ON":
            return True
        if input == "False" or input == "OFF":
            return False