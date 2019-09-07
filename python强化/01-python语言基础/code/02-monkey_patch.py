import time

print(time.time())


def _time():
    return "123"


time.time = _time
print(time.time())
