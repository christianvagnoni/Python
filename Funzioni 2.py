import re
def conta_parole(testo):

    testo = testo.lower()

    testo_pulito = re.sub(r'[^\w\s]', '', testo)
    
    parole = testo_pulito.split()

    conteggio_parole = {}

    for parola in parole:
        if parola in conteggio_parole:
            conteggio_parole[parole] += 1
        else:
            conteggio_parole[parola] = 1
    
    return conteggio_parole

testo = "Ciao, ciao! Come stai? Stai bene?"
risultato = conta_parole(testo)
print(risultato)


