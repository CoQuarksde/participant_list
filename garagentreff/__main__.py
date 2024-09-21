# __main__.py
# Dies ist der Einstiegspunkt des Programms, wenn es über den Befehl "python -m garagentreff_teilnehmer" aufgerufen wird.
# Es ruft die Hauptfunktion "main" aus der Datei "garagentreff.py" auf.

from garagentreff import main  # Importiere die Hauptfunktion aus garagentreff.py

if __name__ == "__main__":
    # Ruft die Hauptfunktion auf, um das Menü anzuzeigen und die Teilnehmerverwaltung zu starten.
    main()
