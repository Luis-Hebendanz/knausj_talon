from talon import app, Module, Context, actions, ui, imgui, settings, app, registry


ctx = Context()
mod = Module()
ctx.matches = r"""
tag: user.generic_unix_shell
"""

@ctx.action_class("user")
class Actions:
    # implements the function from generic_terminal.talon for unix shells

    def terminal_list_directories():
        """Lists directories"""
        actions.insert("ls")
        actions.key("enter")

    def terminal_list_all_directories():
        """Lists all directories including hidden"""
        actions.insert("ls -a")
        actions.key("enter")

    def terminal_change_directory(path: str):
        """Lists change directory"""
        actions.insert("cd {}".format(path))
        if path:
            actions.key("enter")

    def terminal_change_directory_root():
        """Root of current drive"""
        actions.insert("cd /")
        actions.key("enter")

    def search_history(data: str):
        """Searches through the previously executed commands"""
        actions.insert(f"$(cat $HISTFILE | sed 's/.*;//g'  | fzf)")
        actions.key("enter")
        actions.insert(data)

    def edit(data: str):
        """Opens the code editor"""
        actions.insert(f"$EDITOR {data}")

    def search_file(path: str):
        """Searches for a file"""
        actions.insert("fd {}".format(path))


    def search_string(data: str):
        """Searches for a file"""
        actions.insert("ag \"{}\"".format(data))


    def terminal_clear_screen():
        """Clear screen"""
        actions.insert("clear")
        actions.key("enter")

    def terminal_run_last():
        """Repeats the last command"""
        actions.key("up enter")

    def terminal_rerun_search(command: str):
        """Searches through the previously executed commands"""
        actions.key("ctrl-r")
        actions.insert(command)

    def terminal_kill_all():
        """kills the running command"""
        actions.key("ctrl-c")
        actions.insert("y")
        actions.key("enter")
