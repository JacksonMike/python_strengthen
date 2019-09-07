import time


"""若a+b+c=1200,a^2+b^2=c^2,a,b,c都是正整数,求a,b,c的值
枚举法
独立存在解决问题的思路和方法
"""
start = time.time()
for a in range(0, 1001):
    for b in range(0, 1001):
        c = 1000 - a - b
        if a + b + c == 1000 and a**2 + b**2 == c**2 and a*b*c != 0:
            print("a=%d,b=%d,c=%d" % (a, b, c))
end = time.time()
print("finish time=%d" % (end - start))
