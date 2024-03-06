from zorglangue_traductor import zorglangue_traductor


def test_zorglangue_traductor():
    assert zorglangue_traductor("Hello world! L'effort.") == "Olleh dlrow! L'troffe."
