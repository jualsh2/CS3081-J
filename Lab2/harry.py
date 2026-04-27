from logic import *

rain = Symbol("rain")
hagrid = Symbol("hagrid")
dumbledore = Symbol("dumbledore")
snape = Symbol("snape")

knowledge = And(
    Implication(Not(rain), hagrid),
    Or(hagrid, dumbledore, snape),
    Not(And(hagrid, dumbledore)),
    Not(And(hagrid, snape)),
    Not(And(snape, dumbledore)),
    Implication(rain, Not(snape)),
    snape
)

print(knowledge.formula())
print(model_check(knowledge, rain))