import os
import sys
import csv

from tabulate import tabulate
import sys
import os.path

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

elif len(sys.argv) == 2:
    path = f"./{sys.argv[1]}"

    if os.path.isfile(path):
        line_count = []
        with open(sys.argv[1]) as file:

            reader = csv.reader(file)
            for line in reader:
                line_count.append(line)

        print(tabulate(line_count[1:], line_count[0], tablefmt="grid"))
    else:
        sys.exit("File does not exist")



