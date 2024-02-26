import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
figfonts = figlet.getFonts()

if len(sys.argv) == 1:
    figlet.setFont(font=random.choice(figfonts))
elif (
    len(sys.argv) == 3
    and (sys.argv[1] == "-f" or sys.argv[1] == "--fonts")
    and sys.argv[2] in figfonts
):
    figlet.setFont(font=sys.argv[2])
else:
    sys.exit("Invalid usage")

text = input("Input: ")
print(figlet.renderText(text))
