from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.work_panel.visible = True

    # Any code you write here will run before the form opens.

  def admin_pw_pressed_enter(self, **event_args):
    if self.admin_pw.text == 'ft27':
      self.admin_pw.visible = False
      self.load_panel.visible = True
    else:
      self.work_panel.visible = True

  def admin_click(self, **event_args):
    """This method is called when the component is clicked."""
    self.admin_pw.visible = True

  def get_str(self, mgl_ln):
    ln_en = mgl_ln
    ln_en_1 = ln_en.find('"') + 1
    lnn = ln_en[ln_en_1:]
    ln_en_2 = lnn.find('"')
    lnn = lnn[:ln_en_2]
    return lnn

  def file_loader_1_change(self, file, **event_args):
    print(f"The file's name is: {file.name}")
    print(f"The number of bytes in the file is: {file.length}")
    print(f"The file's content type is: {file.content_type}")
    #    print(f"The file's contents are: '{file.get_bytes()}'")
    #    print(file)
    b = file.get_bytes()
    bb = b.decode("utf-8")
    mgl = bb.splitlines()
    #    anvil.server.call("upload_csv_pols", bbb, "regs")
    i = 0
    while i < len(mgl):
      ln = mgl[i]
      if ln.find("[") != -1:
        str_na = ln
        str_na_equ = str_na.find('=')
        str_na = str_na[0:str_na_equ].strip()
        self.load_text.text = "Loading "+str_na
        en = self.get_str(mgl[i+1])
        de_sie = self.get_str(mgl[i+2])
        de_du = self.get_str(mgl[i+3])
        fr_vous = self.get_str(mgl[i+4])
        no = self.get_str(mgl[i+5])
        app_tables.strings.add_row(name=str_na, en=en, de_sie=de_sie, de_du=de_du,fr_vous=fr_vous,no=no)
        i = i + 6
        # save into db
      i = i + 1
    alert("All text strings from lu.py have been loaded.")
    self.work_panel.visible = True

  def admin_pw_show(self, **event_args):
    self.admin_pw.focus()

  def ddm_lang_1_change(self, **event_args):
    """This method is called when an item is selected"""
    pass
