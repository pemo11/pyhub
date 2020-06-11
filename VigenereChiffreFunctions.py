# Vigenére Chiffre als Functions
# Umsetzung am 11.06.2020
# Autor: Peter Monadjemi

vigFeld = None
schluessel = "SICHER"

# 26x26 Feld mit den jeweils pro Spalte um einen Buchstaben versetzen Buchstaben von A bis Z

def FeldEinrichten():
    global vigFeld
    # Genial - dank List Comprehension
    vigFeld = [[chr(i+j+65) if i+j < 26 else chr(i+j+39)  for i in range(0,26)]  for j in range(0,26)]

def Verschluesseln(Wort):
    global schluessel
    geheim = ""
    if vigFeld == None:
        FeldEinrichten()
    k = 0
    for c in Wort:
        i = ord(c) - 65
        j = ord(schluessel[k]) - 65
        k = k + 1 if k < len(schluessel) - 1 else 0
        geheim += vigFeld[i][j]
    return geheim

def Entschluesseln(Chiffre):
    global schluessel
    klartext = ""
    if vigFeld == None:
        FeldEinrichten()
    k = 0
    for c in Chiffre:
        # Hole die Nr der Zeile
        j = ord(schluessel[k]) - 65
        # Hole die Nr Spalte, in der der Buchstabe c enthalten ist
        # Die Variable _ ist nur der Form halber dabei, um den Index zu erhalten
        i = [l for l,_ in enumerate(vigFeld[j]) if vigFeld[j][l] == c][0] 
        klartext += chr(i+65)
        k = k + 1 if k < len(schluessel) - 1 else 0
    return klartext

# Das Wort "SEMESTER" soll mit dem Schlüssel SICHER verschüsselt werden
wort = "SEMESTER"
geheim = Verschluesseln(wort)
print(geheim)
# Aus dem Wort KMOLWKWZ soll wieder das Originalwort SEMESTER werden
wort2 = Entschluesseln(geheim)
print(wort2)

