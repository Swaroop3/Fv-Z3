from z3 import *

# Declare propositional variables
a = Bool('a')
b = Bool('b')
c = Bool('c')

# Build the formula: (a ∨ b) ∧ (¬a ∨ c) ∧ (¬b ∨ ¬c)
formula = And(
    Or(a, b),
    Or(Not(a), c),
    Or(Not(b), Not(c))
)

# Create solver and add formula
s = Solver()
s.add(formula)

# Check satisfiability
if s.check() == sat:
    print("SAT")
    print("Model:", s.model())
else:
    print("UNSAT")