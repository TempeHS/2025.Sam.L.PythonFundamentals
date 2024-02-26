import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
figfonts = figlet.getFonts()
try:
    if sys.argv[1] == 0:
        random_fig = Figlet(font=random.choice(figfonts))
    elif sys.argv[1] == 2:
        chosen_fig = Figlet()
except:
