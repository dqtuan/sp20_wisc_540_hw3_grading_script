import sys
import random

# boulderX = -1
# boulderY = -1

def succ(state, boulderX, boulderY):
    # successors differ from state by one variable's row value
    successors = []
    n = len(state)
    for i in range(len(state)):
        # generate all the successors that differ at index i
        for j in range(len(state)):
            if j != state[i] and not (i == boulderX and j == boulderY):
                temp = state[:] # make a copy of the state
                temp[i] = j
                successors.append(temp)
    return successors

def f(state, boulderX, boulderY):
    score = 0
    for i in range(len(state)):
        isAttacking = False
        for j in range(len(state)):
            if i != j:
                # check row with no boulder
                if state[i] == state[j] and not boulderY == state[i]:
                    #print("queen",i,"attacking queen",j)
                    isAttacking = True
                # check row with boulder
                elif state[i] == state[j] and (boulderX<i<j or boulderX<j<i or i<j<boulderX or j<i<boulderX):
                    #print("queen",i,"attacking queen",j)
                    isAttacking = True
                # check diagonals
                elif abs(state[i]-state[j]) == abs(i-j):
                    # no boulder
                    if abs(i-boulderX) != abs(state[i]-boulderY):
                        #print("queen",i,"attacking queen",j)
                        isAttacking = True
                    elif abs(j-boulderX) != abs(state[j]-boulderY):
                        isAttacking = True
                        #print("queen",i,"attacking queen",j)
                    elif (boulderX<i<j or boulderX<j<i or i<j<boulderX or j<i<boulderX):
                        #print("queen",i,"attacking queen",j)
                        isAttacking = True
        if isAttacking:
            score += 1
    return score

def choose_next(state, boulderX, boulderY):
    children = [(c, f(c, boulderX, boulderY)) for c in succ(state, boulderX, boulderY)]
    curr_score = f(state, boulderX, boulderY)
    best_score = curr_score
    higher = []
    equal = [(state, curr_score)]
    for child in children:
        if child[1] == best_score and curr_score > best_score:
            higher.append(child)
        elif child[1] < best_score:
            best_score = child[1]
            higher = []
            higher.append(child)
        elif child[1] == curr_score:
            equal.append(child)

    if len(higher) > 0:
        retval = sorted(higher, key=lambda x: x[0])[0][0]
    else:
        retval = sorted(equal, key=lambda x: x[0])[0][0]

    if retval == state:
        return None
    return retval

def nqueens(init_state, boulderX, boulderY):
    #init_state = [i for i in range(n)]
    #if init_state[boulderX] == init_state[boulderY]:
    #    init_state[boulderX] = (init_state[boulderX]+1)%n

    # print()
    print(init_state,"- f="+str(f(init_state, boulderX, boulderY)))

    prev_state = init_state
    s = succ(init_state, boulderX, boulderY)
 #   for state in s:
 #       print(state,"- f="+str(f(state)))
    x = choose_next(init_state, boulderX, boulderY)

    # print()

    while x != None and f(x, boulderX, boulderY) >= 0:
        print(x,"- f="+str(f(x, boulderX, boulderY)))
        prev_state = x
        x = choose_next(prev_state, boulderX, boulderY)
    return prev_state

def nqueens_restart(n, k, boulderX, boulderY):
    best = []
    bestf = n

    for i in range(k):
        init_state = [random.randint(0,n-1) for x in range(n)]
        while init_state[boulderX] == boulderY:
            init_state = [random.randint(0,n-1) for x in range(n)]

        newstate = nqueens(init_state, boulderX, boulderY)
        newf = f(newstate, boulderX, boulderY)
        if newf == 0:
            # solution
            print(newstate)
            return
        elif newf < bestf:
            bestf = newf
            best = [newstate]
        elif newf == bestf:
            best.append(newstate)

    for state in sorted(best):
        print(state)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("usage: python3 nqueens n boulderX boulderY")
    elif not sys.argv[1].isdigit():
        print("error: n must be a positive integer")
        print("usage: python3 nqueens n boulderX boulderY")
    elif not sys.argv[2].isdigit() or not 0 <= int(sys.argv[2]) < int(sys.argv[1]):
        print("error: boulderX must be an integer 0-"+sys.argv[1])
        print("usage: python3 nqueens n boulderX boulderY")
    elif not sys.argv[3].isdigit() or not 0 <= int(sys.argv[3]) < int(sys.argv[1]):
        print("error: boulderY must be an integer 0-"+sys.argv[1])
        print("usage: python3 nqueens n boulderX boulderY")
    else:
        boulderX = int(sys.argv[2])
        boulderY = int(sys.argv[3])

        #print(choose_next([6,1,5,2,0,3,6,4]))

        #nqueens_restart(int(sys.argv[1]), 5)

        x = nqueens([6, 4, 7, 2, 0, 1, 6, 4])
        print("=>",x)
        #print()
        #print(f([0, 4, 1, 3, 5, 2, 4, 6]))
        #f([4,4,1,3,5,2,4,7])
