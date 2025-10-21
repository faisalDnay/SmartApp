
def aantal_kluizen_vrij():
    with open("kluizen_informatie", "r")as f:
        kluizen_bezet = f.readlines()
    aantal_bezeten = len(kluizen_bezet)
    aantal_vrij = 12 - aantal_bezeten
    return aantal_vrij


def nieuwe_kluizen():
    alle_kluizen = list(range(1, 13))

    with open("kluizen_informatie", "r") as f:
        kluizen_bezet = f.readlines()
        for regel in kluizen_bezet:
            regel = regel.strip()
            if regel == "":
                continue
            kluizen_nummer = int(regel.split(";")[0])
            if kluizen_nummer in alle_kluizen:
                alle_kluizen.remove(kluizen_nummer)

    if len(alle_kluizen) == 0:
        return -2

    nieuwe_kluis = alle_kluizen[0]

    while True:
        code = input(f"Maak uw code (maximal 4 tekens en Geen ';'): ")
        if len(code) < 4:
            print("Fout: code te kort, probeer opnieuw.")
        elif ";" in code:
            print("Fout: code mag geen ';' bevaten, probeer opnieuw.")
        else:
            break

    with open(f"kluizen_informatie", "a") as f:
        f.write(f"{nieuwe_kluis};{code}\n")
    return nieuwe_kluis


def kluis_openen():
    kluis_gegeven = input("Wat is uw kluisnummer?: ")
    kluis_code = input("Wat is uw kluiscode?: ")

    with open("kluizen_informatie", "r") as f:
        regels = f.readlines()

    for regel in regels:
        regel = regel.strip()
        if regel == "":
            continue
        nummer, code = regel.split(";")
        if nummer == kluis_gegeven and code == kluis_code:
            return True
    return False

def kluis_teruggeven():
    kluis_gegeven = input("Wat is uw kluisnummer?: ")
    kluis_code = input("Wat is uw kluiscode?: ")

    with open ("kluizen_informatie", "r") as f:
        regels = f.readlines()

    nieuwe_regels = []
    gevonden = False
    for regel in regels:
        regel = regel.strip()
        if regel == "":
            continue
        nummer, code = regel.split(";")

        if nummer == kluis_gegeven and code == kluis_code:
            gevonden = True
        else:
            nieuwe_regels.append(regel)

    with open("kluizen_informatie", "w") as f:
        for regel in nieuwe_regels:
            f.write(regel + "\n")

    return gevonden

while True:
    print("1: Ik wil weten hoeveel kluizen nog vrij zijn")
    print("2: Ik wil een nieuwe kluis")
    print("3: Ik wil even iets uit mijn kluis halen")
    print("4: Ik geef mijn kluis terug")
    print("5: Ik wil stoppen")

    try:
        keuze = int(input("Maak uw keuze: "))
    except ValueError:
        print("Fout: probeer opnieuw")
        continue

    if 5 < keuze or keuze < 1:
        print("Ongeldig keuize probeer opnieuw")
    elif keuze == 1:
        aantal_vr = aantal_kluizen_vrij()
        print(f"Er zijn {aantal_vr} kluizen vrij")
    elif keuze == 2:
        kluisnummer = nieuwe_kluizen()
        if kluisnummer == -2:
            print("Er zijn geen kluizen meer beschikbaar.")
        else:
            print(f"Uw nieuwe kluisnummer is: {kluisnummer}")
    elif keuze == 3:
        if kluis_openen():
            print("U heeft de juiste code ingevoerd, de kluis is geopend!")
        else:
            print("Fout: Kluisnummer en/of code onjuist.")
    elif keuze == 4:
        if kluis_teruggeven():
            print("Uw kluis is succesvol teruggegeven.")
        else:
            print("Fout: Het opgegeven kluisnummer en code komen niet overeen.")
    elif keuze == 5:
        print("programma gestopt!")
        break
