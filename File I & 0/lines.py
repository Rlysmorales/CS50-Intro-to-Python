import sys
import os.path

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")

elif len(sys.argv) == 2:
    path = f"./{sys.argv[1]}"

    if os.path.isfile(path):
        line_count = []
        with open(sys.argv[1]) as file:
            lines = file.readlines()
            for line in lines:

                if line.startswith("#"):
                    continue
                elif line.lstrip().startswith("#"):
                    continue
                elif line.isspace():
                    continue

                else:
                    line_count.append(line)
        print(len(line_count))
    else:
        sys.exit("File does not exist")
