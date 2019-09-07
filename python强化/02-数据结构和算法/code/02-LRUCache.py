import collections


class LRUCache(object):
    def __init__(self, cap=128):
        self.od = collections.OrderedDict()
        # 初始容量
        self.cap = cap

    def get(self, key):
        if key in self.od:
            val = self.od[key]
            # 移动到最左边
            self.od.move_to_end(key, last=False)
            return val
        else:
            return -1

    def put(self, key, value):
        if key in self.od:
            del self.od[key]
            # 移动到最右边
            self.od[key] = value
        else:
            self.od[key] = value
            if len(self.od) > self.cap:
                # 从最左边开始删除
                self.od.popitem(last=False)


lru = LRUCache()
lru.put("name", "Jim")
lru.put("age", 99)
print(lru.get("age"))
