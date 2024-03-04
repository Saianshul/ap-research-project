from memory_profiler import profile

@profile
def something():
    print('hello')

something()