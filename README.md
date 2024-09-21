# Garagentreff Teilnehmerverwaltung

Dies ist ein Python-Projekt zur Verwaltung von Teilnehmern eines Garagentreffs.
Das Programm ermöglicht es, Teilnehmer hinzuzufügen, alle Teilnehmer anzuzeigen oder einen bestimmten Teilnehmer anhand der E-Mail-Adresse zu suchen.
Die Teilnehmerdaten werden in einer JSON-Datei gespeichert. 

## Projektstruktur

Die Verzeichnisstruktur des Projekts sieht folgendermaßen aus:



```
garagentreff_teilnehmer/
│
├── garagentreff/
│	├── init.py # Markiert das Verzeichnis als Python-Paket
│	├── main.py # Haupt-Einstiegspunkt des Programms
│	├── garagentreff.py # Logik für die Teilnehmerverwaltung
│	└── teilnehmer.json # JSON-Datei mit den Teilnehmerdaten (wird automatisch erstellt)
│
├── config.yml # YAML-Datei für Konfigurationseinstellungen (Pfade, Logging)
├── setup.py # Setup-Datei zur Installation des Python-Pakets
├── requirements.txt # Abhängigkeiten des Projekts
└── README.md # Projektbeschreibung und Installationsanleitung
```


## Voraussetzungen

Stelle sicher, dass du die folgende Software installiert hast:

- **Python 3.8 oder höher**: Das Programm benötigt mindestens Python 3.8.
- **PyYAML**: Eine Bibliothek zum Verarbeiten von YAML-Dateien. Sie wird in der `requirements.txt` aufgeführt und bei der Installation automatisch installiert.

## Installation

### 1. Herunterladen oder Klonen des Projekts

Du kannst das Projekt über Git klonen oder die Dateien manuell herunterladen:

```bash
git clone <repository-url>
cd garagentreff_teilnehmer
```

### 2. Installieren der Abhängigkeiten

Um die notwendigen Abhängigkeiten zu installieren, benutze den folgenden Befehl:

```bash
pip install -r requirements.txt
```

Dieser Befehl installiert die Bibliotheken, die in der requirements.txt-Datei angegeben sind, inklusive PyYAML.


### 3. Installieren des Projekts als Paket

Installiere das Projekt lokal auf deinem System, um es über den Befehl garagentreff oder python -m garagentreff_teilnehmer auszuführen:

```bash
pip install .
```

```bash
(env_garagentreff) PS C:\Users\eteda\source\repos\garagentreff_teilnehmer> python -m pip install .
Processing c:\users\eteda\source\repos\garagentreff_teilnehmer
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Requirement already satisfied: pyyaml==6.0 in c:\users\eteda\source\repos\garagentreff_teilnehmer\env_garagentreff\lib\site-packages (from garagentreff_teilnehmer==0.1) (6.0)
Building wheels for collected packages: garagentreff_teilnehmer
  Building wheel for garagentreff_teilnehmer (pyproject.toml) ... done
  Created wheel for garagentreff_teilnehmer: filename=garagentreff_teilnehmer-0.1-py3-none-any.whl size=3331 sha256=2b109c4924fe086c117a5dc04734fea7d0ecfdffaec56c381e12a69cfd78ccde
  Stored in directory: C:\Users\eteda\AppData\Local\Temp\pip-ephem-wheel-cache-cs1p2mvw\wheels\9b\c5\33\c53485abd6f984c62e8966317ca2c64885b7eee0b0967ebb79
Successfully built garagentreff_teilnehmer
Installing collected packages: garagentreff_teilnehmer
**Successfully installed garagentreff_teilnehmer-0.1**
```


### 4. Ausführen des Programms

Das Programm kann jetzt von überall auf deinem System ausgeführt werden:

```bash
garagentreff
```

Alternativ kannst du das Programm auch über den folgenden Befehl ausführen:

```bash
python -m garagentreff_teilnehmer
```



## Verwendung

Sobald das Programm gestartet wird, hast du folgende Optionen im Hauptmenü:

1. **Neuen Teilnehmer hinzufügen**: Das Programm fragt nach Vorname, Nachname, E-Mail-Adresse und Telefonnummer des Teilnehmers. Die Daten werden in einer JSON-Datei gespeichert. Wenn die E-Mail-Adresse bereits vorhanden ist, wird der Benutzer darüber informiert.
   
2. **Alle Teilnehmer anzeigen**: Zeigt eine Liste aller Teilnehmer an, die in der JSON-Datei gespeichert sind.

3. **Spezifischen Teilnehmer anzeigen**: Du kannst nach einem Teilnehmer suchen, indem du seine E-Mail-Adresse eingibst. Wenn der Teilnehmer gefunden wird, werden seine Daten angezeigt.

4. **Beenden**: Beendet das Programm.

### Beispiel für die Programm-Nutzung:

#### 1. Teilnehmer hinzufügen:

```bash
Gib deinen Vornamen ein: Max
Gib deinen Nachnamen ein: Mustermann
Gib deine E-Mail-Adresse ein: max.mustermann@example.com
Gib deine Telefonnummer ein: 0123456789

Max Mustermann wurde erfolgreich hinzugefügt!
```

#### 2. Alle Teilnehmer anzeigen:

```bash
Max Mustermann, E-Mail: max.mustermann@example.com, Telefon: 0123456789
```

#### 3. Spezifischen Teilnehmer anzeigen:

```bash
Gib die E-Mail-Adresse des Teilnehmers ein: max.mustermann@example.com
Gefundener Teilnehmer: Max Mustermann, Telefon: 0123456789
```



## Konfiguration

Die Konfigurationsdatei **`config.yml`** enthält Informationen zu den Pfaden und den Logging-Einstellungen des Programms.
Wenn du den Speicherort der JSON-Datei oder der Log-Datei ändern möchtest, kannst du dies hier anpassen.

### Beispiel für eine `config.yml`:

```yaml
paths:
  # Pfad zur JSON-Datei, in der die Teilnehmerdaten gespeichert werden
  data_file: "garagentreff/teilnehmer.json"

logging:
  # Log-Level (INFO, DEBUG, etc.)
  level: "INFO"
  # Pfad zur Log-Datei
  file: "garagentreff.log"
```

### Erklärung der Konfiguration:
1. **Pfad-Anpassungen**: Du kannst den Pfad zur JSON-Datei, die die Teilnehmerdaten speichert, in der YAML-Datei konfigurieren.
2. **Logging**: Du kannst das Log-Level (z.B. INFO oder DEBUG) und den Speicherort der Log-Datei in der YAML-Datei festlegen.
3. **YAML-Konfiguration**: Beim Start lädt die Anwendung die config.yml, um die Einstellungen für Pfade und Logging zu verwenden.

## YAML-Konfiguration** in der Anwendung
Das Programm lädt die Konfigurationsdaten aus der config.yml, um den Speicherort der Teilnehmerdaten und die Logging-Einstellungen festzulegen.

Beispielsweise wird die Datei garagentreff/teilnehmer.json verwendet, um die Teilnehmerdaten zu speichern, und die Datei garagentreff.log wird zum Protokollieren von Ereignissen verwendet.


## Logging
Die Logging-Einstellungen werden ebenfalls in der config.yml definiert. Du kannst das Log-Level (z.B. INFO, DEBUG) und den Speicherort der Log-Datei anpassen.

### Beispiel für Logging:

```yaml
logging:
  level: "INFO"
  file: "garagentreff.log"
```

### Weiterentwicklung und Anpassungen
Das Projekt ist modular aufgebaut, sodass du leicht neue Funktionen hinzufügen oder bestehende Funktionen anpassen kannst.
Du kannst z.B. weitere Felder für die Teilnehmerdaten hinzufügen, wie z.B. **Adresse**, **Geburtsdatum** oder **Bemerkungen**.

#### Erweiterungsideen:
1. **Erweiterung der Teilnehmerdaten**: Füge Felder wie **Adresse** oder **Geburtsdatum** hinzu.
2. **Erstellen von Berichten**: Füge eine Funktion hinzu, um eine Liste aller Teilnehmer in einem bestimmten Format zu exportieren (z. B. **CSV**).
3. **Grafische Benutzeroberfläche (GUI)**: Integriere eine GUI mit `Tkinter` oder `PyQt` für eine einfachere Bedienung.


## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Siehe [LICENSE](LICENSE) für weitere Informationen.

### Was die **README.md**-Datei abdeckt:

1. **Projektstruktur**: Eine detaillierte Übersicht über die Struktur deines Projekts.
2. **Voraussetzungen und Installation**: Anweisungen zur Installation von Python-Abhängigkeiten und zum Installieren des Projekts als ausführbares Paket.
3. **Verwendung**: Anleitung zur Nutzung des Programms, einschließlich Beispielen für die Eingabe und Anzeige von Teilnehmerdaten.
4. **Konfiguration**: Beschreibung der Konfigurationsdatei **`config.yml`** und wie sie für Pfade und Logging verwendet wird.
5. **Logging**: Hinweise zur Konfiguration des Loggings über die YAML-Datei.
6. **Erweiterungsmöglichkeiten**: Ideen zur Weiterentwicklung und Anpassung des Projekts.
7. **Lizenz**: Lizenzinformationen, falls relevant.

Diese **`README.md`** Datei ist im Projektverzeichnis abgelegt, um vollständige Informationen für Benutzer und Entwickler zu bieten.

