def flist(l):
    l.append(0)
    print(id(l))
    print(l)


l = []
print(id(l))
flist(l)
print(id(l))
flist(l)
print(id(l))

print("*" * 100)


def fstr(s):
    s += 'a'
    print(id(s))
    print(s)


s = "hello"
print(id(s))
fstr(s)
print(id(s))
fstr(s)
print(id(s))
print("*" * 100)


def clear_list(l):
    l = []


ll = [1]
clear_list(ll)
print(ll)
print("*" * 100)


def lst(l=[1]):
    l.append(1)
    print(l)


lst()
lst()
