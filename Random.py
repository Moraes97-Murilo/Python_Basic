#let's play some random choices with python
import random

elect = "1s²  2s²  2p6  3s²  3p6  4s²  3d10  4p6  5s²  4d10  5p6  6s²  4f14  5d10"
list_e = elect.split("  ")

atom = random.choice(list_e)

print("What element from periodic table have final electronic configuration like {} ?".format(atom))
