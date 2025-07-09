from ._anvil_designer import log_regTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import mg
from anvil.js.window import navigator

class log_reg(log_regTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    ll = navigator["language"]
    my_loc, my_loc2, lx = self.get_lang(ll)
    lx = 3
    mg.lx = lx
    #    lx = 3
    self.regi_title.text = mg.sign_up_title[lx]
    self.regi_user.placeholder = mg.user_placeholder[lx]
    self.regi_save.text = mg.save_btn[lx]
    self.regi_cancel.text = mg.cancel_btn[lx]
    self.regi_first.text = mg.regi_first_tx[lx]
    #    self.regi_user.tooltip = lu.regi_user_tt[lx]
    self.new_user = {"ur": '', "pr": ''}
    self.login_title.text = mg.login_title_tx[lx]
    self.login_u.placeholder = mg.login_u_tx[lx]
    self.login_save.text = mg.login_title_tx[lx]
    self.login_cancel.text = mg.cancel_btn[lx]
    self.login_first.text = mg.login_first_btn[lx]
    self.regi_info.text = mg.regi_privacy_str[lx]

    self.log_in.visible = False 

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

  def login_u_change(self, **event_args):
    """This method is called when the text in this component is edited."""
    pass

  def login_p_change(self, **event_args):
    """This method is called when the text in this component is edited."""
    self.login_err.visible = False
    pass

  def login_save_click(self, **event_args):
    self.login_err.visible = False
    lx = mg.my_lang
    #    lx = 4
    usr = self.login_u.text
    rows = app_tables.nutzer.search(email=usr)
    lenrows = len(rows)
    if len(rows) == 1:
      self.new_user['u'] = self.login_u.text
      self.new_user['ur'] = 'up'
      mg.signup_cancel = False 
      mg.my_email = self.login_u.text
      self.raise_event("x-close-alert", value=self.new_user)
    elif lenrows == 0:
      self.login_err.visible = True
      self.login_err.text = mg.err_user_not_exits[lx]
      self.login_u.focus()

  def login_cancel_click(self, **event_args):
    self.login_err.visible = False
    lx = mg.my_lang
    #    lx = 3
    self.raise_event("x-close-alert", value=342)
    n = Notification(mg.sorry[lx], style="warning")
    n.show()

  def login_first_click(self, **event_args):
    """This method is called when the component is clicked."""
    self.log_in.visible = True 
    self.register.visible = False

  def regi_user_change(self, **event_args):
    self.regi_user_err.visible = False
    lx = mg.my_lang
    #    lx = 4
    if len(self.regi_user.text) < 3:
      self.regi_user_err.visible = True
      self.regi_user_err.text = mg.err_username1[lx]
    elif len(self.regi_user.text) > 15:
      self.regi_user_err.visible = True
      self.regi_user_err.text = mg.err_username2[lx]
    else:
      self.regi_user_err.visible = False

  def regi_save_click(self, **event_args):
    """This method is called when the component is clicked."""
    lx = mg.my_lang
    #    lx = 4
    if len(self.regi_user.text) == 0:
      self.regi_user_err.visible = True
      self.regi_user_err.text = mg.err_username3[lx]
      self.regi_user.focus()
      return
    elif len(self.regi_user.text) > 0 and len(self.regi_user.text) < 3:
      self.regi_user_err.visible = True
      self.regi_user_err.text = mg.err_username1[lx]
      return
    elif len(self.regi_user.text) > 15:
      self.regi_user_err.visible = True
      self.regi_user_err.text = mg.err_username2[lx]
      return
      ## check against database
    usr = self.regi_user.text
    row = app_tables.nutzer.get(email=usr)
    if row is None:
      res = anvil.server.call('nuts_pwd', usr)
      self.new_user['u'] = usr
      mg.signup_cancel = False 
      self.raise_event("x-close-alert", value=self.new_user)
    else:
      self.regi_user_err.visible = True
      self.regi_user_err.text = mg.err_username_exists[lx]

  def regi_cancel_click(self, **event_args):
    lx = mg.my_lang
    #    lx = 3
    self.raise_event("x-close-alert", value=42)
    n = Notification(mg.sorry[lx], style="warning")
    n.show()
    """This method is called when the component is clicked."""

  def regi_first_click(self, **event_args):
    self.log_in.visible = False 
    self.register.visible = True
    """This method is called when the component is clicked."""
    pass

  def regi_user_show(self, **event_args):
    self.regi_user.focus()
    pass

  def login_u_show(self, **event_args):
    self.login_u.focus()
    pass

  def adm_pw_pressed_enter(self, **event_args):
    pw = self.adm_pw.text
    if pw == 'ft27':
      self.raise_event("x-close-alert", value='admin')
    else:
      n = Notification("Sorry, wrong password", style="Warning")
      n.show()

  def adm_btn_click(self, **event_args):
    self.adm_card2.visible = True
    self.register.visible = False
    self.log_in.visible = False
    pass

  def adm_pw_show(self, **event_args):
    self.adm_pw.focus()
