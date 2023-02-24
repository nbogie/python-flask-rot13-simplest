def rot13(text):
    """Return the rot13 encoding of text."""
    inp = "abcdefghijklmnopqrstuvwxyz"
    out = "nopqrstuvwxyzabcdefghijklm"

    def translate(c):
        if c.lower() in inp:
            mapped = out[inp.index(c.lower())]
            return (mapped.upper() if c.isupper() else mapped)
        else:
            return c
    return "".join([translate(c) for c in text])
