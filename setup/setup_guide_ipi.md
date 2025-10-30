# 🧑‍💻 Setup Guide für die Vorlesung *Einführung in die Praktische Informatik (IPI)*

> Bei Fragen oder Problemen während des Setups wenden Sie sich bitte an den Übungsleiter oder die Übungsleiterin Ihrer Übungsgruppe.

Dieses Setup-Dokument beschreibt die Installation und Einrichtung einer **Python-Programmierumgebung** mit **Miniforge (Conda)** und **Visual Studio Code (VS Code)**.
Empfohlen wird die Nutzung eines **Ubuntu-Systems** (oder einer anderen gängigen Linux-Distribution) bzw. **macOS**.
Alternativ kann unter **Windows** das **Windows Subsystem for Linux (WSL)** verwendet werden, um eine Linux-Umgebung auszuführen.

> 💡 **Hinweis:** Wir bieten vollständige Unterstützung nur für **Ubuntu (bzw. WSL)** / **macOS** und **VS Code** an.
> Wenn Sie ein anderes System oder eine andere IDE verwenden möchten, können Sie das tun – allerdings bieten wir dann nur eingeschränkten Support.

---

## 📘 Inhaltsübersicht

- [📘 Inhaltsübersicht](#-inhaltsübersicht)
- [🪟 Linux für Windows-NutzerInnen als Subsystem (WSL)](#-linux-für-windows-nutzerinnen-als-subsystem-wsl)
  - [⚙️ PowerShell 7 installieren (erforderlich für WSL)](#️-powershell-7-installieren-erforderlich-für-wsl)
  - [🔧 WSL installieren](#-wsl-installieren)
  - [🧑‍💻 Ubuntu einrichten](#-ubuntu-einrichten)
- [💻 Visual Studio Code installieren](#-visual-studio-code-installieren)
  - [🧩 Extensions installieren](#-extensions-installieren)
- [🐍 Python mit Miniforge (Conda) installieren](#-python-mit-miniforge-conda-installieren)
  - [📦 Miniforge installieren (Linux/macOS/WSL)](#-miniforge-installieren-linuxmacoswsl)
  - [🧰 Python-Environment anlegen und aktivieren](#-python-environment-anlegen-und-aktivieren)
  - [📚 Python-Pakete in der Conda-Umgebung installieren](#-python-pakete-in-der-conda-umgebung-installieren)
  - [🧩 Environment und Kernel in VS Code auswählen](#-environment-und-kernel-in-vs-code-auswählen)
    - [🐍 Python-Interpreter auswählen](#-python-interpreter-auswählen)
    - [📓 Kernel für Jupyter Notebooks auswählen](#-kernel-für-jupyter-notebooks-auswählen)
- [🧹 Deinstallation und Aufräumen](#-deinstallation-und-aufräumen)
  - [🧰 Conda-Umgebungen entfernen](#-conda-umgebungen-entfernen)
  - [📦 Miniforge deinstallieren](#-miniforge-deinstallieren)
  - [💻 Visual Studio Code deinstallieren](#-visual-studio-code-deinstallieren)
  - [🪟 WSL (Windows Subsystem for Linux) deinstallieren](#-wsl-windows-subsystem-for-linux-deinstallieren)
  - [⚙️ PowerShell 7 deinstallieren](#️-powershell-7-deinstallieren)

---

## 🪟 Linux für Windows-NutzerInnen als Subsystem (WSL)

> Dieser Abschnitt gilt **nur für Windows-NutzerInnen**.
> macOS- und Linux-NutzerInnen können direkt mit [Visual Studio Code installieren](#-visual-studio-code-installieren) fortfahren.

### ⚙️ PowerShell 7 installieren (erforderlich für WSL)

1. Öffnen Sie die **Windows PowerShell**
   (Windows-Taste drücken → „Windows PowerShell“ suchen → anklicken).
   > 💡 Diese Version ist standardmäßig vorinstalliert (Version 5.x) und wird nur verwendet, um PowerShell 7 zu installieren.

2. Geben Sie nacheinander folgende Befehle ein:
   ```powershell
   winget search Microsoft.PowerShell

   winget install --id Microsoft.PowerShell --source winget
   ```

3.	Nach der Installation finden Sie die neue Version im Startmenü als „PowerShell“ (dunkles Symbol, ggf. mit der Versionsnummer 7).
   Sie kann alternativ auch über den Befehl `pwsh` gestartet werden.

### 🔧 WSL installieren

1. Öffnen Sie die **PowerShell** 7 (Windows-Taste → „PowerShell“ suchen → Rechtsklick → *Als Administrator ausführen*).
2. Geben Sie folgenden Befehl ein:
   ```powershell
   wsl --install
   ```
3. Starten Sie den Computer anschließend neu.

> ℹ️ Falls Probleme auftreten, folgen Sie bitte der offiziellen Microsoft-Anleitung:
> [https://learn.microsoft.com/de-de/windows/wsl/install](https://learn.microsoft.com/de-de/windows/wsl/install)

### 🧑‍💻 Ubuntu einrichten

1. Nach dem Neustart öffnet sich ein Terminalfenster mit der Ubuntu-Installation. Falls sich Ubuntu nicht automatisch öffnet, müssen Sie es manuell starten (Windows Taste → „Ubuntu“ suchen → anklicken).
2. Sie werden aufgefordert, einen **Benutzernamen** und ein **Passwort** zu erstellen – merken Sie sich beides. (Bitte beachten Sie, dass Sie beim Eingeben des Kennworts auf dem Bildschirm nichts sehen werden. Dies wird als blinde Eingabe bezeichnet und ist völlig normal.)
3. Nach Abschluss können Sie Ubuntu/WSL-Terminal jederzeit über das Startmenü (Suche nach „Ubuntu“) öffnen.

Damit ist Ihr Linux-Subsystem eingerichtet.

---

## 💻 Visual Studio Code installieren

1. Besuchen Sie die offizielle Downloadseite:
   👉 [https://code.visualstudio.com/Download](https://code.visualstudio.com/Download)
2. Laden Sie die passende Version herunter:
   - **Windows-NutzerInnen:** „Windows Installer“ (`.exe`) auswählen (auch wenn Sie WSL nutzen).
   - **macOS-NutzerInnen:** `.zip`-Datei für macOS.
   - **Linux-NutzerInnen:** `.deb`-Datei (für Ubuntu/Debian) oder `.rpm` (für Fedora).
3. Führen Sie die Installation aus. Für weitere Informationen dazu:
   - **Windows-NutzerInnen:** siehe [hier](https://code.visualstudio.com/docs/setup/windows#_install-vs-code-on-windows),
   - **macOS-NutzerInnen:** siehe [hier](https://code.visualstudio.com/docs/setup/mac#_install-vs-code-on-macos),
   - **Linux-NutzerInnen:** siehe [hier](https://code.visualstudio.com/docs/setup/linux#_install-vs-code-on-linux).
4. Starten Sie **VS Code**.
5. **Hinweis für Windows/WSL:** Links unten auf das blau hinterlegte `><`-Zeichen drücken, dann WSL auswählen.
6. **Spracheinstellung:**
   Bitte stellen Sie sicher, dass **VS Code auf Englisch** eingestellt ist.
   Dadurch stimmen alle folgenden Anweisungen mit der Benutzeroberfläche überein und Fehlermeldungen lassen sich online leichter recherchieren.
   - Öffnen Sie die **Command Palette** (`Ctrl + Shift + P` bzw. `⌘ + Shift + P` auf macOS).
   - Geben Sie **„Configure Display Language“** ein (dieser Befehl funktioniert in jeder Sprache).
   - Wählen Sie **English (en)** und starten Sie VS Code neu.
   > 💡 Falls VS Code nach der Installation automatisch eine Erweiterung namens *Language Pack for Visual Studio Code* installiert hat, können Sie diese über die **Extensions-Ansicht** (linke Seitenleiste → Symbol mit vier Quadraten oder `Ctrl + Shift + X` / `⌘ + Shift + X`) wieder deaktivieren oder entfernen.

---

### 🧩 Extensions installieren

1. Öffnen Sie in VS Code die **Extensions-Ansicht** (linke Seitenleiste → Symbol mit vier Quadraten oder `Ctrl + Shift + X`/`⌘ + Shift + X`).
2. Suchen und installieren Sie folgende Erweiterungen:
   - `Python` (Microsoft)
   - `Jupyter` (Microsoft)

---

## 🐍 Python mit Miniforge (Conda) installieren

Wir nutzen [Miniforge](https://github.com/conda-forge/miniforge), eine schlanke, offene Conda-Distribution, um Python-Umgebungen effizient zu verwalten.

### 📦 Miniforge installieren (Linux/macOS/WSL)

1. Öffnen Sie Ihr Terminal (**Linux**, **macOS** oder **WSL**).
2. **Nur Linux und WSL**: Aktualisieren Sie Ihre Systempakete, bevor Sie Miniforge installieren.
   Das stellt sicher, dass alle benötigten Werkzeuge auf dem neuesten Stand sind.
   - **Unter Ubuntu oder WSL:**
     ```bash
     sudo apt update
     sudo apt upgrade -y
     ```
   - Unter anderen Linux-Distributionen verwenden Sie die entsprechenden Befehle Ihres Paketmanagers.
3. Laden Sie das passende Installationsskript. (*Hinweis*: In den folgenden Befehlen sind `$(uname)` und `$(uname -m)` Variablen, die von der Shell bzw. vom Terminal automatisch eingefügt werden. Sie müssen im Folgenden nichts an den Befehlen anpassen.)
   Unter **Linux** und **WSL**:
   ```bash
   wget "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
   ```
   Unter **macOS**:
   ```bash
   curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
   ```
4. Führen Sie das Skript aus:
   ```bash
   bash Miniforge3-$(uname)-$(uname -m).sh
   ```
5. Folgen Sie den Anweisungen im Installer (Lizenz bestätigen, Standardpfad übernehmen, usw.). Der Ablauf der Installation kann je nach Version des Installationsskript leicht variieren, sollte aber in etwa wie folgt aussehen:
   1. Mit **ENTER** den Installationsvorgang starten.  
   2. Mit **`q`** die Anzeige der Lizenzbedingungen beenden.  
   3. Mit **`yes`** die Lizenzbedingungen akzeptieren.  
   4. Mit **ENTER** den vorgeschlagenen Standardinstallationsort bestätigen.  
   5. Mit **`yes`** bestätigen, dass das Shell-Profil aktualisiert wird, sodass der `conda`-Befehl automatisch verfügbar ist.  
   6. Warten Sie, bis die Installation abgeschlossen ist — am Ende sollte eine entsprechende Erfolgsmeldung erscheinen.
6. Nach der Installation Terminal schließen und neu öffnen, erst dann kann der `conda`-Befehl genutzt werden.
7. Prüfen Sie, ob `conda` aktiv ist:
   ```bash
   conda --version
   ```
   Falls nicht, führen Sie Folgendes aus:
   ```bash
   conda init bash
   exec bash
   ```
8. Deaktivieren Sie die automatische Aktivierung des Basis-Environments.
   Standardmäßig startet Conda jedes neue Terminal im sogenannten `base`-Environment.
   Für eine saubere Arbeitsumgebung (und um Verwechslungen mit dem Kurs-Environment zu vermeiden) empfiehlt es sich, diese automatische Aktivierung auszuschalten. Dazu können Sie einmalig den folgenden Befehl ausführen:
   ```bash
   conda config --set auto_activate_base false
   ```
   Diese Einstellung betrifft nur neue Terminals und wird erst nach einem Neustart des Terminals wirksam.

---

### 🧰 Python-Environment anlegen und aktivieren

Mit Conda können Sie getrennte Umgebungen für verschiedene Projekte anlegen.
Für diese Anleitung nennen wir das Environment **`IPI`**, der Name ist aber **frei wählbar**.

1. Neues Environment mit Python 3.13 anlegen (mit `y` bestätigen):
   ```bash
   conda create -n IPI python=3.13
   ```
2. Environment aktivieren:
   ```bash
   conda activate IPI
   ```
3. Überprüfen, ob alles funktioniert:
   ```bash
   python --version
   which python
   ```
   Wenn alles korrekt eingerichtet ist, sollte die Ausgabe in etwa wie folgt aussehen:
   - Bei `python --version` erscheint eine Zeile wie:
     ```
     Python 3.13.x
     ```
   - Bei `which python` sollte ein Pfad angezeigt werden, der sich innerhalb des Miniforge-Installationsverzeichnisses befindet und den Namen Ihres Conda-Environments enthält, z. B.:
     ```
     /home/<username>/miniforge3/envs/IPI/bin/python
     ```
4. Solange dieses Terminal geöffnet ist, bleibt das Environment aktiv (erkennbar am Präfix `IPI` in der Eingabezeile).
   Sie können es jederzeit wieder deaktivieren mit:
   ```bash
   conda deactivate
   ```
   Wenn Sie das Terminal schließen, wird das Environment ebenfalls automatisch deaktiviert.
   Beim nächsten Öffnen müssen Sie das Environment bei Bedarf erneut mit `conda activate IPI` aktivieren.

> 💡 Python entwickelt sich seit vielen Jahren kontinuierlich weiter. Zwischen den Versionen der Reihe **Python 3.x** gibt es nur kleinere Änderungen und Verbesserungen, die Sprache und ihre Grundprinzipien bleiben gleich. Für diese Vorlesung verwenden wir **Python 3.13**, damit alle dieselbe aktuelle Version mit identischen Funktionen nutzen.

---

### 📚 Python-Pakete in der Conda-Umgebung installieren

Innerhalb einer Conda-Umgebung kann auch der Python-eigene Paketmanager `pip` verwendet werden. Das funktioniert, weil jede Conda-Umgebung ihr eigenes Python und damit auch ein eigenes `pip` enthält. Pakete, die Sie über `pip` installieren, werden also nur in dieser Umgebung installiert – nicht systemweit.

Um beispielsweise Jupyter-Notebooks in **VS Code** nutzen zu können, installieren Sie die benötigten Pakete mit dem folgenden Befehl:

```bash
pip install jupyter ipykernel
```

---

### 🧩 Environment und Kernel in VS Code auswählen

Um sicherzustellen, dass VS Code Ihr Conda-Environment für Python-Dateien und Jupyter Notebooks verwendet, müssen Sie einmalig den Interpreter bzw. Kernel auswählen.

#### 🐍 Python-Interpreter auswählen

1. Öffnen Sie **VS Code**.
2. Öffnen Sie die **Command Palette**
   - **Windows / Linux:** `Ctrl + Shift + P`
   - **macOS:** `⌘ + Shift + P`
3. Geben Sie „Python: Select Interpreter“ ein und drücken Sie **Enter**.
4. Wählen Sie das Environment `IPI` (oder den von Ihnen gewählten Namen) aus.
   VS Code verwendet nun automatisch dieses Conda-Environment für alle Python-Dateien.

#### 📓 Kernel für Jupyter Notebooks auswählen

1. Öffnen Sie ein Jupyter Notebook (`.ipynb`) in VS Code.
2. Klicken Sie oben rechts auf **„Select Kernel“**.
3. Wählen Sie **„Python Environments...“** und dann das Conda-Environment `IPI` (oder den von Ihnen gewählten Namen).
   Danach werden alle Notebook-Zellen in dieser Umgebung ausgeführt.

> 💡 Der ausgewählte Kernel bzw. Interpreter bestimmt, in welcher Python-Umgebung Ihr Code ausgeführt wird.
> Wenn Sie später ein anderes Environment verwenden möchten, können Sie den Interpreter oder Kernel jederzeit erneut über den selben Weg ändern.

---

## 🧹 Deinstallation und Aufräumen

Wenn Sie Ihre Entwicklungsumgebung zurücksetzen oder vollständig entfernen möchten, können Sie die folgenden Schritte ausführen.

---

### 🧰 Conda-Umgebungen entfernen

- **Ein bestimmtes Environment (hier `IPI`) löschen:**
  ```bash
  conda remove -n IPI --all
  ```

- **Alle vorhandenen Environments anzeigen:**
  ```bash
  conda env list
  ```

> ⚠️ Sie können alle Environments löschen, **außer das `base`-Environment**.
> Das `base`-Environment gehört zur Conda-Installation selbst und darf **nicht entfernt** werden.

---

### 📦 Miniforge deinstallieren

Befolgen Sie die offiziellen Deinstallationsanweisungen von Miniforge:
🔗 [Miniforge deinstallieren](https://github.com/conda-forge/miniforge?tab=readme-ov-file#uninstall)

---

### 💻 Visual Studio Code deinstallieren

Befolgen Sie die offiziellen Deinstallationsanweisungen von VS Code:
🔗 [VS Code deinstallieren](https://code.visualstudio.com/docs/setup/uninstall)

---

### 🪟 WSL (Windows Subsystem for Linux) deinstallieren

Wenn Sie WSL nicht mehr benötigen, können Sie es folgendermaßen entfernen:

1. **Alle Linux-Distributionen auflisten:**
   ```powershell
   wsl --list
   ```
2. **Eine bestimmte Distribution (z. B. Ubuntu) deinstallieren:**
   ```powershell
   wsl --unregister Ubuntu
   ```
3. **WSL komplett entfernen (optional):**
   - Öffnen Sie „Apps & Features“ → suchen Sie nach **Windows Subsystem for Linux** → deinstallieren.
   - Alternativ über PowerShell:
     ```powershell
     dism.exe /online /disable-feature /featurename:Microsoft-Windows-Subsystem-Linux
     ```

> ⚠️ Durch das Unregistern einer Distribution werden alle darin gespeicherten Daten gelöscht.

---

### ⚙️ PowerShell 7 deinstallieren

Wenn Sie PowerShell 7 nicht mehr benötigen, können Sie sie über die Windows-Einstellungen oder per `winget` entfernen.

> 💡 Führen Sie den folgenden Befehl in der **Windows PowerShell (Version 5)** aus,
> da PowerShell 7 sich nicht selbst deinstallieren kann.

```powershell
winget uninstall --id Microsoft.PowerShell --source winget
```

Anschließend bleibt die vorinstallierte **Windows PowerShell 5** weiterhin auf Ihrem System verfügbar.
