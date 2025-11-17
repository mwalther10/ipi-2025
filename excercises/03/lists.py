def count_occurrences(xs: list[str], x: str) -> int:
    """
    Zählt, wie oft der String `x` in der Liste `xs` vorkommt.

    Gibt die Anzahl der Vorkommnisse als int zurück.
    """
    count = 0
    for element in xs:
        if element == x:
            count += 1
    return count


def min(xs: list[int]) -> int | None:
    """
    Gibt das Minimum einer Liste ganzer Zahlen zurück.
    Falls die Liste leer ist, wird None zurückgegeben.
    """

    # leere Liste -> kein Minimum vorhanden
    if not xs:
        return None

    # erstes Element als Startwert für das Minimum speichern
    minimum = xs[0]

    # alle Elemente der Liste durchgehen und Minimum finden
    for value in xs:
        if value < minimum:
            minimum = value

    return minimum


def max(xs: list[int]) -> int | None:
    """
    Gibt das Maximum einer Liste ganzer Zahlen zurück.
    Ist die Liste leer, wird None zurückgegeben.
    """

    # ist hier nötig, da sonst `-smallest_negated` einen TypeError erzeugt
    if not xs:
        return None

    # Liste mit negierten Werten erstellen
    negated = []
    for value in xs:
        negated += [-value]

    smallest_negated = min(negated)

    return -smallest_negated


assert count_occurrences([], "jemand da?") == 0
assert count_occurrences(["Python", "C++", "Java", "Python"], "Python") == 2
assert count_occurrences(["Python", "C++", "Java", "Java Script"], "JavaScript") == 0

assert min([]) is None
assert min([1, 2, 3]) == 1
assert min([-2, 20, -4, 19]) == -4

assert max([]) is None
assert max([1, 2, 3]) == 3
assert max([-2, 20, -4, 19]) == 20
