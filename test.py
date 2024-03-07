from zorglonde import zorglonde


def test_zorglonde():
    assert zorglonde("Hello world! L'effort.") == "Olleh dlrow! L'troffe."


def test_reverse_zorglonde():
    assert zorglonde("Olleh dlrow! L'troffe.", reverse=True) == "Hello world! L'effort."
