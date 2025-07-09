import anvil.server
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
sign_up_title = [
  "New registration",
  "Neu registrieren",
  "Neu registrieren",
  "Nouvelle inscription",
  "Ny registrering",
  "_last_"
]
user_placeholder = [
  "Enter username",
  "Benutzername",
  "Benutzername",
  "Entrez votre nom d'utilisateur",
  "brukernavn",
  "_last_"
]
save_btn = [
  "Save",
  "Speichern",
  "Speichern",
  "Enregistrer",
  "Lagre",
  "_last_"
]
cancel_btn = [
  "Cancel",
  "Abbrechen",
  "Abbrechen",
  "Annuler",
  "Avbryt",
  "_last_"
]
regi_first_tx = [
  "Register, after all?",
  "Doch erst registrieren?",
  "Doch erst registrieren?",
  "Il faut d'abord s'inscrire, après tout ?",
  "Registrere seg, tross alt?",
  "_last_"
]
login_title_tx = [
  "Log-in",
  "Einloggen",
  "Einloggen",
  "Se connecter",
  "Logg inn",
  "_last_"
]
login_u_tx = [
  "Enter your username",
  "Benutzernamen eingeben",
  "Benutzernamen eingeben",
  "Entrez votre nom d'utilisateur",
  "Skriv inn brukernavn",
  "_last_"
]
login_first_btn = [
  "Already registered? Log in",
  "Bereits registriert? Einloggen",
  "Bereits registriert? Einloggen",
  "Déjà inscrit ? Connectez-vous.",
  "Allerede registrert? Logg inn",
  "_last_"
]
err_user_not_exits = [
  "A user with this name does not exist",
  "Ein Benutzer mit diesem Namen existiert nicht.",
  "Ein Benutzer mit diesem Namen existiert nicht.",
  "Il n'existe aucun utilisateur portant ce nom.",
  "Det finnes ingen bruker med dette navnet.",
  "_last_"
]
sorry = [
  "Sorry - to see you go",
  "Es tut uns leid, dass Sie gehen",
  "Es tut uns leid, dass Du gehst",
  "Désolé de vous voir partir",
  "Beklager - å se deg gå",
  "_last_"
]
err_username1 = [
  "The username must be at least 3 chars long",
  "Der Benutzername muss mindestens 3 Zeichen lang sein.",
  "Der Benutzername muss mindestens 3 Zeichen lang sein.",
  "Le nom d'utilisateur doit comporter au moins 3 caractères.",
  "Brukernavnet må være minst 3 tegn langt",
  "_last_"
]
err_username2 = [
  "The username cannot be longer than 15 chars",
  "Der Benutzername darf nicht länger als 15 Zeichen sein.",
  "Der Benutzername darf nicht länger als 15 Zeichen sein.",
  "Le nom d'utilisateur ne peut pas dépasser 15 caractères.",
  "Brukernavnet kan ikke være lengre enn 15 tegn.",
  "_last_"
]
err_username3 = [
  "You must enter a username",
  "Sie müssen einen Benutzernamen eingeben.",
  "Du musst einen Benutzernamen eingeben.",
  "Vous devez saisir un nom d'utilisateur.",
  "Du må oppgi et brukernavn",
  "_last_"
]
err_username_exists = [
  "The username already exists",
  "Der Benutzername existiert bereits.",
  "Der Benutzername existiert bereits.",
  "Le nom d'utilisateur existe déjà.",
  "Brukernavnet eksisterer allerede",
  "_last_"
]
err_username_alpha = [
  "The username cannot be all digits",
  "Der Benutzername darf nicht ausschließlich aus Ziffern bestehen.",
  "Der Benutzername darf nicht ausschließlich aus Ziffern bestehen.",
  "Le nom d'utilisateur ne peut pas être composé uniquement de chiffres.",
  "Brukernavnet kan ikke bestå av bare tall.",
  "_last_"
]
