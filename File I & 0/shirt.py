from PIL import Image, ImageOps

import sys
import os.path

print("First Argument", sys.argv[1].split(".")[1])
print("second Argument",sys.argv[2].split(".")[1])

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")


elif sys.argv[1].split(".")[1] not in ["jpg", "jpeg", "png"]:
    sys.exit(" Invalid output")


elif sys.argv[1].split(".")[1] != sys.argv[2].split(".")[1]:
    sys.exit("Input and output have different extensions")

elif len(sys.argv) == 3:
    path = f"./{sys.argv[1]}"

    if os.path.isfile(path):
        photo = Image.open(sys.argv[1])

        shirt = Image.open("shirt.png")

        photo = ImageOps.fit(photo, shirt.size)
        photo.paste(shirt, shirt)
        photo.save(sys.argv[2])
    else:
        sys.exit("Input does not exist")
