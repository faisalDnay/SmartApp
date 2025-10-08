from SmartAppcontroller import smart_app_controller
from Weerstation import menu
from OpenAPI import weerapi
from time import sleep
while True:

    print("\nWelcome in Smart_App!")
    print("\n=== Smart App menu ===")
    print("1. Smart App controller")
    print("2. Weerstation")
    print("3. Hudige temratuur in Utrecht")
    keuze = input("Maak uw keuze: ")

    if keuze == "1":
        smart_app_controller()
    elif keuze == "2":
        menu()
    elif keuze == "3":
        weerapi()
        sleep(3)
