import time
def timer(func):
    def wrapper(*args, **kwargs):
        before = time.time()
        func(*args, **kwargs)
        after = time.time()
        print(f"-----------------[{round(after - before, 2)} seconds]-----------------")

    return wrapper
