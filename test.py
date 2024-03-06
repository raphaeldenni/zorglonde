from zorglangue_traductor import zorglangue_traductor

assert (
    zorglangue_traductor("Hello world! ; . ? ' + * !? &=bonjour 33/3=11")
    == "Olleh dlrow! ; . ? ' * + ?! ruojnob=& 11=3/33"
)
