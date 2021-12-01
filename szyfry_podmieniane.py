def szyfr_słownik(szyfr):
    """Tworzy słownik na podstawie szyfru."""
    sł = {}
    i = 0
    j = 1
    # Wykluczam przypadek kiedy szyfr składa się z nieprzystej ilości znaków.
    while j < len(szyfr):
        sł[szyfr[i].lower()] = szyfr[j].lower()
        sł[szyfr[j].lower()] = szyfr[i].lower()
        i += 2
        j += 2

    return sł


def szyfruj(tekst, szyfr):
    """Szyfruje wiadomość za pomocą szyfru podstawieniowego."""
    sł = szyfr_słownik(szyfr)
    wyn = ""
    for litera in tekst:
        x = sł.get(litera.lower())
        if x is None:
            wyn += litera
        else:
            wyn += x if litera.islower() else x.upper()

    return wyn


def weryfikuj(szyfr):
    """Weryfikacja, czy sekwencja podana przez użytkownika jest poprawnym szyfrem."""
    y = []
    for i in szyfr:
        for j in y:
            if j == i.lower():
                return False
        y.append(i.lower())

    return True


def main():
    a = "GADERYPOLUKI"
    b = "POLITYKARENU"
    wybierz = input("Jakim szyfrem podmiennym chcesz zaszyfrować wiadomość? "
                    "\n- GADERYPOLUKI (1), POLITYKARENU (2), czy chcesz podać własną sekwencję (3)? ")
    if wybierz == '1':
        tekst = input("Szyfrowanie za pomocą 'GADERYPOLUKI'. Proszę podaj wiadomość do zaszyfrowania: ")
        print(f"Zaszyfrowana wiadomość => {szyfruj(tekst, a)}")
    elif wybierz == '2':
        tekst = input("Szyfrowanie za pomocą 'POLITYKARENU'. Proszę podaj wiadomość do zaszyfrowania: ")
        print(f"Zaszyfrowana wiadomość => {szyfruj(tekst, b)}")
    elif wybierz == '3':
        szyfr = input("Proszę podać sekwencję za pomocą której chcesz zaszyfrować wiadomość: ")
        print(">>> Trwa weryfikacja sekwencji...")
        if weryfikuj(szyfr):
            print(">>> Sekwencja poprwana")
            tekst = input(f"Szyfrowanie za pomocą '{szyfr}'. Proszę podaj wiadomość do zaszyfrowania: ")
            print(f"Zaszyfrowana wiadomość => {szyfruj(tekst, szyfr)}")
        else:
            print("Niestety podana sekwencja jest niepoprawna.")
    else:
        print("Nieprawidłowy znak.")


main()
