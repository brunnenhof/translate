import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import datetime

@anvil.server.callable
def nuts_pwd(u):
  ## with hash https://kinsta.com/blog/python-hashing/
  jetzt = datetime.datetime.now()
  app_tables.nutzer.add_row(usr=u, started=jetzt, wo=0)
  return 27

@anvil.server.callable
def loggin(u):
  row = app_tables.nutzer.get(email=u)
  jetzt = datetime.datetime.now()
  row["last_used"] = jetzt
