from zorglonde import zorglonde

print("--- Zorglonde program ---\n---  by Raphaël Denni  ---\n")

while True:
    text = input("Enter your string : ")

    zorg = zorglonde(text)

    print(
        f"\nEviv Bulgroz! : {zorg}\n\nPress enter for an another sentence or Ctrl+C to quit."
    )

    pause = input()
