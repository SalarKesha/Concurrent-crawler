from multiprocess import multiprocess
from multithread import multithread

if __name__ == "__main__":
    # words to be search
    words = []

    # multiprocess or multithread
    mode = 'mp'
    # mode = 'mt'

    # number of threads or process
    concurrency = 4
    if mode == 'mp':
        multiprocess(words, concurrency)
    elif mode == 'mt':
        multithread(words, concurrency)
    else:
        print('Invalid Mod')
