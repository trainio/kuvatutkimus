#PERUSTUU PYTHONIN VALMIISIIN FUNKTIOIHIN
import sys as systeemi
# YLEISTOIMINTOJA
from builtins import print as kirjoita
from builtins import help as apua
from builtins import input as syote
from builtins import open as avaa

from builtins import range as alueella
from builtins import iter as toisto
from builtins import len as pituus


## MUUTTUJIA

from builtins import bool as totuusarvo
from builtins import int as kokonaisluku
from builtins import int as k_luku
from builtins import float as desimaaliluku
from builtins import str as teksti
from builtins import hex as heksadesimaali
from builtins import bin as binaari
from builtins import chr as kirjain_numerolle
from builtins import ord as numero_kirjaimelle




class Totuusarvo:
  def __init__(self, value):
    self.value = value

  def kirjoita_tiedot(self):
    kirjoita("Hello, my value is: " + teksti(self.value))

  def aseta_arvoksi(self, value):
    self.value = value

  def on_tosi(self):
    return self.value


# def ei_tosi():
#     return False
#
# def tosi():
#     return True

# def heksadesimaali(arvo):
#     return hex(arvo)
#
# def desimaaliluku(luku):
#         return float(luku)
#
# def kokonaisluku(luku):
#     return int(luku)
#
# def teksti(t):
#     return str(t)



# MATEMATIIKKAA

from builtins import abs as itseisarvo
from builtins import round as likimain
from builtins import sum as summa


#
# def itseisarvo(luku):
#     return abs(luku)





# TODO: The Python interpreter has a number of functions and types built into it that are always available. They are listed here in alphabetical order.

    # abs()
# delattr()
# hash()
# memoryview()
# set()all()
# dict()
# help()
# min()
# setattr()any()
# dir()
    # hex()
# next()
# slice()
# ascii()
# divmod()
# id()
# object()
# sorted()
# bin()
# enumerate()
# input()
# oct()
# staticmethod()
    # bool()
# eval()
    # int()
# open()
    # str()
# breakpoint()
# exec()
# isinstance()
# ord()
# sum()
# bytearray()
# filter()
# issubclass()
# pow()
# super()
# bytes()
    # float()
# iter()
    # print()
# tuple()
# callable()
# format()
# len()
# property()
# type()
# chr()
# frozenset()
# list()
# range()
# vars()
# classmethod()
# getattr()
# locals()
# repr()
# zip()compile()
# globals()
# map()
# reversed()
# __import__()
# complex()
# hasattr()
# max()
# round()
