"""
    @author: Tuan Dinh (tuan.dinh@wisc.edu)
    Test cases for HW3 - 540 - Spring 2020
"""

testset = {}

# succ(state, boulderX, boulderY): 2, 4, 4
testset['0'] = [
    {'state': [1, 1, 2], 'boulder': [0, 0], 'score': 2},
    {'state': [2, 0, 4, 4, 1], 'boulder': [2, 3], 'score': 4},
    {'state': [1, 3, 0, 5, 0, 1, 4], 'boulder': [2, 2], 'score': 4},
]

# f(state, boulderX, boulderY): 2, 4, 4
# 10: boulder not affect score
# 10
testset['1'] = [
    # non-effect
    {'state': [1, 2, 2], 'boulder': [1, 1], 'f': 3, 'score': 2},
    {'state': [2, 0, 4, 4, 1], 'boulder': [1, 2], 'f':3, 'score': 4},
    {'state': [1, 3, 0, 5, 0, 1, 4], 'boulder': [3, 2], 'f':7, 'score': 4},
    # affect
    {'state': [0, 0, 2], 'boulder': [1, 1], 'f': 2, 'score': 2},
    {'state': [2, 1, 4, 4, 1], 'boulder': [1, 3], 'f':2, 'score': 4},
    {'state': [1, 3, 0, 5, 0, 1, 4], 'boulder': [3, 1], 'f':5, 'score': 4},
]

# choose_next(curr, boulderX, boulderY):
# - 10: better state
# - 10: plateau
# - 10: None
# - a state of None
testset['2'] = [
    {'state': [1, 1, 2], 'boulder': [0, 0], 'output': [1, 0, 2], 'score': 2},#better state
    {'state': [2, 0, 4, 4, 1], 'boulder': [1, 2], 'output':[2, 0, 2, 4, 1], 'score': 4},
    {'state': [1, 3, 0, 5, 0, 1, 4], 'boulder': [3, 2], 'score': 4},

    {'state': [0, 0, 2], 'boulder': [1, 1], 'output': 'None', 'score': 2},# None
    {'state': [2, 0, 4, 4, 1], 'boulder': [1, 3], 'output': 'None', 'score': 4},
    {'state': [1, 3, 0, 6, 2, 5, 1], 'boulder': [3, 1], 'output': 'None', 'score': 4},

    {'state': [1, 2, 2], 'boulder': [1, 0], 'output': [0, 2, 2], 'score': 2}, # plateau
    {'state': [2, 0, 4, 4, 1], 'boulder': [1, 4], 'output':[2, 0, 2, 4, 1], 'score': 4},
    {'state': [1, 3, 0, 5, 0, 1, 4], 'boulder': [3, 2], 'output': [1, 3, 0, 5, 0, 1, 6], 'score': 4},
]

# nqueens(initial_state, boulderX, boulderY): 2, 4, 4
# - 10: terminal state
# - 10: print correct seq (dont care f)
testset['3'] = [
    {'state': [0,1,2,3,5,5,6,7], 'boulder': [4, 4], 'score': 2},
    {'state': [0,2,2,3,4,5,6,7], 'boulder': [1, 1], 'score': 2},
    {'state': [1, 1, 2], 'boulder': [0, 0], 'score': 2},
    {'state': [2, 0, 4, 4, 1], 'boulder': [1, 2], 'score': 2},
    {'state': [1, 3, 0, 5, 0, 1, 4], 'boulder': [3, 2], 'score': 2},
]

# nqueens_restart(n, k, boulderX, boulderY): 5, 5, 5, 5
# - 10: a different random initial valid state each start
# - 10: correct output after <= 10 runs: SOLUTION
testset['4'] = [
    {'n': 3, 'k': 1, 'boulder': [1, 1], 'score': 2},
    {'n': 3, 'k': 3, 'boulder': [1, 2], 'score': 2},
    {'n': 4, 'k': 5, 'boulder': [2, 2], 'score': 2},
    {'n': 4, 'k': 7, 'boulder': [3, 0], 'score': 2},
    {'n': 5, 'k': 9, 'boulder': [3, 2], 'score': 2},
]
