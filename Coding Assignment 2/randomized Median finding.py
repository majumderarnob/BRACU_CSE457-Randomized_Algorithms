import math
import random
 
L = [i + 1 for i in range(6561)]
random.shuffle(L)
 

def randomized_median_algorithm(S):
    n = len(S)

    R = [random.choice(S) for i in range(math.ceil(n ** (3 / 4)))]
    R.sort()

    d = R[math.floor((1 / 2) * (n ** (3 / 4)) - math.sqrt(n)) - 1]
    u = R[math.ceil((1 / 2) * (n ** (3 / 4)) + math.sqrt(n)) - 1]
 
    C = [x for x in S if d <= x <= u]
    l_d = len([x for x in S if x < d])
    l_u = len([x for x in S if x > u])
 
    if((l_d > int(n / 2)) or (l_u > int(n / 2))):
        return False
    if (len(C) > 4 * (n ** (3 / 4))):
        return False
 
    C.sort()
 
    try:
        m = C[math.floor(n/2) - l_d]
    except:
        print(f"Exp_idx: {math.floor(n/2) - l_d}")

    return True
 
 
success = 0
fail = 0
for i in range(100):
    if randomized_median_algorithm(L):
        success = success + 1
    else:
        fail = fail + 1
print("number of times the algorithm success: ", success)
print("number of times the algorithm fails: ", fail)

#theoretical calculation
L = 6561
probabilityOFfail =  (L ** (-1/4))
print("With at most", probabilityOFfail, "probability should the median finding algorithm fail on L")