from contextlib import contextmanager

with open("note11.txt", 'w') as file:
    file.write("todo list")

try:
    file = open('note2.txt', 'w')
    file.write("todo list")
finally:
    file.close()

from threading import Thread, Lock

lock = Lock()
lock.acquire()
#...
lock.release()

with lock:
    pass
    #....

class ManageFile:
    def __init__(self, filename):
        print("init")
        self.filename = filename
    def __enter__(self):
        print("enter")
        self.file = open(self.filename,'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print("exec has been caught")
        return True    #return true to move on
        print('exec:', exc_type, exc_val)
        print('exit')

with ManageFile('note3.txt') as file:
    print("do some stuff")
    file.write("new to do list")
    file.unknowMethod() #exec: <class 'AttributeError'> '_io.TextIOWrapper' object has no attribute 'unknowMethod'
print("continue") #is not reachable



@contextmanager
def open_manage_file(filename):
    file = open(filename, 'w')
    try:
        yield file
    finally:
        file.close()

with open_manage_file("note_content") as f:
    f.write("to do list")


