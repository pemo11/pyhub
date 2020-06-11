# Vigenére Chiffre
# Umsetzung am 9.06.2020
# Autor: Peter Monadjemi
 
# Schritt 1: 26x26 Feld mit den jeweils pro Spalte um einen Buchstaben versetzen Buchstaben von A bis Z

# Thereotisch ließe sich das Fels auch gleich per List Comprehension passend füllen
vigFeld = [[0 for i in range(0,26)] for j in range(0,26)]

offset = 0

# Ergebnis stimmt, kann aber eventuell vereinfacht werden
for i in range(0,26):
    for j in range(0,26):
        c = j + offset + 65
        c = c - 26 if c > 90 else c
        vigFeld[i][j] = chr(c)
    offset += 1
 
for i in range(0,26):
    print(vigFeld[i])

# Das Wort "SEMESTER" soll mit dem Schlüssel SICHER verschüsselt werden
wort = "SEMESTER"
schluessel = "SICHER"
geheim = ""

k = 0
for c in wort:
    i = ord(c) - 65
    j = ord(schluessel[k]) - 65
    k = k + 1 if k < len(schluessel) - 1 else 0
    geheim += vigFeld[i][j]

# Stimmt - aus SEMESTER wird KMOLWKWZ
print(geheim)

# Wie muss eine Entschlüsselungsfunktion aussehen?