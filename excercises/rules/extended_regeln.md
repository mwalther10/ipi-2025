Zusätzlich zu den bisherigen Abgaberegeln (diese finden Sie auch
[[hier]{style="color: red"}](https://moodle.uni-heidelberg.de/mod/page/view.php?id=1433657)),
gelten ab diesem Übungsblatt folgende Regeln:

1.  **Syntax-Fehler**

    Ab diesem Übungsblatt werden Python-Skripte, die aufgrund eines
    Syntax-Fehlers nicht ausführbar sind, mit 0 Punkten bewertet.
    Syntax-Fehler treten auf, wenn Ihr Programm nicht den Regeln der
    Python-Syntax entspricht. Ein Beispiel für einen Syntax-Fehler ist
    das Vergessen eines Doppelpunkts am Ende einer Funktionsdefinition:

            # Am Ende der Zeile fehlt ein':'
            def add_one(x: int) -> int
                return x + 1   

    Wenn Sie versuchen, dieses Programm auszuführen, erhalten Sie die
    folgende Fehlermeldung:

            File "foo.py", line 2
            def add_one(x: int) -> int
                                      ^
            SyntaxError: expected':'    

    Dabei zeigt die Fehlermeldung sowohl die fehlerhafte Zeile als auch
    eine kurze Fehlerbeschreibung an. In diesem Fall wird in Zeile 2 an
    der angezeigten Stelle ein Doppelpunkt erwartet.

    Syntax-Fehler sind oft leicht zu finden und zu beheben, insbesondere
    wenn Sie VS Code nutzen. Wenn Sie einen Syntax-Fehler nach längerem
    Überprüfen Ihres Codes dennoch nicht lösen können, wenden Sie sich
    bitte rechtzeitig an Ihre Tutorin oder fragen Sie im Forum, ohne
    dabei (Teil)Lösungen zu posten.

2.  **Typannotationen**

    Zusätzlich sollen Sie ab diesem Übungsblatt Typannotationen in Ihren
    Funktionen verwenden. Geben sie dabei den Typen so präzise wie
    möglich an. Gibt eine Funktion zum Beispiel eine Liste von ganzen
    Zahlen zurück, so sollte der Rückgabetyp `list[int]` sein.

    In der Vorlesung am 6.11.2025 haben wir über Typannotationen
    gesprochen und auch gesehen, wie diese bei der Spezifikation von
    benutzerdefinierten Funktionen verwendet werden.
