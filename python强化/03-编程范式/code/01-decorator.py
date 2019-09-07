import time


def timer(func):
    def inner(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        return end - start

    return inner


@timer
def test():
    s = 0
    for i in range(1000000):
        s += i


new_test = timer(test)
print(new_test())
print(test())
print("*" * 1000)


class LongTime(object):
    def __init__(self, a):
        self.a = a

    def __call__(self, func):
        def inner(*args, **kwargs):
            start = time.time()
            func(*args, **kwargs)
            end = time.time()
            if self.a == 1:
                return end - start
            else:
                return end + start

        return inner


@LongTime(9)
def test1():
    time.sleep(0.5)


print(test1())
