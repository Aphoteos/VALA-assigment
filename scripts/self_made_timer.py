from time import time


def timer_func(func):
    # This function shows the execution time of  
    # the function object passed 
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        resultTime = t2-t1
        print(f'Executed in {(t2-t1):.4f} seconds')
        return result, resultTime
    return wrap_func