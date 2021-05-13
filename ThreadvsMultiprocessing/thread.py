from threading import Thread, Lock
from queue import  Queue
import time

database_value = 0

database_value_lock = 0

def increase():
    global database_value
    # database_value += 1
    local_copy = database_value
    local_copy += 1
    time.sleep(0.1)
    database_value = local_copy

def increase_lock(lock):
    print("thread start")
    global database_value_lock

    # lock.acquire()
    # print(" thread lock")
    # local_copy = database_value_lock
    # local_copy += 1
    # time.sleep(0.1)
    # database_value_lock = local_copy
    # lock.release()
    with lock:
        local_copy = database_value_lock
        local_copy += 1
        time.sleep(0.1)
        database_value_lock = local_copy

    print((" thread release"))


if __name__ == "__main__":
    threads = []
    num_thread = 10
     # create thread

    for i in range(num_thread):
        t = Thread(target=increase)
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()


    threads_lock = []
    lock = Lock()
    for i in range(num_thread):
        t = Thread(target=increase_lock, args=(lock,))
        threads_lock.append(t)
    for t in threads_lock:
        t.start()
    for t in threads_lock:
        t.join()

    print("data value", database_value)  # data value 1 without lock
    print("data value with lock", database_value_lock)  # data value with lock 10
    print("end main")


