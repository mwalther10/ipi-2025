import math


# a)
def degrees_to_radians(deg: float) -> float:
    """Konvertiert Grad in Bogenmaß (Radiant)."""
    deg = deg % 360  # Begrenzung auf [0, 360)
    rad = math.radians(deg)
    return rad % (2 * math.pi)  # Begrenzung auf [0, 2pi)


def radians_to_degrees(rad: float) -> float:
    """Konvertiert Bogenmaß (Radiant) in Grad."""
    rad = rad % (2 * math.pi)  # Begrenzung auf [0, 2pi)
    deg = math.degrees(rad)
    return deg % 360  # Begrenzung auf [0, 360)


def gradians_to_radians(gon: float) -> float:
    """Konvertiert Gon (Neugrad) in Bogenmaß (Radiant)."""
    gon = gon % 400  # Begrenzung auf [0, 400)
    rad = gon * (math.pi / 200)
    return rad % (2 * math.pi)  # Begrenzung auf [0, 2pi)


def radians_to_gradians(rad: float) -> float:
    """Konvertiert Bogenmaß (Radiant) in Gon (Neugrad)."""
    rad = rad % (2 * math.pi)  # Begrenzung auf [0, 2pi)
    gon = rad * (200 / math.pi)
    return gon % 400  # Begrenzung auf [0, 400)


# b)
def degrees_to_gradians(deg: float) -> float:
    """Konvertiert Grad in Gon (Neugrad)."""
    rad = degrees_to_radians(deg)
    return radians_to_gradians(rad)


def gradians_to_degrees(gon: float) -> float:
    """Konvertiert Gon (Neugrad) in Grad."""
    rad = gradians_to_radians(gon)
    return radians_to_degrees(rad)


if __name__ == "__main__":
    assert math.isclose(degrees_to_radians(45), math.pi / 4)
    assert math.isclose(radians_to_degrees(math.pi), 180)
    assert math.isclose(radians_to_degrees(3 * math.pi), 180)
    assert math.isclose(degrees_to_gradians(270.0), 300.0)
    assert math.isclose(gradians_to_degrees(100.0), 90.0)
    assert math.isclose(gradians_to_degrees(500.0), 90.0)
    assert math.isclose(gradians_to_degrees(-300.0), 90.0)
    assert math.isclose(gradians_to_radians(300), 3 * math.pi / 2)
    assert math.isclose(radians_to_gradians(math.pi / 2), 100.0)

    print("Alle Tests bestanden.")
