from talon import Context, actions, Module
mod = Module()
# Context matching
ctx = Context()
ctx.matches = r"""
os: linux
and app.name: kitty
and title: History
"""

@mod.action_class
class Actions:
    def forward():
        """Search forward"""
    def backward():
        """Search backwards"""
    def quits():
        """Quit"""
    def search(data: str):
        """Search string"""

@ctx.action_class("self")
class Actions:
    def search(data: str):
        """Search string"""
        actions.insert(f"/{data}")

    def forward():
        """Search forward"""
        actions.key("n")

    def backward():
        """Search backwards"""
        actions.key("N")

    def quits():
        """Quit"""
        actions.key("ctrl-c")
        actions.key("q")