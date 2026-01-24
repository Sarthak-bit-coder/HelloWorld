# thread = a flow of execution in a program
#         like a separate order of instructions
#         GIL = Global Interpreter Lock
#         allows only one thread to hold the control of the Python interpreter at any one time

# cpu bound = program/task that spends most of its time waiting for internal events (CPU intensive)
# Ex. calculating Fibonacci numbers, processing images

# io bound = program/task that spends most of its time waiting for external events (input/output intensive)
# Ex. web scraping, reading/writing files, network operations

from multiprocessing import Process, cpu_count
import threading
import time


def eat_breakfast():
    time.sleep(3)
    print("You ate breakfast")


def drink_coffee():
    time.sleep(4)
    print("You drank coffee")


def study():
    time.sleep(5)
    print("You studied")


x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

x.join()  # wait until thread x is completed
y.join()  # wait until thread y is completed
z.join()  # wait until thread z is completed

# eat_breakfast()
# drink_coffee()
# study()

print(threading.active_count())  # number of thread objects currently alive
print(threading.current_thread())  # returns the current thread object
# returns the value (in fractional seconds) of a performance counter, i.e. a clock with the highest available resolution to measure a short duration
print(time.perf_counter())

# Ex. Like the quiz game that was io bound, we could have added a timer saying you have 10 seconds to answer each question which is an example of multithreading


# daemon thread = a thread that runs in the background, not important to run program to run
#                 your program will not wait for daemon threads to complete before exiting
#                 non-daemon threads cannot normally be terminated until they complete their work

#                 ex. background tasks, garbage collection, waiting for incoming connections


def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("You were logged in for:", count, "seconds", end="\r")


# daemon=True makes this a daemon thread
x = threading.Thread(target=timer, daemon=True)
x.start()

# x.setDaemon(True)  # another way to set a thread as a daemon thread

answer = input("Do you want to exit?:")

# Multiprocessing = a package that supports spawning processes using an API similar to the threading module
#                   multiprocessing is used to bypass the GIL and utilize multiple processors on a machine
#                   multithreading is used to run multiple threads (tasks, function calls) at once within a single process


def counter(num):
    count = 0
    while count < num:
        count += 1


def main():

    a = Process(target=counter, args=(500000000000,))
    a.start()

    c = Process(target=counter, args=(500000000000,))
    c.start()

    d = Process(target=counter, args=(500000000000,))
    d.start()

    b = Process(target=counter, args=(500000000000,))
    b.start()

    a.join()
    b.join()
    c.join()
    d.join()

    print("Finished in:", time.perf_counter(), "seconds")


if __name__ == "__main__":
    main()
