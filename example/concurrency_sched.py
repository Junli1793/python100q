#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
sched — Event scheduler
https://docs.python.org/3/library/sched.html

The sched module defines a class which implements a general purpose event scheduler:
    class sched.scheduler(timefunc=time.monotonic, delayfunc=time.sleep)

    The scheduler class defines a generic interface to scheduling events.
    It needs two functions to actually deal with the “outside world” —
    1, timefunc should be callable without arguments, and return a number (the “time”, in any units whatsoever).
    2, The delayfunc function should be callable with one argument, compatible with the output of timefunc, and should delay that many time units.
    delayfunc will also be called with the argument 0 after each event is run to allow other threads an opportunity to run in multi-threaded applications.


Scheduler Objects

    scheduler instances have the following methods and attributes:

scheduler.enterabs(time, priority, action, argument=(), kwargs={})

    Schedule a new event. The time argument should be a numeric type compatible with the return value of the timefunc function passed to the constructor.
    Events scheduled for the same time will be executed in the order of their priority.
    A lower number represents a higher priority.
    Executing the event means executing action(*argument, **kwargs).
    argument is a sequence holding the positional arguments for action. kwargs is a dictionary holding the keyword arguments for action.

    Return value is an event which may be used for later cancellation of the event (see cancel()).

scheduler.enter(delay, priority, action, argument=(), kwargs={})

    Schedule an event for delay more time units. Other than the relative time, the other arguments, the effect and the return value are the same as those for enterabs().

scheduler.run(blocking=True)

    Run all scheduled events. This method will wait (using the delayfunc() function passed to the constructor) for the next event, then execute it and so on until there are no more scheduled events.
    If blocking is false executes the scheduled events due to expire soonest (if any) and then return the deadline of the next scheduled call in the scheduler (if any).
    Either action or delayfunc can raise an exception. In either case, the scheduler will maintain a consistent state and propagate the exception.
    If an exception is raised by action, the event will not be attempted in future calls to run().

    If a sequence of events takes longer to run than the time available before the next event, the scheduler will simply fall behind.
    No events will be dropped; the calling code is responsible for canceling events which are no longer pertinent.

"""
import sched
import time

print()
print("==============Example 1==============")

def some_function(arg1, arg2, arg3, arg4):
    print(time.time())
    print("some_function", arg1, arg2, arg3, arg4)

intervals = 15
# start at the beginning of next 5 minute
timestamp = time.time()
s = sched.scheduler(time.time, time.sleep)
s.enterabs((timestamp + 30 - timestamp % 30 + 1), 1, some_function, argument=("arg1", "arg2", intervals, 0))
s.run()
time.sleep(3)


print()
print("==============Example 2==============")
s = sched.scheduler(time.time, time.sleep)

def print_time(a='default'):
    print("From print_time", time.time(), a)

def print_some_times():
    print(time.time())
    s.enter(10, 1, print_time)
    s.enter(5, 2, print_time, argument=('positional',))
    s.enter(5, 1, print_time, kwargs={'a': 'keyword'})
    s.enter(2, 1, print_time, kwargs={'a': '2s'})
    s.run()
    print(time.time())


print_some_times()

