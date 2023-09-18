import random
from pyfiglet import Figlet
import sys

def different_fonts():

    figlet = Figlet()

    try:

        if len(sys.argv) < 2:
            user_input = input("Input: ")
            figlet.setFont(font=random.choice(figlet.getFonts()))
            print()
            print(figlet.font)
            print(figlet.renderText(user_input))

        if not len(sys.argv) == 3 or not (sys.argv[1] == "-f" or sys.argv[1] == "--font") or sys.argv[2] not in figlet.getFonts():
            sys.exit("Invalid usage")

        else:
            user_input = input("Input: ")
            figlet.setFont(font=sys.argv[2])
            print(figlet.renderText(user_input))

    except ValueError:
        outdated()

    except IndexError:
        outdated()


different_fonts()