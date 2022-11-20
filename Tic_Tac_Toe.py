spiel_aktiv = True
spieler_aktiv = "x"
spielfeld = [" ",
             "1", "2", "3",
             "4", "5", "6",
             "7", "8", "9"]

# Spelfeld generieren
def spielfeld_output():
    print(spielfeld[1] + " " + spielfeld[2] + " " + spielfeld[3])
    print(spielfeld[4] + " " + spielfeld[5] + " " + spielfeld[6])
    print(spielfeld[7] + " " + spielfeld[8] + " " + spielfeld[9])

# Spieler wechseln
def spieler_wechsel(spieler_aktiv):
    if spieler_aktiv == "x":
        spieler_aktiv = "o"
    else:
        spieler_aktiv = "x"
    return spieler_aktiv


# Spieler eingabe
def spieler_input(spieler_aktiv):
    try:
        spieler = int(input(f"Spieler {spieler_aktiv}: An welche Position? "))
        if spieler >= 1 and spieler <= 9:
            if spielfeld[spieler] == "x" or spielfeld[spieler] == "o":
                print("Spielfeld bereits besetz")
                spieler_input(spieler_aktiv)
            else:
                spielfeld[spieler] = spieler_aktiv
        else:
            print("Zahl muss zwieschen 1 und 9 sein!")
            spieler_input(spieler_aktiv)
    except ValueError:
        print("Bitte nur Zahlen eingaben!")
        spieler_input(spieler_aktiv)

# Pruefung, ob Spiel gewonnen wurde
def gewonnen_check(spiel_aktiv):
    #horizontale linien
    if spielfeld[1] == spielfeld[2] == spielfeld[3]:
        print(f"Spieler {spielfeld[1]} hat gewonnen")
        spiel_aktiv = False
    if spielfeld[4] == spielfeld[5] == spielfeld[6]:
        print(f"Spieler {spielfeld[4]} hat gewonnen")
        spiel_aktiv = False
    if spielfeld[7] == spielfeld[8] == spielfeld[9]:
        print(f"Spieler {spielfeld[7]} hat gewonnen")
        spiel_aktiv = False
    #vertikale linien
    if spielfeld[1] == spielfeld[4] == spielfeld[7]:
        print(f"Spieler {spielfeld[1]} hat gewonnen")
        spiel_aktiv = False
    if spielfeld[2] == spielfeld[5] == spielfeld[8]:
        print(f"Spieler {spielfeld[2]} hat gewonnen")
        spiel_aktiv = False
    if spielfeld[3] == spielfeld[6] == spielfeld[9]:
        print(f"Spieler {spielfeld[3]} hat gewonnen")
        spiel_aktiv = False
    #dioganale linien
    if spielfeld[1] == spielfeld[5] == spielfeld[9]:
        print(f"Spieler {spielfeld[1]} hat gewonnen")
        spiel_aktiv = False
    if spielfeld[3] == spielfeld[5] == spielfeld[7]:
        print(f"Spieler {spielfeld[3]} hat gewonnen")
        spiel_aktiv = False
    spiel_aktiv = unentschieden(spiel_aktiv)
    return spiel_aktiv

# Pruefung, ob Spiel unterschieden
def unentschieden(spiel_aktiv):
    if (spielfeld[1] == "x" or spielfeld[1] == "o") \
        and(spielfeld[2] == "x" or spielfeld[2] == "o") \
        and(spielfeld[3] == "x" or spielfeld[3] == "o") \
        and(spielfeld[4] == "x" or spielfeld[4] == "o") \
        and(spielfeld[5] == "x" or spielfeld[5] == "o") \
        and(spielfeld[6] == "x" or spielfeld[6] == "o") \
        and(spielfeld[7] == "x" or spielfeld[7] == "o") \
        and(spielfeld[8] == "x" or spielfeld[8] == "o") \
        and(spielfeld[9] == "x" or spielfeld[9] == "o"):
        print("UNENTSCHIEDEN")
        spiel_aktiv = False
    return spiel_aktiv

#############Spiel##################
print("Spieler1  ist x, Spieler2 ist o")
print("x beginnt")

spielfeld_output()

while spiel_aktiv:
    spieler_input(spieler_aktiv)
    spieler_aktiv = spieler_wechsel(spieler_aktiv)
    spiel_aktiv = gewonnen_check(spiel_aktiv)
    spielfeld_output()
