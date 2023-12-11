from multiprocessing import Pool
from crawler import crawl_mp
from storage import store
from timer import timer


@timer
def multiprocess(words, concurrency):
    pool = Pool(concurrency)
    with pool:
        pool.map(crawl_mp, words)
    store()
    print("Task Done Successfully")
