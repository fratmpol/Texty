# Texty base

# texty è un'intelligenza artificiale che vuile simulare il funzionamento di base del cervello umano.
# Lo sviluppo e i diritti sono riservati in toto a Francesco Polcri





# FUNCTION WAY (WORKING)



# import random
#
#
#
# ## Variabili di servizio
#
# # variabili di bump
#
#       # aggiornato ad ogni sessione
#
# # lista variabili controllo amministratore
# admin_var=[True, True, False, True, True, True]
# # 0: allow bump
# # 1: print della memoria di texty in apertura
# # 2: allow to modify NC and NN if bump happens
# # 3: show if a bump happens
# # 4: if a NC* is modified print it
# # 5: print NN and NC after every interaction
#
#
#
# ## VARIABILI PRINCIPALI
#
# # NN list (Network Neurons)
# NN = list()
#
# # NC definition
# DNC = {"elements": ("a", "b"), "counter": 0}
#
# # NC list (Network Connections)
# NC = list()
#
#
#
#
#
#
#
# ## FUNZIONI DI SAVE AND LOAD DELLA MEMORIA ###
#
# def load(NN, NC):
#     memory = open('memory/memory.txt', 'r').readlines()
#     # rimozione degli \n
#     for ind, dex in enumerate(memory):
#         memory[ind] = dex.split('\n')[0]
#     switch = 0
#     for x in memory:
#         if switch == 0 and x != "//NC":
#             NN.append(x)
#         if switch == 1 and x != "//end":
#             temp = DNC.copy()
#             to_c = x.split(',')
#             el = [to_c[0], to_c[1]]
#             temp['elements'] = el
#             temp['counter'] = int(to_c[2])
#             NC.append(temp)
#         if x == '//NC':
#             switch = 1
#         if x == "//end":
#             return NN, NC
#
# def save(NN, NC):
#     SAVE = ""
#     for x in NN:
#         SAVE = SAVE + f'{x}\n'
#     SAVE = SAVE + f'//NC\n'
#     for x in NC:
#         SAVE = SAVE + f'{x.get("elements")[0]},'
#         SAVE = SAVE + f'{x.get("elements")[1]},'
#         SAVE = SAVE + f'{x.get("counter")}\n'
#     SAVE = SAVE + f'//end\n'
#
#     memory = open('memory/memory.txt', 'w')
#     memory.write(SAVE)
#     memory.close()
#
#
#
#
#
#
#
# ### FUNZIONI DI SERVIZIO ###
#
# # Funzione conversione true false
# # funzione che restituisce true or false in base ad un input testuale
# # INPUT: testo da conertire
# # OUTPUT: True \\ False
# def tf(input):
#     if input == "True" or input == "ON":
#         return True
#     if input == "False" or input == "OFF":
#         return False
#
# # Funzione ricerca lista
# # restituisce l'indice dell'elemento della lista cercato, se nonlo trova restituisce -1
# # INPUT: lista in cui cercare \\ elemeto da cercare
# # OUTPUT: indice dell'emento cercato nella lista \\ -1 se non trova l'elemento
# def search(list_in, to_search):
#     for i in range(len(list_in)):
#         if list_in[i] == to_search:
#             return i
#     return -1
#
# # Funzione ricerca gruppo di NC
# # ritorna una lista con gli indici dei NC che contengono quella parola, se non ne trova restituisce -1
# # INPUT: NC \\ NN di cui cercare i collegamenti
# # OUTPUT: lista di indici di NC con gli elementi cercati \\ -1 se non trova collegamenti
# def search_nc(nc, nn1):
#     results = list()
#     for i in range(len(nc)):
#         index = search(nc[i]['elements'], nn1)
#         if index != -1:
#             results.append(i)
#     if len(results) == 0:
#         return -1
#     else:
#         return results
#
# # Funzione di ricerca singolo NC
# # ritorna l'indice del NC contenente le parole cercate altrimenti restituisce -1
# # INPUT: NC \\ NN1 di cui cercare un NC* con \\ NN2
# def double_search_nc(nc, nn1, nn2):
#     partial = list()
#     for i in range(len(nc)):
#         index = search(nc[i]['elements'], nn1)
#         if index != -1:
#             partial.append(i)
#     if len(partial) == 0:
#         return -1
#     else:
#         for j in partial:
#             index = search(nc[j]['elements'], nn2)
#             if index != -1:
#                 return j
#     return -1
#
# # Funzione di massimo
# # cerca la parola con più collegamenti e salva il numero massimo di collegamenti
# # INPUT: NN \\ NC
# # OUTPUT: numero di NC* che ha la parola con più NC*
# def bump_p(nn, nc):
#     max = 0
#     for x in nn:
#         l_max = max
#         t_max = 0
#         links = search_nc(nc, x)
#         if links != -1:
#             t_max = len(links)
#         if l_max > t_max:
#             max = l_max
#         elif l_max <= t_max:
#             max = t_max
#     return max
#
# # Funzione decisione bump
# # funzione che decide se far fare il bump o meno
# # INPUT: numero di NC* di un NN* \\ bump_norm
# # OUTPUT: True \\ False (sottofrma di 0 e 1)
# def bump_switch(len, Norm, bump_perc):
#     res  = 0
#     norm = (len/Norm)*bump_perc
#     a  = random.randrange(100)
#     res = a/100
#     if res <= norm:
#         return True
#     elif res > norm:
#         return False
#
# # Funzione riconnessione
# # se viene fatto un bump si chiede all'utente se ha senso
# # INPUT: NN \\ NC \\ NN1 \ NN2 (NN* di cui controllare il senso del collegamento)
# def bump_check(nn, nc, nn1, nn2, bump_perc):
#     print("does the connection make sense ? \n>>")
#     res = input()
#     #                                                                                                                   TEMPORANEO (DA RIVEDERE)
#     if res == "yes":
#         connection_method(nn, nc, nn1, nn2, bump_perc)
#
#
#
#
#
#
# ### METODI GENERICI ###
#
# # Metodo di connessione
# # metodo che connette due NN e li associa un valore di connessione
# # INPUT: NN \\ NC \\ NN1 \\ NN2 variabili da associare
# def connection_method(nn, nc, nn1, nn2, increment):
#     if search(nn, nn1) == -1:
#         nn.append(nn1)
#     if search(nn, nn2) == -1:
#         nn.append(nn2)
#
#     sr = double_search_nc(nc, nn1, nn2)
#     if sr == -1:
#         new_nc = DNC.copy()
#         comb = [nn1, nn2]
#         new_nc['elements'] = comb
#         new_nc['counter'] = increment
#         nc.append(new_nc)
#         if admin_var[3]:
#             print(f'nothing -> new:{new_nc}')
#     else:
#         old = nc[sr].copy()
#         nc[sr]['counter'] = nc[sr]['counter'] + increment
#         if admin_var[3]:
#             print(f'old:{old} -> new:{nc[sr]}')
#
# # Metodo per il salto di neuroni
# # in base a quanti collegamenti ha una parola puo decidere di saltare il collegamento al collegamento successivo
# # INPUT: NN \\ NC \\ NN* da cui decidere se far il salto
# # OUTPUT True \\ False (sottoforma di 0 o 1)
# def bump_method(nn, nc, nn1,norm_bump, bump_perc):
#     links = search_nc(nc, nn1)
#     switch = bump_switch(len(links), norm_bump, bump_perc)
#     return switch
#
# def link_method(nc, nn1):
#     options = search_nc(nc, nn1)
#     sum = 0
#     selector = {"id": 0, "range": (0, 1)}
#     selectors = list()
#     #print(options)
#     for i in options:
#         rang = [sum, sum + nc[i].get('counter')]
#         sum = rang[1]
#         sel = selector.copy()
#         sel["id"] = i
#         sel["range"] = rang
#         selectors.append(sel)
#     selection = random.randrange(sum)
#     found = 0
#     for x in selectors:
#         if selection <= x.get("range")[1] and selection >= x.get("range")[0]:
#             found = x.get("id")
#             break
#     to_g = nc[found].get("elements").copy()
#     to_g.remove(nn1)
#     to_g = to_g[0]
#     return to_g
#
#
# ### Metodi specifici ###
#
# # verbo essere
# # crea un collegamento forte
# def be(nn, nc, nn1, nn2):
#     connection_method(nn, nc, nn1, nn2, 1)
#
# # verbo sembrare
# # crea un collegamento debole
# def seems(nn, nc, nn1, nn2):
#     connection_method(nn, nc, nn1, nn2, 0.5)
#
# # verbo dire
# # fa dire qualcosa di casuale a texty (senza salti)
# def tell(nn, nc, output):
#     i = random.randrange(len(nn))
#     to_ass = link_method(nc,nn[i])
#     if output:
#         print(f'{nn[i]} is {to_ass}')
#
# # verbo dire forzato
# # fa dire qualcosa a texty partendo da una parola
# def force_tell(nn, nc, nn1, output, norm_bump, bump_perc):
#     to_ass = link_method(nc, nn1)
#     if not output:
#         print(f'{nn1} is {to_ass}')
#     else:
#         while bump_method(nn, nc, to_ass, norm_bump, bump_perc):
#             temp = link_method(nc, to_ass)
#             while temp == nn1:
#                 temp = link_method(nc, to_ass)
#             to_ass = temp
#         print(f'{nn1} is {to_ass}')
#     if admin_var[2] == True:
#         bump_check(nn, nc, nn1, to_ass, bump_perc)
#
# # verbo dire libero
# # fa dire qualcosa a texty (bump attivo)
# def free_tell(nn, nc, norm_bump, bump_perc):
#     i = random.randrange(len(nn))
#     force_tell(nn, nc, nn[i], admin_var[0], norm_bump, bump_perc)
#
#
#
#
#
#
#
# ### SELETTORI
#
# # Selettore Primario
# # scompone input e reindirizza a selettori secondari
# def refractor(input, norm_bump, bump_perc):
#     to_ret = list()
#     output = input.split(" ")
#     if "\is" in output:
#         refractor_be(output)
#     elif "\seems" in output:
#         refractor_seems(output)
#     elif "\Tell" in output:
#         refractor_tell()
#     elif "\Ftell" in output:
#         refractor_force_tell(output, norm_bump, bump_perc)
#     elif "\Free" in output:
#         refractor_free_tell(norm_bump, bump_perc)
#     elif "\Admin" in output:
#         to_ch = refractor_admin_commands(output[1], bump_perc, norm_bump)
#         if len(to_ch) == 2:
#             bump_perc = to_ch[0]
#             to_ret.append(bump_perc)
#     elif "\exit"in output:
#         print("Bye Bye User :)")
#
#
#     # spazio per altri eventuali refrattori
#
#     else:
#         print("user error: none method recognised")
#     to_ret.append(0)
#     return to_ret
#
#
# # Selettori Secondari
# # reindirizzano ai metodi
#
# def refractor_be(output):
#     ref = output.index("\is")
#     be(NN, NC, output[ref - 1], output[ref + 1])
#
# def refractor_seems(output):
#     ref = output.index("\seems")
#     seems(NN, NC, output[ref - 1], output[ref + 1])
#
# def refractor_tell():
#     tell(NN, NC, True)
#
# def refractor_force_tell(output, norm_bump, bump_perc):
#     ref = output.index("\Ftell")
#     #controllo giusto utilizzo del comando
#     if ref == 0:
#         print("user error: word before \Ftell missing")
#         return 1
#     # controllo temporaneo se non esiste parola in memoria                                                              TEMPORANEO
#     if search(NN, output[ref-1]) == -1:
#         NN.append(output[ref-1])
#         print("TEMPORARY ERROR: the word does not have NC")
#         return 2
#     force_tell(NN, NC, output[ref-1], admin_var[0], norm_bump, bump_perc)
#
# def refractor_free_tell(norm_bump, bump_perc):
#     free_tell(NN, NC, norm_bump, bump_perc)
#
# def refractor_admin_commands(output, bump_perc, n_bump):
#     to_ret=list()
#     command = output.split(':')
#     if command[0] == "allow_bump":
#         admin_var[0] = tf(command[1])
#     if command[0] == "sart_nn":
#         admin_var[1] = tf(command[1])
#     if command[0] == "bump_norm":
#         print(f'admin_return: bump_norm = {n_bump}')
#     if len(command) == 1:
#         print('user error: missing parameter')
#     elif command[0] == "bump_percentage" and command[1] == "show":
#         print(f'admin_return: bump_percentage = {bump_perc}')
#     elif command[0] == "bump_percentage" and command[1] == "modify":
#         print(f'admin: current bump_percetage is {bump_perc}\nadmin: insert the new percenrage:')
#         new = -1
#         while new <= 0 or new >=1 :
#             print("admin: >>")
#             new = float(input())
#         to_ret.append(new)
#     if command[0] == "bump_modify":
#         admin_var[2] = tf(command[1])
#     if command[0] == "show_bump":
#         admin_var[3] = tf(command[1])
#     if command[0] == "print_mod_nc":
#         admin_var[4] = tf(command[1])
#     if command[0] == "interaction_nn":
#         admin_var[5] = tf(command[1])
#     to_ret.append(0)
#     return to_ret
#
#     #spazio per altri comadidi sistema
#
#
#
#
#
#
#
#
# def main():
#
#     load(NN, NC)
#
#     if admin_var[1] == True:
#         print(NN)
#         print(NC)
#     # normalizzazione del bump
#
#     bump_perc = 0.4
#     n_bump = bump_p(NN, NC)
#
#
#     print("hello user \n\n")
#
#     inp = ""
#
#     while inp != "\exit":
#         print(">> ")
#         inp = input()
#         returns = refractor(inp,n_bump, bump_perc)
#         if len(returns) == 2:
#             bump_perc = returns[0]
#         if admin_var[5]:
#             print(NN, NC)
#
#     save(NN, NC)


# CLASS WAY (WIP)

from Read import Read
from InternalProcessing import IP
from Tell import Tell
from NNGestor import NNG
from Be import Be

def main(inp):

    # NN list (Network Neurons)
    NN = list()

    nng = NNG(NN)
    nng.load()
    NN = nng.nn # ce l'hai già in NN riga 450
    #print(NN)
    be = Be(NN)
    be.load()
    #print(be.NC_be)
    be.bump_normalizer()
    #print(be.bump_norm)

    read = Read()
    ip = IP(NN, be)
    tell = Tell()
    ans = ">> "

    if inp != "\exit":
        read.input = inp
        read.read()
        ip.int_input = read.IP_int_output
        ip.out_input = read.IP_out_output
        ip.processing()
        tell.input = ip.tell_output
        ans = ">> "+str(tell.answer())
        read.clear()
        ip.clear()
        tell.clear()
    return ans

from flask import Flask, flash, render_template, url_for, request, redirect, send_from_directory

app = Flask(__name__)

# Home page with upload
@app.route('/', methods=['GET', 'POST'])
def refresh_results():
    if request.method == 'POST':
        if request.form["text"] != "":
            inp = request.form["text"]
            return render_template('home.html', main=str(">> "+inp+"\n")+str(main(inp)), inp="")
    inp = ""
    return render_template('home.html', main=main(inp), inp=inp)

if __name__ == '__main__':
    app.run()
