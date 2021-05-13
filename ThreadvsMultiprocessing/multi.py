from multiprocessing import Process

from threading import Thread
import os
import time

def square_number(limit):

    for index in range(limit):
        print(index * index)
        index * index

        time.sleep(0.1)


# Process

processes = []
num_process = os.cpu_count()

#create process

for i in range(num_process):
    process = Process(target=square_number, args=([50]))
    processes.append(process)
for p in processes:
    p.start()
for p in processes:
    p.join()

print("end main")

#Thread

threads = []
num_thread = 10

#create thread

for i in range(num_thread):
    # t = Thread(target=square_number, args=([50]))
    t = Thread(target=square_number, args=(50, )) #tuple
    threads.append(t)
for t in threads:
    t.start()
for t in threads:
    t.join()

print("end main")

