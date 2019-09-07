class MyException(Exception):
    print("error")


a = 1
try:
    b = a / 0
except MyException as e:
    raise e
else:
    print(b)
finally:
    print("hello")
