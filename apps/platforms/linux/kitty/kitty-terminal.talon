app: kitty_terminal
-
# Set tags
tag(): terminal
tag(): user.tabs
tag(): user.generic_unix_shell
tag(): user.git
tag(): user.kubectl

go window <number>: user.window_jump(number)
change layout: user.change_layout()
window move: user.window_move()
window full: user.window_full()
hunt url: user.hunt_url()
search screen [<user.text>]: user.search_screen(user.text or "")
