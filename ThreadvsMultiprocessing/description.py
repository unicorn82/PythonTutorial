
# --------------------- Process ----------------
# Process: An instance of a program (e.g a Python interpreter)
# Takes advantage of multiple CPUs and Cores
# Separate memory space -> Memory is not shared between processes
# Great for CPU-bound processing
# New process is started independently from other processes
# Processes are interruptable/killable
# One GIL for each process -> avoids GIL limitation

# Heavyweight
# Starting a process is slower than starting a thread
# More memory
# IPC (inter-process communication) is more complicated

# --------------------- Thread ----------------
# Threads: An entity within a process that can be scheduled (also known as "lightweight process")
# A process can spawn multiple threads

# All threads within a process share the same memory
# Leightweight
# Starting a thread is faster than starting a process
# Great for I/O-bound tasks

# Threading is limited by GIL: only one thread at a time
# No effect for CPU-bound tasks
# Not interruptable/killable
# Careful with race condition

# --------------------- GIL ----------------
# GIL: Global interpreter lock
# A lock that allows only one thread at a time to execute in Python
# Needed in CPython because memory management is not thread-safe
# Avoid
#  - Use multiprocessing
#  - Use a different, free-threaded Python implementation (Jython, IronPython)
#  - Use Python as a wrapper for third-party library (C/C++) -> numpy, scipy
