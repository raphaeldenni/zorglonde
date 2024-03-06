from zorglangue_traductor import zorglangue_traductor

print("--- Zorglangue program ---\n---  by Raphaël Denni  ---\n")

while True:
    text = input("Enter your string : ")

    zt = zorglangue_traductor(text)

    print(
        f"\nEviv Bulgroz! : {zt}\n\nPress enter for an another sentence or Ctrl+C to quit."
    )

    pause = input()
