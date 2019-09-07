import collections

Point = collections.namedtuple("Point", "x, y")
p = Point(1, 2)
print(p.x, p.y, p[0], p[1])

de = collections.deque()
de.appendleft(9)
de.append(1)
de.append(2)
de.append(3)
de.pop()
de.popleft()
print(de)

c = collections.Counter("hello")
print(c, type(c), c['l'])
print(c.most_common())

od = collections.OrderedDict()
od['name'] = "Jim"
od["age"] = 19
od['gender'] = "M"
print(od, od.keys())

dd = collections.defaultdict(int)
dd['b'] += 1
print(dd, dd['a'], dd['b'])
