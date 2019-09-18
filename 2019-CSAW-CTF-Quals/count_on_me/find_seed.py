import random

def repeat(x): 
    _size = len(x)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated

def check_pos(seed, val):
    random.seed(seed)
    rand_list = []
    for _ in range(300):
        rand_list.append(random.getrandbits(32))

    cycle = 0
    found = False
    for i in range(0,len(rand_list),3):
        if rand_list[i] == val:
            print(1)
            print(cycle)
        elif rand_list[i+1] == val:
            print(2)
            print(cycle)
            found = True
        elif rand_list[i+2] == val:
            print(3)
            print(cycle)

        cycle += 1
        
    return found

for i in range(1111111111143950,1111111111211111):
    random.seed(i)

    rand_list = []
    for _ in range(300):
        rand_list.append(random.getrandbits(32))

    repeated = repeat(rand_list)
    if len(repeated) > 0:
        if(check_pos(i, repeated[0])):
            print(i)
            print(rand_list)
            break