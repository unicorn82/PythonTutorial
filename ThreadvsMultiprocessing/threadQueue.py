from threading import Thread, Lock, current_thread
from queue import  Queue

def worker(q, lock):
    while True:
        value = q.get()
        with lock:
            print(f"in {current_thread().name} got {value}")
        q.task_done()


if __name__ == "__main__":
    q = Queue()
    num_threads = 10
    lock = Lock()
    for i in range(num_threads):
        t = Thread(target=worker, args=(q, lock))
        t.daemon = True # make thread die when main thread die
        t.start()

    for i in range(1,20):
        q.put(i)

    q.join()