
from Base import Base
from NNGestor import NNG
import random

class Be:

    bump_norm = 0
    bump_perc = 0.4
    base = Base(0)

    def __init__(self, NN):
        self.DNC_be = {"elements": ("a", "b"), "counter": 0}
        self.NC_be = list()
        self.nn = NN
        self.nng = NNG(self.nn)


    ## Service functions

    def load(self):
        memory = open('memory/NC_BE.txt', 'r').readlines()
        # rimozione degli \n
        for ind, dex in enumerate(memory):
            memory[ind] = dex.split('\n')[0]
        for x in memory:
                temp = self.DNC_be.copy()
                to_c = x.split(',')
                el = [to_c[0], to_c[1]]
                temp['elements'] = el
                temp['counter'] = float(to_c[2])
                self.NC_be.append(temp)

    def save(self):
        memory = open('memory/NC_be.txt', 'w')
        SAVE = ""
        memory.write(SAVE)
        for x in self.NC_be:
            SAVE = SAVE + f'{x.get("elements")[0]},'
            SAVE = SAVE + f'{x.get("elements")[1]},'
            SAVE = SAVE + f'{x.get("counter")}\n'


        memory.write(SAVE)
        memory.close()



    # Funzione ricerca gruppo di NC
    # ritorna una lista con gli indici dei NC che contengono quella parola, se non ne trova restituisce -1
    # INPUT: NC \\ NN di cui cercare i collegamenti
    # OUTPUT: lista di indici di NC con gli elementi cercati \\ -1 se non trova collegamenti
    def search_nc(self, nn1):
        results = list()
        for i in range(len(self.NC_be)):
            index = self.base.search(self.NC_be[i]['elements'], nn1)
            if index != -1:
                results.append(i)
        if len(results) == 0:
            return -1
        else:
            return results

    # Funzione di massimo
    # cerca la parola con più collegamenti e salva il numero massimo di collegamenti
    # INPUT: NN \\ NC
    # OUTPUT: numero di NC* che ha la parola con più NC*
    def bump_normalizer(self):
        for x in self.nn:
            l_max = self.bump_norm
            t_max = 0
            links = self.search_nc(x)
            if links != -1:
                t_max = len(links)
            if l_max > t_max:
                self.bump_norm = l_max
            elif l_max <= t_max:
                self.bump_norm = t_max

    # Funzione di ricerca singolo NC
    # ritorna l'indice del NC contenente le parole cercate altrimenti restituisce -1
    # INPUT: NC \\ NN1 di cui cercare un NC* con \\ NN2
    def double_search_nc(self, nn1, nn2):
        partial = list()
        for i in range(len(self.NC_be)):
            index = self.base.search(self.NC_be[i]['elements'], nn1)
            if index != -1:
                partial.append(i)
        if len(partial) == 0:
            return -1
        else:
            for j in partial:
                index = self.base.search(self.NC_be[j]['elements'], nn2)
                if index != -1:
                    return j
        return -1

    # Funzione decisione bump
    # funzione che decide se far fare il bump o meno
    # INPUT: numero di NC* di un NN* \\ bump_norm
    # OUTPUT: True \\ False (sottofrma di 0 e 1)
    def bump_switch(self, len):
        norm = (len / self.bump_norm) * self.bump_perc
        res = random.randrange(100)/100
        if res <= norm:
            return True
        elif res > norm:
            return False


    # OUTPUT PRIMARY METHODS

    # Metodo per il salto di neuroni
    # in base a quanti collegamenti ha una parola puo decidere di saltare il collegamento al collegamento successivo
    # INPUT: NN \\ NC \\ NN* da cui decidere se far il salto
    # OUTPUT True \\ False (sottoforma di 0 o 1)
    def bump_method(self, nn1):
        links = self.search_nc(nn1)
        print(links)
        switch = self.bump_switch(len(links))
        return switch

    # Metodo di scelta collegamenti
    # tramite scelta randomica sceglie due parole da accostare e chiede quanto ahnno senso da 1 a 100                       TEMPORANEO (DA RIVEDERE)
    # ritorna il nome della NN corrispondendte al collegamento scelto
    # INPUT: NC \\ NN1 da cui far aprtire il link
    # OUTPUT: NN2 a cui il link arriva da NN1
    def link_method(self, nn1):
        options = self.search_nc(nn1)
        sum = 0
        selector = {"id": 0, "range": (0, 1)}
        selectors = list()
        if options != -1:
            for i in options:
                rang = [sum, sum + self.NC_be[i].get('counter')]
                sum = rang[1]
                sel = selector.copy()
                sel["id"] = i
                sel["range"] = rang
                selectors.append(sel)
                csum = int(sum)
                if csum == 0:
                    csum = 1
            selection = random.randrange(csum)
            found = 0
        else:
            print('error: links not found')
            return 1
        for x in selectors:
            if selection <= x.get("range")[1] and selection >= x.get("range")[0]:
                found = x.get("id")
                break
        to_g = self.NC_be[found].get("elements").copy()
        to_g.remove(nn1)
        to_g = to_g[0]
        to_ret= [nn1, to_g]
        return to_ret

    # INPUT PRIMARY METHODS

    # Metodo di connessione
    # metodo che connette due NN e li associa un valore di connessione
    # INPUT: NN \\ NC \\ NN1 \\ NN2 variabili da associare
    def connection_method(self, nn1, nn2, increment):
        if self.base.search(self.nn, nn1) == -1:
            self.nn.append(nn1)
            self.nng.save()
        if self.base.search(self.nn, nn2) == -1:
            self.nn.append(nn2)
            self.nng.save()
        sr = self.double_search_nc(nn1, nn2)
        if sr == -1:
            new_nc = self.DNC_be.copy()
            comb = [nn1, nn2]
            new_nc['elements'] = comb
            new_nc['counter'] = increment
            self.NC_be.append(new_nc)
        else:
            old = self.NC_be[sr].copy()
            self.NC_be[sr]['counter'] = self.NC_be[sr]['counter'] + increment

    # INPUT SECONDARY METHODS

    # verbo dire
    # fa dire qualcosa di casuale a texty (senza salti)
    def tell(self):
        i = random.randrange(len(self.nn))
        to_ass = self.link_method(self.nn[i])
        return to_ass

    # verbo dire forzato
    # fa dire qualcosa a texty partendo da una parola
    def force_tell(self, nn1, output):
        if self.base.search(self.nn, nn1) == -1:
            self.nn.append(nn1)
            self.nng.save()
            print("TEMPORARY ERROR: the word does not have NC")
        to_ass = self.link_method(nn1)
        print(to_ass)
        if not output:
            return to_ass
        else:
            while self.bump_method(to_ass[1]):
                temp = self.link_method(to_ass[1])
                while temp == nn1:
                    temp = self.link_method(to_ass[1])
                to_ass[1] = temp
                print(temp)
            return to_ass

    # verbo dire libero
    # fa dire qualcosa a texty (bump attivo)
    def free_tell(self, output):
        i = random.randrange(len(self.nn))
        print(self.nn[i])
        return self.force_tell(self.nn[i], output)

    #ritornano in output le cose da dire e il loro livello di connessione

    # OUTPUT SECONDARY METHODS

    # verbo essere
    # crea un collegamento forte
    def be(self, nn1, nn2):
        self.connection_method(nn1, nn2, 1)
        self.save()

    # verbo sembrare
    # crea un collegamento debole
    def seems(self, nn1, nn2):
        self.connection_method(nn1, nn2, 0.5)
        self.save()





