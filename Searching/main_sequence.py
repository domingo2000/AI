import AB_secuence
from searching import SearchSolver
from sequence_parameters import SEQ, ALGORITHM
import time

start = time.time()

# Create the sequence, the solver and execute the solver
sequence = AB_secuence.sequence_creator(100)
sequence = SEQ
solver = SearchSolver(sequence, AB_secuence.expand_seq, AB_secuence.is_goal)
solution = solver.solve(ALGORITHM)
if solution:
    print(f"solution: {solution}")
else:
    print("FAILURE")


print(f"time : {time.time() - start}")
