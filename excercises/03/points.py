def points_easy(points: int, mistakes: int) -> int:
    """Berechnet die erreichten Punkte für eine leichte Aufgabe."""

    # kein Fehler -> volle Punktzahl
    if mistakes == 0:
        return points

    # mehr als 7 Fehler -> keine Punkte
    if mistakes > 7:
        return 0

    # sonst: 2 Punkte Abzug pro Fehler, aber nicht negativ
    return max(points - 2 * mistakes, 0)


def points_hard(points: int, mistakes: int) -> int:
    """Berechnet die erreichten Punkte für eine schwere Aufgabe."""

    # weniger als 3 Fehler -> volle Punktzahl
    if mistakes < 3:
        return points

    # ab dem 3. Fehler: für jeden weiteren Fehler 1 Punkt Abzug
    # aber nicht negativ
    return max(points - (mistakes - 2), 0)


def calculate_points(mistakes_easy: int, mistakes_hard: int) -> int:
    """
    Berechnet die Gesamtpunktzahl einer Abgabe bestehend aus:
    - einer leichten Aufgabe (14 Punkte)
    - einer schweren Aufgabe (16 Punkte)
    """

    points_easy_result = points_easy(14, mistakes_easy)
    points_hard_result = points_hard(16, mistakes_hard)

    return points_easy_result + points_hard_result


# Tests für points_easy
assert points_easy(10, 0) == 10
assert points_easy(10, 1) == 8
assert points_easy(10, 3) == 4
assert points_easy(10, 5) == 0
assert points_easy(10, 6) == 0
assert points_easy(20, 7) == 6
assert points_easy(20, 8) == 0

# Tests für points_hard
assert points_hard(10, 0) == 10
assert points_hard(10, 2) == 10
assert points_hard(10, 3) == 9
assert points_hard(10, 4) == 8
assert points_hard(10, 5) == 7
assert points_hard(10, 10) == 2
assert points_hard(10, 11) == 1
assert points_hard(10, 12) == 0
assert points_hard(10, 13) == 0
assert points_hard(10, 15) == 0

# Tests für calculate_points
assert calculate_points(0, 0) == 30
assert calculate_points(2, 0) == 26
assert calculate_points(8, 0) == 16
assert calculate_points(0, 3) == 29
assert calculate_points(5, 10) == 12
assert calculate_points(8, 18) == 0

print("Alle Tests erfolgreich!")
