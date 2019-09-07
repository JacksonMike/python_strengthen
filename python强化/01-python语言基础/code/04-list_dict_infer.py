a = [1, 2, 3]
b = ["x", "y", "z"]
d = {k: v for k, v in zip(a, b)}
print(d)

l1 = [i for i in range(10)]
print(l1)

# 生成器
l2 = (i for i in range(10))
for i in l2:
    print(i)
