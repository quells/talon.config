from talon.voice import Context, Key

context = Context("go")

def back(n):
    return Key(" ".join(["left"] * n))

context.keymap(
    {
        "go funk": ["func () {}", back(5)],
        "go var": "var ",
        "go error": "err",
        "go error check": ["if err != nil {}", back(1)],
        "go assign [to]": " := ",
    }
)
