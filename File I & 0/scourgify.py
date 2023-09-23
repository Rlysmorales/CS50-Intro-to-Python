import os
import sys
import csv

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

elif len(sys.argv) == 3:
    path = f"./{sys.argv[1]}"

    if os.path.isfile(path):
        list_of_elements = []
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            for line in reader:
                list_of_elements.append(line)

        my_list = []
        counter = 1
        for element in list_of_elements:
            if counter == 1:
                first_element = element[0]
                replace_element = first_element.replace("name", "first")
                second_element = element[1]
                separating_elements = replace_element.split(", ")
                reverse_list = separating_elements[::-1]
                my_list += reverse_list
                my_list.append(second_element)

            elif counter == 2:

                my_list.insert(1, "last")
                first_element = element[0]
                second_element = element[1]
                separating_elements = first_element.split(", ")
                reverse_list = separating_elements[::-1]
                my_list += reverse_list
                my_list.append(second_element)

            else:

                first_element = element[0]
                second_element = element[1]
                separating_elements = first_element.split(", ")
                reverse_list = separating_elements[::-1]
                my_list += reverse_list
                my_list.append(second_element)

            counter += 1

        smaller_list = [my_list[i:i + 3] for i in range(0, len(my_list), 3)]

        with open(sys.argv[2], "w", newline="") as f:
            writer = csv.writer(f)

            writer.writerows(smaller_list)
    else:
        sys.exit("File does not exist")
