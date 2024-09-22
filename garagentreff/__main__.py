# Module docstring (for the whole file):
"""
This module is the entry point of the garagentreff application.
"""

# __main__.py
# Dies ist der Einstiegspunkt des Programms,
# wenn es über den Befehl "python -m garagentreff_teilnehmer" aufgerufen wird.
# Es ruft die Hauptfunktion "main" aus der Datei "garagentreff.py" auf.

from garagentreff import main  # Importiere die Hauptfunktion aus garagentreff.py

# main function docstring:
if __name__ == "__main__":
    """Ruft die Hauptfunktion auf, um das Menü anzuzeigen und die Teilnehmerverwaltung zu starten."""
    # main function call from garagentreff.py
    main()
