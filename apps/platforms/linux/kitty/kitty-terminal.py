from talon import Context, actions, Module


# App definition
mod = Module()
mod.apps.kitty_terminal = """
os: linux
and app.name: kitty
"""

# Context matching
ctx = Context()
ctx.matches = r"""
app: kitty
"""

@mod.action_class
class Actions:
    def window_jump(number: int):
        """Jumps to window number """
        actions.key(f"ctrl-{number}")

    def change_layout():
        """Change layout """
        actions.key("ctrl-shift-l")
    def window_move():
        """Move window """
        actions.key("ctrl-shift-f")
    def window_full():
        """ Maximizes current window"""
        actions.key("f11")

    def hunt_url():
        """Hunt for url"""
        actions.key("ctrl-shift-e")

    def search_screen(data: str):
        """Search screen"""
        actions.key("ctrl-shift-h")

# --- Implement actions ---
@ctx.action_class("user")
class user_actions:
    # user.tabs
    def tab_jump(number):
        actions.key(f"-{number}")

    def terminal_clear_screen():
        actions.edit.delete_line()
        actions.key("ctrl-l")

    def terminal_kill_all():
        """kills the running command"""
        actions.key("ctrl-c")

@ctx.action_class("app")
class app_actions:
    # app.tabs
    def tab_open(): actions.key("ctrl-shift-t")
    def tab_previous(): actions.key("ctrl-pageup")
    def tab_next(): actions.key("ctrl-pagedown")
    def tab_close(): actions.key("ctrl-shift-q")
    # global (overwrite linux/app.py)
    def window_open(): actions.key('ctrl-enter')
    def window_close(): actions.key('ctrl-shift-w')
    def window_next():
        actions.key("ctrl-up")
    def window_previous():
        actions.key("ctrl-down")


# global (overwrite linux/edit.py)
@ctx.action_class('edit')
class EditActions:
    def page_down(): actions.key('shift-pagedown')
    def page_up(): actions.key('shift-pageup')
    def paste(): actions.key('ctrl-shift-v')
    def copy(): actions.key('ctrl-shift-c')
    def find(text: str = None):
        actions.key('ctrl-shift-f')
        if text:
            actions.insert(text)
    def delete_line():
        actions.edit.line_start()
        actions.key('ctrl-k')

    # afaik not possible in gnome-terminal
    def extend_left(): pass
    def extend_right(): pass
    def extend_up(): pass
    def extend_down(): pass
    def extend_word_left(): pass
    def extend_word_right(): pass
