from ._anvil_designer import homeTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import mg
from ..log_reg import log_reg
from anvil.js.window import navigator
import datetime
from datetime import timezone

class home(homeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.work_panel.visible = True

    # Any code you write here will run before the form opens.

    t1 = ("English", 0)
    t2 = ("Deutsch - Sie", 1)
    t3 = ("Deutsch - Du", 2)
    t4 = ("Français", 3)
    t5 = ("Norsk-Bokmål", 4)
#    self.ddm_lang_1.placeholder = "English"
    self.ddm_lang_1.items = [t1, t2, t3, t4, t5]
    self.ddm_2.items = [t1, t2, t3, t4, t5]
    
    ll = navigator["language"]
    my_loc, my_loc2, lx = self.get_lang(ll)
    lx = 3
    mg.lx = lx
    self.file_loader_1.tooltip = mg.file_loader_tooltip[lx]
    self.file_loader_1.text = mg.load_tx[lx]
    self.load_panel.visible = True
    self.work_panel.visible = False
    new_user = {}
    save_clicked = alert(
      content=log_reg(item=new_user),
      large=True,
      buttons=[],
    )
    if save_clicked == 42 or save_clicked == 342:
      ### left the app
      self.bye_card.visible = True
      self.bye_tx.text = mg.bye_tx[lx]
      self.file_loader_1.visible = False
      return
    elif save_clicked == "admin":
      self.adm_card.visible = True
      self.navbar_links.visible = False
      self.lang_card.visible = False
      return
    else:
      usr = save_clicked["u"]
      mg.usr = usr
      row = app_tables.nutzer.get(usr=usr)
      row["lx"] = lx
      where = row['wo']
      if save_clicked["ur"] == 'up':
        now = datetime.datetime.now()
        row['last_used'] = now
      self.bye_card.visible = False
      len_str = len(app_tables.strings.search())
      if len_str == 0:
        self.load_panel.visible = True
      else:
        self.load_panel.visible = True
        self.load_done(lx, 11)

  def get_lang(self, lang):
    p1 = lang.find("-")
    if p1 > 0:
      lls = lang.split("-")
      l1 = lls[0]
      l2 = lls[1]
    else:
      l1 = "en"
      l2 = "US"
    if l1 in ["en", "de", "fr", "no"]:
      lox = mg.ln_2_idx[l1]
    else:
      lox = 0
    return l1, l2, lox

  def lang_dd_menu_change(self, **event_args):
    print(self.lang_dd_menu.selected_value)
    """This method is called when an item is selected"""
    print(self.lang_dd_menu.selected_value)
    my_lox = int(self.lang_dd_menu.selected_value)
    mg.lx = my_lox
    self.ddm_lang_1.label = "Select your source language"

  def get_str(self, mgl_ln):
    ln_en = mgl_ln
    ln_en_1 = ln_en.find('"') + 1
    lnn = ln_en[ln_en_1:]
    ln_en_2 = lnn.find('"')
    lnn = lnn[:ln_en_2]
    return lnn

  def file_loader_1_change(self, file, **event_args):
    app_tables.strings.delete_all_rows()
    print(f"The file's name is: {file.name}")
    print(f"The number of bytes in the file is: {file.length}")
    print(f"The file's content type is: {file.content_type}")
    #    print(f"The file's contents are: '{file.get_bytes()}'")
    #    print(file)
    b = file.get_bytes()
    bb = b.decode("utf-8")
    mgl = bb.splitlines()
    lx = mg.lx
    #    anvil.server.call("upload_csv_pols", bbb, "regs")
    i = 0
    idx = 0
    self.file_loader_1.enabled = False
    self.file_loader_1.tooltip = ""
    while i < len(mgl):
      ln = mgl[i]
      if ln.find("[") != -1:
        str_na = ln
        str_na_equ = str_na.find('=')
        str_na = str_na[0:str_na_equ].strip()
        self.load_text.text = mg.loading_tx[lx]+str_na
        en = self.get_str(mgl[i+1])
        de_sie = self.get_str(mgl[i+2])
        de_du = self.get_str(mgl[i+3])
        fr_vous = self.get_str(mgl[i+4])
        no = self.get_str(mgl[i+5])
        app_tables.strings.add_row(name=str_na, en=en, de_sie=de_sie, de_du=de_du,fr_vous=fr_vous,no=no, usr=mg.usr, id=idx)
        idx = idx + 1
        i = i + 6
        # save into db
      i = i + 1
    alert(mg.loaded_tx[lx])
    self.load_done(lx, 0)

  def load_done(self, lx, where):
    self.work_panel.visible = True
    self.load_panel.visible = False
    len_row = len(app_tables.strings.search())
    mg.where = where
    mg.len_row = len_row - 1
    row=app_tables.strings.search()[where]
    lang1_str = self.get_lang_str(row, lx)
    mg.where_name = row['name']
    abc = mg.where_name
    self.lang_1.text = lang1_str
    self.where.text = str(where) + " | "+str(mg.len_row)
    self.ddm_lang_1.placeholder = mg.ddm_lang_1_placeholder[lx]
    self.ddm_lang_1.label = mg.ddm_lang_1_change_language[lx]
    self.lang_1.label = mg.quelltext[lx]
    self.lang_2.label = mg.bearbeitetertext[lx]
    self.ddm_2.placeholder = mg.ddm_lang_1_placeholder[lx]
    self.ddm_2.label = mg.ddm_lang_2_change_language[lx]
    lang2_str = self.get_lang_str(row, lx)
    self.lang_2.text = lang2_str
    mg.where = where
    mg.lx2 = lx

  def next_click(self, **event_args):
    lx1 = mg.lx
    lx2 = mg.lx2
    usr = mg.usr
    abc = mg.len_row
    where_name = mg.where_name
    row = app_tables.strings.get(usr=usr, name=where_name)  
    id = row['id']
    where = mg.where + 1
    if where >= mg.len_row:
      where = 0
      row_next = app_tables.strings.get(usr=usr, id=0)
    else:
      id = id + 1
      row_next = app_tables.strings.get(usr=usr, id=id)
    lang2_str = self.get_lang_str(row_next, lx2) 
    self.lang_2.text = lang2_str
    lang1_str = self.get_lang_str(row_next, lx1)
    self.lang_1.text = lang1_str
    self.where.text = str(where) + " | " + str(mg.len_row)
    mg.where = where
    mg.where_name = row_next['name']
    pass

  def prev_click(self, **event_args):
    """This method is called when the component is clicked."""
    pass

  def get_lang_str(self, ro, lx):
    if lx == 0:
      return ro['en']
    elif lx == 1:
      return ro['de_sie']
    elif lx == 2:
      return ro['de_du']
    elif lx == 3:
      return ro['fr_vous']
    elif lx == 4:
      return ro['no']
    else:
      return ro['en']

  def ddm_lang_1_change(self, **event_args):
    mg.lang_1 = int(self.ddm_lang_1.selected_value)
    lx = mg.lang_1
    usr = mg.usr
    ro = app_tables.strings.get(usr=usr, id=mg.where)
    lang1_str = self.get_lang_str(ro, lx)
    self.lang_1.text = lang1_str
    self.where.text = str( mg.where)+" | "+str(mg.len_row)
    self.ddm_lang_1.placeholder = mg.ddm_lang_1_placeholder[lx]
    self.ddm_lang_1.label = mg.ddm_lang_1_change_language[lx]
    self.lang_1.text = self.get_lang_str(ro, mg.lang_1)
    self.lang_1.label = mg.quelltext[lx]

  def ddm_2_change(self, **event_args):
    mg.lx2 = int(self.ddm_2.selected_value)
    lx2 = mg.lx2
    usr = mg.usr
    ro = app_tables.strings.get(usr=usr, id=mg.where)
    lang2_str = self.get_lang_str(ro, lx2)
    self.lang_2.text = lang2_str
    self.where.text = str( mg.where)+" | "+str(mg.len_row)
    self.ddm_2.placeholder = "self.ddm_2.placeholder  " + mg.ddm_lang_1_placeholder[lx2]
    self.ddm_2.label = "self.ddm_2.label  " + mg.ddm_lang_2_change_language[lx2]
    self.lang_2.text = self.get_lang_str(ro, mg.lx2)
    self.lang_2.label = mg.bearbeitetertext[lx2]

  def button_1_click(self, **event_args):
    """This method is called when the component is clicked."""
    app_tables.nutzer.delete_all_rows()
    app_tables.strings.delete_all_rows()