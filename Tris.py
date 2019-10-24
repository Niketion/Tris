# Quando è True termina il gioco
endGame = False
# Lista di oggetti Casella
caselle = []
# Lista di oggetti Giocatore
giocatori = []
# Alterna il giocatore in ogni selezione (0 = primo giocatore, 1 = secondo giocatore)
personaScelta = 0
# Tutte le possibilitò di vincita, mediante la posizione assoluta
posizioni_vincite = [[1,5,9],[3,5,7],[1,3,7],[2,5,8],[3,6,9],[1,2,3],[4,5,6],[7,8,9]]

# Classe Casella
class Casella:
    occupato = False
    giocatore = None

    def __init__(self, posX, posY):
        self.posX = posX
        self.posY = posY
        self.posAbs = cerca_posizione(posX, posY)

# Classe Giocatore
class Giocatore:
    simbolo = ""
    nome = ""
    posPrese = []

    def __init__(self, nome, simbolo):
        self.simbolo = simbolo
        self.nome = nome

# Prendere l'instanza di una classe attraverso la posizione assoluta
def get_casella(posAbs):
    for casella in caselle:
        if (casella.posAbs == posAbs):
            return casella

# Attraverso posX e posY trovo la posizione assoluta (posAbs)
def cerca_posizione(posX, posY):
    if (posX == 0):
        return posY + 1
    elif (posX == 1):
        return posY + 4
    elif (posX == 2):
        return posY + 7

# Inizializza il gioco
for i in range(3):
    for y in range(3):
        caselle.append(Casella(i, y))
for i in range(2):
    nome = input("Giocatore "+str(i)+", scegli il tuo nome: ")
    simbolo = input(" Ora scegli il tuo simbolo: ")
    giocatori.append(Giocatore(nome, simbolo))

print("----------------")
print("| 1  | 2  | 3  |")
print("----------------")
print("| 4  | 5  | 6  |")
print("----------------")
print("| 7  | 8  | 9  |")
print("----------------")

"""Seleziona la casella dove il giocatore vuole inserire il simbolo.

Parameters
---------
giocatore : Giocatore
    Il giocatore che sta giocando il turno
num : int
    Posizione assoluta data in input dal giocatore

Returns
-------
bool 
    True se è riuscito a posizionare il simbolo, altrimenti lo richiede
"""
def selezione(giocatore, num):
    for casella in caselle:
        if (casella.posAbs == num):
            if (not (casella.occupato)):
                casella.occupato = True
                casella.giocatore = giocatore
                giocatore.posPrese.append(casella)
                disegnaTabella()
                return True;
            else:
                nuovaPosizione = int(input("Posto già occupato, scegline un altro: "))
                selezione(giocatore, nuovaPosizione)

# Disegna la tabella con i simboli aggiornati all'ultima azione
def disegnaTabella():
    simboli=[]
    for casella in caselle:
        if (casella.giocatore != None):
            simboli.append(casella.giocatore.simbolo)
        else:
            simboli.append("")

    print("----------------")
    print("|  " + str(simboli[0]) + "  |  " + str(simboli[1]) + "  |  " + str(simboli[2]) + "  |")
    print("----------------")
    print("|  " + str(simboli[3]) + "  |  " + str(simboli[4]) + "  |  " + str(simboli[5]) + "  |")
    print("----------------")
    print("|  " + str(simboli[6]) + "  |  " + str(simboli[7]) + "  |  " + str(simboli[8]) + "  |")
    print("----------------")

def gioco():
    global personaScelta
    global endGame

    posizioneScelta = int(input(giocatori[personaScelta].nome + ", scrivi la posizione: "))
    if (selezione(giocatori[personaScelta], posizioneScelta)):
        if (personaScelta == 0): personaScelta = personaScelta + 1
        else: personaScelta = personaScelta - 1

        # Vincita
        for posizioni in posizioni_vincite:
            winning = 0
            vincitore = None
            for i in range(3):
                condizione=True
                # Controllo se è lo stesso simbolo per fare tris
                if (i!=0):
                    condizione=get_casella(posizioni[i-1]).giocatore == get_casella(posizioni[i]).giocatore
                if (get_casella(posizioni[i]).giocatore != None and condizione):
                    winning = winning+1
                    vincitore = get_casella(posizioni[i]).giocatore
            if (winning == 3):
                print(vincitore.nome," ha vinto!")
                endGame = True
                return

        # Controllo se ci sono ancora posizioni disponibili
        posDisponibili = 9
        for casella in caselle:
            if (casella.giocatore != None):
                posDisponibili = posDisponibili-1
        if (posDisponibili == 0):
            print("Posizioni terminate, nessuno ha vinto! :(")
            endGame = True
            return

        gioco()

while (not (endGame)):
    gioco()