###########  Simulare AFN-lambda
##in fisierul 'in.txt' se gasesc datele de intrare
##fisierul este de forma:
##stare_initiala Stari_finale
##cuvant cuvant cuvant......
##litera starea_din_care_pleaca starea_in_care_ajunge
##...
##litera starea_din_care_pleaca starea_in_care_ajunge

def parcurgere(lista, sir):
    ok = True
    point = 0 #pointeaza litera pana la acare s-a parcurs sirul
    f = open("out.txt", "a")
    f.write('Cuvantul: ' + str(sir) + '\n')

    while (len(lista)!= [] and point<len(sir)):
        f.write(str(lista) + ' ' + str(sir[point:]) + "\n") #scrie in fisier
        print(str(lista) + ' ' + str(sir[point:]))  #scrie in consola
        lista = cautare(sir[point], lista, m)
        if(lista == []):
            ok = False
            break
        point = point+1

    if(ok): #verifica daca starea in care s-a ajuns dupa parcurgerea cuvantului este finala
        f.write(str(lista) + ' ' + "''\n") #scrie in fisier
        print(str(lista) + ' ' + "''")  #scrie in consola
        ok = verificare(lista, final)
    if(ok):
        f.write(str(lista) + ' ' + "''\n")
        print(str(lista) + ' ' + "''")
        f.write('Cuvantul este acceptat!\n')
        print('Cuvantul este acceptat!')
    else:
        f.write('Nu se poate!\n')
        print('Nu se poate!')
    f.write('\n')
    f.close()

def cautare(litera, starea, text):  #cauta starile a caror tranzitie accepta o litera anume
    lista = []
    for i in range(0, len(text.splitlines())):
        for j in range(0, len(starea)):
            if(text.splitlines()[i][0] == litera and text.splitlines()[i][2] == starea[j]):
                lista.append(text.splitlines()[i][4])
    return lista

def verificare(lista, final):   #verifica daca cel putin una din starile in care a ajuns este stare finala
    ok = False
    for i in range(0, len(final)):
        for j in range(0, len(lista)):
            if (final[i] == lista[j]):
                #print(str(final[i]) + ' == ' + str(lista[j] ))     #debug
                ok = True
    return ok

def lmbd(text):
    #modifica imputul (lambda-drumuri.....)
    for i in range(2, len(text.splitlines())):
        if(text.splitlines()[i][0] == 'l'):
            for j in range(2, len(text.splitlines())):
                if(text.splitlines()[j][2] == text.splitlines()[i][4] and text.splitlines()[i][2] != text.splitlines()[j][4]): ###########
                    ok = False
                    for q in range(2, len(text.splitlines())): #verifica daca starea pe care vrem sa o introducem exista deja in lista
                        if(str(text.splitlines()[j][0] + ' ' + text.splitlines()[i][2] + ' ' +  text.splitlines()[j][4]) == text.splitlines()[q]):
                            ok = True
                            break
                    if (ok == False):
                        text += str('\n' + text.splitlines()[j][0] + ' ' + text.splitlines()[i][2] + ' ' +  text.splitlines()[j][4])
    return text

def lmbdfinal(final, text):
    #adauga stari finale
    for i in range(0, len(text.splitlines())):
        for j in range(0, len(final)):
            if(text.splitlines()[i][0] == 'l' and text.splitlines()[i][4] == final[j]):
                final.append(text.splitlines()[i][2])
            
    return final

f = open("in.txt", "r")
m = f.read()

start = m[0]    #starea initiala
final = []
final = m.splitlines()[0][2:].split()   #vector cu starile finale
f.close()
sir = m.splitlines()[1].split()
lista = [start]

#print(m)            #debug
while (m != lmbd(m)):
    m = lmbd(m)
#print(final)
#print()
final = lmbdfinal(final, m) #adaugam starile finale generate dupa ce am adaugat drumurile de la lambda
#print(final)
#print() 
#print(m)        #debug
#print()

f = open("out.txt", "w")    #solutie simpla ptr a sterge un posibil vechi fisier "out.txt" si a creea unul nou in care se va face append
f.close()
for i in range(0, len(sir)):
    print()
    print(sir[i])
    parcurgere(lista, sir[i])