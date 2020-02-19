import time
def a(b):     # A is wrapped is around b
    def c(*d, **e):
        a = time.time()
        return (b(*d, **e), time.time()-a)
    return c

