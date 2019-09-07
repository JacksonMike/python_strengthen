class Person(object):
    def swim(self):
        print("像鱼一样游泳")


class Duck(object):
    def swim(self):
        print("鸭子特有的方式")


def in_pool(obj):
    obj.swim()


if __name__ == '__main__':
    p = Person()
    d = Duck()
    in_pool(p)
    in_pool(d)
    print(isinstance(p, Person))
    print(isinstance(d, Duck))
