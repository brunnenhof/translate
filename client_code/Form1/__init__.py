from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def admin_pw_pressed_enter(self, **event_args):
    if self.admin_pw.text == 'ft27':
      self.admin_pw.visible = False
    else:
      self.load_panel.visible = True
      pass

  def admin_click(self, **event_args):
    """This method is called when the component is clicked."""
    self.admin_pw.visible = True
