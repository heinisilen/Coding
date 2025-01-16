

def Valikko():
    print("Tämä laskin osaa seuraavat toiminnot:")
    print("1) Anna luvut")
    print("2) Summa")
    print("3) Osamäärä")
    print("0) Lopeta")
    Syote = input("Valitse toiminto (0-3): ")
    toiminto = int(Syote)
    return toiminto

def AnnaLuku(kehote):
    Syote = input(kehote)
    Luku = int(Syote)
    return Luku

def Summa(Luku1, Luku2):
    summa = Luku1 + Luku2
    return summa
    
def Osamaara(Luku1, Luku2):
    if (Luku2 > 0):
        osamaara = round(Luku1 / Luku2, 2)
        return osamaara
    else:
        return "Nollalla ei voi jakaa."

def paaohjelma():
    Luku1 = None
    Luku2 = None

    while True:
        valinta = Valikko()
        
        if (valinta == 1):
            Luku1 = AnnaLuku("Anna ensimmäinen luku: ")
            Luku2 = AnnaLuku("Anna toinen luku: ")
            print("Annoit luvut", Luku1, "ja", Luku2)
        elif (valinta == 2):
            summa = Summa(Luku1, Luku2)
            print("Summa", Luku1, "+" , Luku2, "=", summa)
        elif (valinta == 3):
            osamaara = Osamaara(Luku1, Luku2)
            print("Osamäärä", Luku1, "/", Luku2, "=", osamaara)
        elif (valinta == 0):
            print("Lopetetaan")
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.")
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
