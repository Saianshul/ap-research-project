import cProfile

def idk(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

cProfile.run('idk(10)')