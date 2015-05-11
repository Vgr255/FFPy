import collections as _collections
_stats = _collections.namedtuple("stats", "health strength magic defense spirit speed")

_TODO = """
Stats growth curve (I'd rather it not be linear) for each stats and level
Maybe more stats (can't think of more right now)
A way to calculate... stuff? I forgot. -Vgr
"""

class Character:
    def __init__(self):
        raise TypeError

    def __repr__(self):
        if self.letter is not None:
            if self.num is not None:
                return "<%s (%s - #%s) - S-Team #%s>" % (self.name, self.letter, self.rank, self.num)
            return "<%s (%s - #%s)>" % (self.name, self.letter, self.rank)
        if self.num is not None:
            return "<%s - S-Team #%s>" % (self.name, self.num)
        return self.name

class AryaAlexander(Character):
    def __init__(self):
        self.name = "Arya Alexander"
        self.letter = "A"
        self.rank = 25
        self.num = 0

class Brandon(Character):
    def __init__(self):
        self.name = "Brandon"
        self.letter = "B"
        self.rank = 8
        self.num = None

class Charles(Character):
    def __init__(self):
        self.name = "Charles"
        self.letter = "C"
        self.rank = 22
        self.num = None

class Diana(Character):
    def __init__(self):
        self.name = "Diana"
        self.letter = "D"
        self.rank = 17
        self.num = None

class Fanny(Character):
    def __init__(self):
        self.name = "Fanny"
        self.letter = "F"
        self.rank = 2
        self.num = None

class GhiMartin(Character):
    def __init__(self):
        self.name = "Ghi Martin"
        self.letter = "G"
        self.rank = 6
        self.num = None

class AshlynCormier(Character):
    def __init__(self):
        self.name = "Ashlyn Cormier"
        self.letter = "H"
        self.rank = 19
        self.num = None

class Isa(Character):
    def __init__(self):
        self.name = "Isa"
        self.letter = "I"
        self.rank = 21
        self.num = None

class Jordan(Character):
    def __init__(self):
        self.name = "Jordan"
        self.letter = "J"
        self.rank = 15
        self.num = None

class KatelynJackson(Character):
    def __init__(self):
        self.name = "Katelyn Jackson"
        self.letter = "K"
        self.rank = 12
        self.num = 1

class AnabellaLiakin(Character):
    def __init__(self):
        self.name = "Anabella Liakin"
        self.letter = "L"
        self.rank = 26
        self.num = 6

class JeremyAlexander(Character):
    def __init__(self):
        self.name = "Jeremy Alexander"
        self.letter = "M"
        self.rank = 20
        self.num = 3

class Nate(Character):
    def __init__(self):
        self.name = "Nate"
        self.letter = "N"
        self.rank = 10
        self.num = None

class Audrey(Character):
    def __init__(self):
        self.name = "Audrey"
        self.letter = "O"
        self.rank = 9
        self.num = None

class P(Character):
    def __init__(self):
        self.name = "P"
        self.letter = "P"
        self.rank = 18
        self.num = None

class Quan(Character):
    def __init__(self):
        self.name = "Quan"
        self.letter = "Q"
        self.rank = 13
        self.num = None

class Rachel(Character):
    def __init__(self):
        self.name = "Rachel"
        self.letter = "R"
        self.rank = 7
        self.num = None

class Samuel(Character):
    def __init__(self):
        self.name = "Samuel"
        self.letter = "S"
        self.rank = 5
        self.num = None

class Tania(Character):
    def __init__(self):
        self.name = "Tania"
        self.letter = "T"
        self.rank = 23
        self.num = None

class U(Character):
    def __init__(self):
        self.name = "U"
        self.letter = "U"
        self.rank = 3
        self.num = None

class Victor(Character):
    def __init__(self):
        self.name = "Michael Cormier"
        self.letter = "V"
        self.rank = 4
        self.num = 9

class LukeWalker(Character):
    def __init__(self):
        self.name = "Luke Walker"
        self.letter = "W"
        self.rank = 11
        self.num = None

class X(Character):
    def __init__(self):
        self.name = "X"
        self.letter = "X"
        self.rank = 16
        self.num = None

class Y(Character):
    def __init__(self):
        self.name = "Y"
        self.letter = "Y"
        self.rank = 24
        self.num = None

class Zoe(Character):
    def __init__(self):
        self.name = "Zoe"
        self.letter = "Z"
        self.rank = 1
        self.num = None

class AmeliaBater(Character):
    def __init__(self):
        self.name = "Amelia Bater"
        self.letter = None
        self.rank = None
        self.num = 2

class MatthewJotkins(Character):
    def __init__(self):
        self.name = "Matthew Jotkins"
        self.letter = None
        self.rank = None
        self.num = 4

class GeraldKennedy(Character):
    def __init__(self):
        self.name = "Gerald Kennedy"
        self.letter = None
        self.rank = None
        self.num = 5

class MarisaMerkel(Character):
    def __init__(self):
        self.name = "Marisa Merkel"
        self.letter = None
        self.rank = None
        self.num = 7

class SimonRookwell(Character):
    def __init__(self):
        self.name = "Simon Rookwell"
        self.letter = None
        self.rank = None
        self.num = 8
