#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
multiprocessing is a package that supports spawning processes using an API similar to the threading module.
The multiprocessing package offers both local and remote concurrency, effectively side-stepping the Global Interpreter Lock by using subprocesses instead of threads.
Due to this, the multiprocessing module allows the programmer to fully leverage multiple processors on a given machine.
It runs on both Unix and Windows.

"""


print()
print("==============Example 1==============")

from multiprocessing import Pool, current_process, Manager


def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))

print()
print("==============Example 2==============")

from multiprocessing import Process
import os

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    info('function f')
    print('hello', name)

if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()

print()
print("==============Example 3: pump data==============")

manager = Manager()
# global shared_list
shared_list = manager.list()

def pump_data(index):
    # print(len(shared_list))

    apName = shared_list[index][0]
    apMAC = shared_list[index][1]
    print("$"*60)
    print(current_process().name.center(60, "$"))
    print("$"*60)
    print("\npumping data for AP: {} \n               Name: {} \n".format(apMAC, apName))
    print((str(index) + " done").center(60, "="))


ap_list = [('test_ap_01', 'AA:BB:CC:11:11:11'),
           ('test_ap_02', 'AA:BB:CC:22:22:22'),
           ('test_ap_03', 'AA:BB:CC:33:33:33'),
           ('test_ap_04', 'AA:BB:CC:44:44:44'),
           ('test_ap_05', 'AA:BB:CC:55:55:55'),
           ('test_ap_06', 'AA:BB:CC:66:66:66'),
           ('test_ap_07', 'AA:BB:CC:77:77:77'),
           ('test_ap_08', 'AA:BB:CC:88:88:88'),
           ('test_ap_11', '1A:BB:CC:11:11:11'),
           ('test_ap_12', '1A:BB:CC:22:22:22'),
           ('test_ap_13', '1A:BB:CC:33:33:33'),
           ('test_ap_14', '1A:BB:CC:44:44:44'),
           ('test_ap_15', '1A:BB:CC:55:55:55'),
           ('test_ap_16', '1A:BB:CC:66:66:66'),
           ('test_ap_17', '1A:BB:CC:77:77:77'),
           ('test_ap_18', '1A:BB:CC:88:88:88'),
           ('test_ap_21', '1A:BB:CC:11:11:11'),
           ('test_ap_22', '1A:BB:CC:22:22:22'),
           ('test_ap_23', '1A:BB:CC:33:33:33'),
           ('test_ap_24', '1A:BB:CC:44:44:44'),
           ('test_ap_25', '1A:BB:CC:55:55:55'),
           ('test_ap_26', '1A:BB:CC:66:66:66'),
           ('test_ap_27', '1A:BB:CC:77:77:77'),
           ('test_ap_28', '1A:BB:CC:88:88:88')
           ]

start_i = 0
end_i = len(ap_list)

shared_list = []
shared_list.extend(ap_list[start_i:end_i])
# print(shared_list)
total_ap = len(shared_list)

pool = Pool(processes=24)

index_list = [(i,) for i in range(total_ap)]

pool.starmap(pump_data, index_list)

pool.close()
pool.join()

print()
print("==============Example 3: Pool + Queue==============")

from multiprocessing import Manager, Pool

def f(q, n):
    q.put(n*n)

if __name__ == '__main__':
    with Manager() as manager:
        q = manager.Queue()
        with Pool(5) as p:
            for i in range(10):
                p.apply_async(f, (q, i))
            p.close()
            p.join()
            while not q.empty():
                print(q.get())
