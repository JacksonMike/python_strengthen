class CatToy(object):
    def speak(self):
        print("miao")


class DogToy(object):
    def speak(self):
        print("wang")


def factory_toy(toy_type):
    if toy_type == "dog":
        return DogToy()
    if toy_type == "cat":
        return CatToy()


dog = factory_toy("dog")
dog.speak()
