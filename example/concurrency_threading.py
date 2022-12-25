#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
threading — Thread-based parallelism

https://docs.python.org/3/library/threading.html

This module constructs higher-level threading interfaces on top of the lower level _thread module.


When to use Python threading

As introduced in the process and thread tutorial, there’re two main tasks:

    I/O-bound tasks – the time spent on I/O is significantly more than the time spent on computation
    CPU-bound tasks – the time spent on computation is significantly higher than the time waiting for I/O.

Python threading is optimized for I/O bound tasks. For example, requesting remote resources, connecting a database server, or reading and writing files.


Summary

    Use the Python threading module to create a multi-threaded application.
    Use the Thread(function, args) to create a new thread.
    Call the start() method of the Thread class to start the thread.
    Call the join() method of the Thread class to wait for the thread to complete in the main thread.
    Only use threading for I/O bound processing applications.

"""


print()
print("==============Example 1==============")

print()
print("==============Example 1: Single-threaded==============")

from time import sleep, perf_counter

def task():
    print('Starting a task...')
    sleep(1)
    print('done')


start_time = perf_counter()

task()
task()

end_time = perf_counter()

print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')

print()
print("==============Example 1: multi-threaded==============")

from time import sleep, perf_counter
from threading import Thread


def task():
    print('Starting a task...')
    sleep(1)
    print('done')


start_time = perf_counter()

# create two new threads
t1 = Thread(target=task)
t2 = Thread(target=task)

# start the threads
t1.start()
t2.start()

# wait for the threads to complete
t1.join()
t2.join()

end_time = perf_counter()

print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')

print()
print("==============Example 1: Passing arguments to threads==============")

from time import sleep, perf_counter
from threading import Thread


def task(id):
    print(f'Starting the task {id}...')
    sleep(1)
    print(f'The task {id} completed')


start_time = perf_counter()

# create and start 10 threads
threads = []
for n in range(1, 11):
    t = Thread(target=task, args=(n,))
    threads.append(t)
    t.start()

# wait for the threads to complete
for t in threads:
    t.join()

end_time = perf_counter()

print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')

print()
print("==============Example 2: A Practical Python threading example==============")

print("==============Example 2: Single-threaded==============")

from time import perf_counter


def replace(filename, substr, new_substr):
    print(f'Processing the file {filename}')
    # get the contents of the file
    with open(filename, 'r') as f:
        content = f.read()

    # replace the substr by new_substr
    content = content.replace(substr, new_substr)

    # write data into the file
    with open(filename, 'w') as f:
        f.write(content)
        f.write("Example 2: Single-threaded\n")


def main1():
    filenames = [
        '../testdata/test1.txt',
        '../testdata/test2.txt',
        '../testdata/test3.txt',
        '../testdata/test4.txt',
        '../testdata/test5.txt',
        '../testdata/test6.txt',
        '../testdata/test7.txt',
        '../testdata/test8.txt',
        '../testdata/test9.txt',
        '../testdata/test10.txt',
    ]

    for filename in filenames:
        replace(filename, 'ids', 'id')


if __name__ == "__main__":
    start_time = perf_counter()

    main1()

    end_time = perf_counter()
    print(f'It took {end_time- start_time :0.2f} second(s) to complete.')

print("==============Example 2: multi-threaded==============")

from threading import Thread
from time import perf_counter


def replace(filename, substr, new_substr):
    print(f'Processing the file {filename}')
    # get the contents of the file
    with open(filename, 'r') as f:
        content = f.read()

    # replace the substr by new_substr
    content = content.replace(substr, new_substr)

    # write data into the file
    with open(filename, 'w') as f:
        f.write(content)
        f.write("Example 2: multi-threaded\n")


def main2():
    filenames = [
        '../testdata/test1.txt',
        '../testdata/test2.txt',
        '../testdata/test3.txt',
        '../testdata/test4.txt',
        '../testdata/test5.txt',
        '../testdata/test6.txt',
        '../testdata/test7.txt',
        '../testdata/test8.txt',
        '../testdata/test9.txt',
        '../testdata/test10.txt',
    ]

    # create threads
    threads = [Thread(target=replace, args=(filename, 'id', 'ids'))
               for filename in filenames]

    # start the threads
    for thread in threads:
        thread.start()

    # wait for the threads to complete
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    start_time = perf_counter()

    main2()

    end_time = perf_counter()
    print(f'It took {end_time- start_time :0.10f} second(s) to complete.')

