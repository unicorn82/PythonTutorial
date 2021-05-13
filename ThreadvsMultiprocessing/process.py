from multiprocessing import Process, Value, Array, Lock, Queue
import os
import time



def add_100(number):
    for i in range(100):
        number.value += 1
        time.sleep(0.01)


def add_100_withLock(number, lock):
    for i in range(100):
        with lock:
            number.value += 1
            time.sleep(0.01)

def add_100_Array_withLock(array, lock):
    for i in range(100):
        time.sleep(0.01)
        for index in range(len(array)):
            with lock:
                array[index] += 1

def convert_negative(numbers, queue):
    for i in numbers:
        queue.put(-1*i)


if __name__ == '__main__':
    share_number = Value('i',0)
    print(type(share_number))
    print('Number at beginning is', share_number.value)
    p1 = Process(target=add_100, args=(share_number,))
    p2 = Process(target=add_100, args=(share_number,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('Number at end is', share_number.value)

    share_number_lock = Value('i', 0)
    lock = Lock()
    print('Number with lock  at beginning is', share_number_lock.value)
    p3 = Process(target=add_100_withLock, args=(share_number_lock,lock))
    p4 = Process(target=add_100_withLock, args=(share_number_lock,lock))

    p3.start()
    p4.start()

    p3.join()
    p4.join()

    print('Number with lock at end is', share_number_lock.value)

    share_array = Array('d', [0.0, 100.0, 200.0])
    lock2 = Lock()
    print('Array with lock  at beginning is', share_array[:])
    p5 = Process(target=add_100_Array_withLock, args=(share_array,lock2))
    p6 = Process(target=add_100_Array_withLock, args=(share_array,lock2))

    p5.start()
    p6.start()
    p5.join()
    p6.join()
    print('Array with lock  at end is', share_array[:])

    q = Queue()
    numbers = range(1,6)

    p7 = Process(target=convert_negative, args=(numbers, q))
    p8 = Process(target=convert_negative, args=(numbers, q))

    p7.start()
    p8.start()
    p7.join()
    p8.join()


    while not q.empty():
        print(q.get())

