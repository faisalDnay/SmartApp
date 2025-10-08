# Sprint_2 = Smart_App_controller

def aantal_dagen(inputfile):
    try:
        with open(inputfile, "r") as f:
            next(f)  # sla de eerste regel over (kolomnamen)
            regels = f.readlines()
        return len(regels)
    except FileNotFoundError:
        print(f"Fout: Het bestand '{inputfile}' is niet gevonden.")
        return 0


def auto_bereken(inputfile, outputfile):

    with open(inputfile, "r") as f:
        next(f)
        regels = f.readlines()

    resultaten = []
    for regel in regels:
        onderdelen = regel.strip().split(";")
        datum = onderdelen[0]
        numpersonen = int(onderdelen[1])
        tempbinnen = float(onderdelen[2])
        tempbuiten = float(onderdelen[3])
        neerslag = float(onderdelen[4])

        verschil = tempbinnen - tempbuiten
        if verschil >= 20:
            cv = 100
        elif 10 <= verschil < 20:
            cv = 50
        else:
            cv = 0

        ventilatie = min(numpersonen + 1, 4)
        bewatering = "True" if neerslag < 3 else "False"
        resultaten.append([datum, str(cv), str(ventilatie), bewatering])

    with open(outputfile, "w") as b:
        for line in resultaten:
            b.write(";".join(line) + "\n")


def overwrite_settings(outputfile):
    with open(outputfile, "r") as f:
        regels = [r.strip().split(";") for r in f if r.strip()]

    datum = input("Wat is de datum?: ")

    gevonden = None
    for regel in regels:
        if regel[0] == datum:
            gevonden = regel
            break
    if not gevonden:
        print(f"Datum '{datum}' niet gevonden.")
        return

    sesteem = input("Welke systeem wil je (cv, ventilatie, bewatering)?: ")
    if sesteem not in ("cv", "ventilatie", "bewatering"):
        print(f"De {sesteem} is ongeldig!")
        return

    nieuwe_waarde = input("Geef de nieuwe warden?: ")

    if sesteem == "cv":
        if not (0 <= int(nieuwe_waarde) <= 100):
            print("Ongeldige waarde voor CV!")
            return
        gevonden[1] = nieuwe_waarde

    elif sesteem == "ventilatie":
        if not (0 <= int(nieuwe_waarde) <= 4):
            print("Ongeldige waarde voor ventilatie!")
            return
        gevonden[2] = nieuwe_waarde

    elif sesteem == "bewatering":
        if nieuwe_waarde not in ("0", "1"):
            print("Ongeldige waarde voor bewatering!")
            return
        gevonden [3] = "True" if nieuwe_waarde == "1" else "False"

    with open(outputfile, "w") as f:
        for regel in regels:
            f.write(";".join(regel)+ "\n")

    print("Waarde succesvol aangepast.")


def smart_app_controller() -> None:
    while True:
        print("\n==== Smart App Controller ====")
        print("1. Aantal dagen in het bestand")
        print("2. Automatisch bereken en naar bestand schrijven")
        print("3. Instellingen handmatig overschrijven")
        print("4. stoppen")

        keuze = input("Maak uw keuze (1-4): ")

        if keuze == "1":
            aantal = aantal_dagen("input.txt")
            print(f"Aantal dagen in het bestand: {aantal}")
        elif keuze == "2":
            auto_bereken("input.txt", "output.txt")
            print(f"Automatisch bereken en naar bestand output.txt")
        elif keuze == "3":
            overwrite_settings("output.txt")
        elif keuze == "4":
            print("Programma afgesluiten.")
            break
        else:
            print("Ongeldige keuze, probeer opnieuw.")

if __name__ == "__main__":
    smart_app_controller()