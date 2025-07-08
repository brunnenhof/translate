import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
# This is a module.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
#
#    from .. import Module1
#
#    Module1.say_hello()
#

lx = 0
where_name = ''
where = 0
ln_2_idx = {
  "en" : 0,
  "de" : 1,
  "fr" : 3,
  "no" : 4
}
load_tx = [
  "Load file",
  "Datei laden",
  "Datei laden",
  "Charger le fichier",
  "Last inn fil",
]
loading_tx = [
  "Loading ",
  "Einlesen von ",
  "Einlesen von ",
  "Lecture de ",
  "Innlesning av ",
]
loaded_tx = [
  "All text strings from lu.py have been loaded.",
  "Alle Texte aus lu.py wurden geladen..",
  "Alle Texte aus lu.py wurden geladen..",
  "Toutes les chaînes de texte de lu.py ont été chargées.",
  "Alle tekststrenger fra lu.py er lastet inn."
]
file_loader_tooltip  = [
  "First, you need to load all text strings from lu.py into the database.",
  "Zunächst müssen Sie alle Texte aus lu.py in die Datenbank einlesen.",
  "Zunächst müssen Sie alle Texte aus lu.py in die Datenbank einlesen.",
  "Tout d'abord, vous devez charger toutes les chaînes de texte de lu.py dans la base de données.",
  "Først må du laste alle tekststrenger fra lu.py inn i databasen.",
]
ddm_lang_1_placeholder = [
  "English",
  "Deutsch-Sie",
  "Deutsch-Du",
  "Français",
  "Norsk-Bokmål",
]
ddm_lang_1_change_language = [
  "Change source language",
  "Quellsprache ändern",
  "Quellsprache ändern",
  "Changer la langue source",
  "Endre kildespråk",
]