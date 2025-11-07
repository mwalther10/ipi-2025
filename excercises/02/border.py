height = int(input("Höhe: "))
width = int(input("Breite: "))
character = input("Zeichen: ")

print(
    character * width
    + "\n"
    + (height - 2) * (character + (width - 2) * " " + character + "\n")
    + character * width
)
##############################

# for-loop version
print(character * width)

for _ in range(height - 2):
    print(character + " " * (width - 2) + character)

print(character * width)
