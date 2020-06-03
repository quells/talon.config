from talon.voice import Context, Key

context = Context("Safari", bundle="com.apple.Safari")

keymap = {
    "(address bar | go address | go url)": Key("cmd-l"),
    "go back[ward]": Key("cmd-["),
    "forward": Key("cmd-]"),
    "new [tab]": Key("cmd-n"),
    "close [tab]": Key("cmd-w"),
    "safari (find | marco)": Key("cmd-f"),
    "dev tools": Key("cmd-alt-i"),
}

context.keymap(keymap)
