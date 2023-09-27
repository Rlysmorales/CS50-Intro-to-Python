import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:

        regex_ip_address = re.search(
            "(^[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.(["
            "0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])",
            ip)

        if len(ip.split(".")) != 4:
            return False

        elif regex_ip_address:
            split_ip = ip.split(".")
            list_int = [int(i) for i in split_ip]
            if 0 > list_int[0] >= 256:
                return False
            elif any(i >= 256 for i in list_int):
                return False

            return True

        else:
            return False

    except ValueError:
        return False


if __name__ == "__main__":
    main()
