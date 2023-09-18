def outdated():
    month_list = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    loop_true = True
    try:
        while loop_true:
            user_input = input("Date: ").strip()
            split_input = user_input.split("/")
            length_string = len(split_input)

            if length_string != 3:
                string_split = user_input.split(" ")
                string_month = string_split[0]
                string_day = string_split[1]
                day_character = string_day.replace(",", "")
                int_day = int(day_character)
                string_year = string_split[2]
                len_string = len(string_split)

                if len_string != 3:
                    loop_true = True
                elif int_day > 31:
                    loop_true = True
                elif string_month not in month_list:
                    loop_true = True
                elif not string_day.endswith(","):
                    loop_true = True
                elif len(string_year) != 4:
                    loop_true = True
                elif month_list.index(string_month) + 1 > 12:
                    loop_true = True
                else:
                    month_index = month_list.index(string_month) + 1
                    # final_month = month_index + 1
                    print(f"{string_year}-{month_index:02}-{int_day:02}")
                    loop_true = False

            elif len(split_input[2]) != 4:
                loop_true = True
            elif int(split_input[1]) > 31:
                loop_true = True
            elif int(split_input[0]) > 12:
                loop_true = True
            elif len(split_input[2]) == 4:
                user_month = int(split_input[0])
                user_day = int(split_input[1])
                user_year = split_input[2]
                print(f"{user_year}-{user_month:02}-{user_day:02}")
                loop_true = False

    except ValueError:
        outdated()

    except IndexError:
        outdated()


outdated()
