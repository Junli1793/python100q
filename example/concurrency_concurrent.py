#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
concurrent.futures — Launching parallel tasks
https://docs.python.org/3/library/concurrent.futures.html

The concurrent.futures module provides a high-level interface for asynchronously executing callables.

The asynchronous execution can be performed with threads, using ThreadPoolExecutor, or separate processes, using ProcessPoolExecutor.
Both implement the same interface, which is defined by the abstract Executor class.

concurrent.futures.ThreadPoolExecutor offers a higher level interface to push tasks to a background thread without blocking execution of the calling thread,
while still being able to retrieve their results when needed.

"""
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor

print()
print("==============Example 1: ThreadPoolExecutor==============")

with ThreadPoolExecutor(max_workers=10) as executor:
    future = executor.submit(pow, 323, 1235)
    print(future.result())

concurrent.futures.as_completed(future)

print()
print("==============Example 2: ThreadPoolExecutor==============")

import shutil
with ThreadPoolExecutor(max_workers=4) as e:
    e.submit(shutil.copy, 'src1.txt', 'dest1.txt')
    e.submit(shutil.copy, 'src2.txt', 'dest2.txt')
    e.submit(shutil.copy, 'src3.txt', 'dest3.txt')
    e.submit(shutil.copy, 'src4.txt', 'dest4.txt')

print()
print("==============Example 3: ThreadPoolExecutor==============")

import concurrent.futures
import urllib.request

URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://some-made-up-domain.com/']

# Retrieve a single page and report the URL and contents
def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()

# We can use a with statement to ensure threads are cleaned up promptly
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # Start the load operations and mark each future with its URL
    future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
    print(future_to_url)
    # for future in concurrent.futures.as_completed(future_to_url.keys()):
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
        else:
            print('%r page is %d bytes' % (url, len(data)))

print()
print("==============Example 4: ProcessPoolExecutor==============")

import concurrent.futures
import math

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))

if __name__ == '__main__':
    main()
