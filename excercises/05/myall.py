def all(lst: list[bool]) -> bool:
    """Gibt True zurück, wenn alle Elemente in der Liste True sind, andernfalls False.

    Args:
        lst (list[bool]): Eine Liste von booleschen Werten.
    """
    for item in lst:
        # if not item:
        # if not item is True:
        # if item is False:
        if item is not True:
            return False
    return True


assert all([]) is True
assert all([True, True, True]) is True
assert all([True, False, True, False]) is False


def all2(lst: list[bool]) -> bool:
    return False not in lst


assert all2([]) is True
assert all2([True, True, True]) is True
assert all2([True, False, True, False]) is False

"""
Punktevergabe:
- 2 Punkte für korrekte Implementierung und Typannotationen
- da davon ausgegangen werden kann, dass nur boolsche Werte in der Liste sind,
sind verschiedene Varianten zur Prüfung auf False ohne problematische Edge Cases möglich
- -1 Punkt für fehlende Typannotationen
"""
