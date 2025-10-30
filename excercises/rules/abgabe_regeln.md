**Gruppenabgaben:**

- Die Aufgaben sollten in Gruppen von idealerweise drei Studierenden
  bearbeitet und abgegeben werden. Nutzen Sie in Moodle das Forum
  ZettelpartnerInnen-Börse, um weitere Mitglieder für eine Gruppe zu
  finden oder eine Gruppe zu bilden.

- Die Mitglieder einer Gruppe sollen von dem ersten Übungsblatt an für
  die weiteren Übungszettel fix bleiben.

- Ab dem zweiten Übungszettel werden wir Gruppen in Moodle einrichten.
  Für den ersten Übungszettel reicht es, wenn ein Mitglied einer Gruppe
  die Lösungen auf Moodle hochlädt. Reichen Sie Ihre Abgabe
  ausschließlich über die bereitgestellte Upload-Funktion in Moodle ein.

- Damit wir bei jedem Übungsblatt wissen, wer die Gruppenmitglieder
  sind, ist jeder Abgabe eine einfache Text-Datei mit dem Namen
  `mitglieder.txt` beizufügen, in der Nachname, Vorname, Matrikelnummer
  und Nummer der Übungsgruppe eines jeden Gruppenmitglieds aufgeführt
  sind. Diese Datei ist mit Teil der Abgabe!

**Für die Abgabe ihrer Lösungen beachten Sie bitte folgende Regeln:**

1.  Verwenden Sie nur Befehle, Funktionen und Programmiertechniken, die
    in den bisherigen Vorlesungen (bis zum Abgabetermin) und bisherigen
    Übungsblättern behandelt wurden.

2.  Die einzelnen Aufgaben sind mit vollständigen Dateinamen versehen.
    Verwenden Sie genau diese Namen und die dazugehörigen Dateiformate
    für Ihre Abgabe. Um Tippfehler zu vermeiden, können Sie die
    Dateinamen auch einfach kopieren.

3.  Ihre Dateien sollen immer im Plaintext-Format (UTF-8 codiert)
    vorliegen. Python-Code speichern Sie in Dateien mit der Endung
    `.py`. Für Texte können Sie zwischen `.txt` und `.md` (Markdown)
    frei wählen. Markdown-Dateien bieten gegenüber einfachen
    `.txt`-Dateien zusätzliche Formatierungsmöglichkeiten, die Sie in
    Visual Studio Code mit der Tastenkombination STRG + SHIFT + V (unter
    Windows) bzw. COMMAND + SHIFT + V (unter MacOS) anzeigen lassen
    können. **Insbesondere sind also keine PDFs, keine Word-Dokumente
    und auch keine Bildschirmfotos erlaubt!**

4.  Geben Sie Ihre Aufgaben bis zur angegebenen Deadline über die
    Moodle-Seite zur Vorlesung ab. Abgaben per Mail werden generell
    nicht berücksichtigt.

5.  Für Python-Code prüfen wir, ob Ihr Code die Stilrichtlinien von
    flake8[^1] befolgt. Dieser Check muss erfolgreich sein; ansonsten
    gibt es Punkteabzug.

    Eine einfache Möglichkeit, diese Anforderungen zu erfüllen, besteht
    darin, alle Dateien mit Visual Studio Code zu erstellen oder zu
    bearbeiten. Wenn Sie zum Beispiel eine Datei mit der Endung `.txt`
    oder `.md` bearbeiten, behandelt Visual Studio Code diese wie eine
    normale Textdatei. Bei `.py`-Dateien zeigt Visual Studio Code
    flake8-Warnungen als gelbe Markierungen an, die Sie durch einen
    Mouseover erklärt bekommen.

6.  Das Format der Abgabe muss die folgenden Eigenschaften haben:

    - Es handelt sich um eine Archivdatei (.zip, .gz, .tar.gz), in der
      alle Dateien zu den einzelnen Übungsaufgaben sowie die Datei
      `mitglieder.txt` enthalten ist.

    - Das Verzeichnis hat den Namen
      `<NummerZettel>_<Nachname1>_<Nachname2>_<Nachname3>.<FileExtension>`
      mit den jeweiligen Nachnamen ihrer Gruppenmitglieder,
      beispielsweise also `01_Reuter_Gertz_Schmidt.zip`.

[^1]: Details dazu finden Sie hier:
    <https://flake8.pycqa.org/en/latest/>
