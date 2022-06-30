import random
from essential_generators import *
import time
from rich.console import Console

c = Console()
gen = MarkovWordGenerator()


def randLst(lst):
    return lst[random.randint(0, len(lst)-1)]


text_colours = ["red", "green", "blue"]
temp = 0

while temp < 10:
    c.print(f"[{randLst(text_colours)}]" + gen.gen_text())
    temp += 1
c.print(f"[{randLst(text_colours)}]HI!")
c.input(f"Press {gen.gen_word()} to {gen.gen_word()}...")
time.sleep(5)
