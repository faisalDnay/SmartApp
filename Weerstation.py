# Smart App - Sprint 1: Weerstation


def fahrenheit (temp_celsius):
    return 32 + 1.8 * temp_celsius


def gevoelstempratuur(temp_celsius, windsnelheid, vochtigheid):
    return temp_celsius - (vochtigheid/100) * windsnelheid


dagen = []

def weerrapport(temp_celsius, windsnelheid, vochtigheid):
    gevoel = gevoelstempratuur(temp_celsius, windsnelheid, vochtigheid)

    if gevoel < 0 and windsnelheid > 10:
        return "Het is heel koud en het stormt! Verwarming helemaal aan!"
    elif gevoel < 0 and windsnelheid <= 10:
        return "Het is behoorlijk koud! Verwarming aan op de benedenverdiepeing!"
    elif 0 <= gevoel < 10 and windsnelheid > 12:
        return "Het is best koud en het waait; verwarming aan en roosters dicht!"
    elif 0 <= gevoel < 10 and windsnelheid <= 12:
        return "Het is een beetje koud, elektrische kachel op de benedenverdieping aan!"
    elif 10 <= gevoel < 22:
        return "Heerlijk weer, niet te koud of te warm."
    else:
        return "Warm! Airco aan!"

def menu():

    for dag in range(7):
        temp_celsius = float(input(f"Wat is op dag {dag+1} de tempratuur [C]: "))
        windsnelheid = float(input(f"Wat is de windsnelheid [m/s]: "))
        vochtigheid = int(input(f"Wat is de luchtvochtheid %: "))

        temp_f = fahrenheit(temp_celsius)
        dagen.append(temp_celsius)
        gem_temp = sum(dagen) / len(dagen)
        rapport = weerrapport(temp_celsius, windsnelheid, vochtigheid)

        print(f"Dag {dag+1}: {temp_celsius}°C ({temp_f:.1f}°F)")
        print(f"Gemiddelde temperatuur tot nu toe: {gem_temp:.1f}°C")
        print(rapport)
        print("=" * 40)
        return


