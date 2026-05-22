import math

def bikespeed_from_power(
    incline: float,
    power_watt: float = 120.0,
    mass_kg: float = 85.0,
    max_speed_mps: float = 12.5,  # 45 km/h
) -> float:
    """
    Berechnet die Fahrradgeschwindigkeit in m/s bei konstanter Leistung.

    Die Geschwindigkeit wird so gesucht, dass die benötigte Leistung
    ungefähr der verfügbaren Fahrerleistung entspricht.
    Danach wird die Geschwindigkeit auf max_speed_mps begrenzt.

    Basierend auf:
    Martin et al. (1998): Validation of a Mathematical Model
    for Road Cycling Power. Journal of Applied Biomechanics, 14(3), 276-291.
    """

    g = 9.81
    crr = 0.005
    cda = 0.5
    rho = 1.225
    efficiency = 0.97

    available_power = power_watt * efficiency

    theta = math.atan(incline)
    sin_theta = math.sin(theta)
    cos_theta = math.cos(theta)

    def needed_power(speed_mps: float) -> float:
        """
        Gibt zurück, wie viel Leistung nötig wäre,
        um mit speed_mps auf dieser Steigung zu fahren.
        """

        gravity_power = mass_kg * g * sin_theta * speed_mps
        rolling_power = crr * mass_kg * g * cos_theta * speed_mps
        air_power = 0.5 * rho * cda * speed_mps**3

        return gravity_power + rolling_power + air_power

    # Wir suchen eine Geschwindigkeit zwischen fast 0 und der erlaubten Topspeed.
    low = 0.01
    high = max_speed_mps

    # Binäre Suche:
    # Wenn bei der getesteten Geschwindigkeit weniger Leistung nötig ist
    # als verfügbar, kann der Fahrer schneller fahren.
    # Wenn mehr Leistung nötig ist, muss er langsamer fahren.
    for _ in range(40):
        test_speed = (low + high) / 2

        if needed_power(test_speed) <= available_power:
            low = test_speed
        else:
            high = test_speed

    # low ist die gefundene Geschwindigkeit in m/s.
    # Sie kann wegen high=max_speed_mps nie über der Topspeed liegen.
    return low