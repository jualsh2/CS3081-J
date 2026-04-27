# import termcolor

# from logic import *

# mustard = Symbol("ColMustard")
# plum = Symbol("ProfPlum")
# scarlet = Symbol("MsScarlet")
# characters = [mustard, plum, scarlet]

# ballroom = Symbol("ballroom")
# kitchen = Symbol("kitchen")
# library = Symbol("library")
# rooms = [ballroom, kitchen, library]

# knife = Symbol("knife")
# revolver = Symbol("revolver")
# wrench = Symbol("wrench")
# weapons = [knife, revolver, wrench]

# symbols = characters + rooms + weapons


# def check_knowledge(knowledge):
#     for symbol in symbols:
#         if model_check(knowledge, symbol):
#             termcolor.cprint(f"{symbol}: YES", "green")
#         elif not model_check(knowledge, Not(symbol)):
#             print(f"{symbol}: MAYBE")


# # There must be a person, room, and weapon.
# knowledge = And(
#     Or(mustard, plum, scarlet),
#     Or(ballroom, kitchen, library),
#     Or(knife, revolver, wrench)
# )

# # Initial cards
# knowledge.add(And(
#     Not(mustard), Not(kitchen), Not(revolver)
# ))

# # Unknown card
# knowledge.add(Or(
#     Not(scarlet), Not(library), Not(wrench)
# ))

# # Known cards
# knowledge.add(Not(plum))
# knowledge.add(Not(ballroom))

# check_knowledge(knowledge)

#Modified code for lab 2
import termcolor

from logic import *

alice = Symbol("AliceSuspect")
bob = Symbol("BobSuspect")
carol = Symbol("CarolSuspect ")
Suspects = [alice, bob, carol]

office = Symbol("office")
garage = Symbol("garage")
basement = Symbol("basement")
Rooms = [office, garage, basement]

poison = Symbol("poison")
rope = Symbol("rope")
candlestick = Symbol("candlestick")
Weapons = [poison, rope, candlestick]

symbols = Suspects + Rooms + Weapons

def check_knowledge(knowledge):
    for symbol in symbols:
        if model_check(knowledge, symbol):
            termcolor.cprint(f"{symbol}: YES", "green")
        elif not model_check(knowledge, Not(symbol)):
            print(f"{symbol}: MAYBE")

knowledge = And(
    Or(alice, bob, carol),
    Or(office, garage, basement),
    Or(poison, rope, candlestick)
)

knowledge.add(And(
        Not(alice), Not(office), Not(poison)))

knowledge.add(Or(
    Not(bob), Not(garage), Not(rope)))

knowledge.add(Not(candlestick))
knowledge.add(Not(basement))


check_knowledge(knowledge)