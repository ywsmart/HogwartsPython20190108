import random
import time


def add(x, y):
    return x + y


def test_add():
    time.sleep(random.randint(2,6))
    assert add(1, 2) == 3


def test_add2():
    print("I am 2")
