from threading import Thread
from crawler import crawl_mt
from timer import timer
from crawler import q
from storage import store


@timer
def multithread(words, concurrency):
    for word in words:
        q.put(word)
    for i in range(concurrency):
        t = Thread(target=crawl_mt, daemon=True)
        t.start()
    q.join()
    store()
    print("Task Done Successfully")
