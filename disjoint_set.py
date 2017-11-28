class DisjointSet:
    def __init__(self):
        self.parents = {}
        self.ranks = {}
    def add(self, item):
        self.parents[item] = item
        self.ranks[item] = 0
    def find(self, item):
        parent = self.parents[item]
        if parent != item:
            parent = self.find(parent)
        return parent
    def union(self, a, b):
        for item in [a,b]:
            if item not in self.parents:
                self.add(item)
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb:
            return
        if self.ranks[pa] > self.ranks[pb]:
            self.parents[pb] = pa
        elif self.ranks[pb] > self.ranks[pa]:
            self.parents[pa] = pb
        else:
            self.parents[pb] = pa
            self.ranks[pa] += 1
    def get_roots(self):
        return set([val for key, val in self.parents.iteritems()])

if __name__ == "__main__":
    ds = DisjointSet()
    ds.union("123", "456")
    ds.union("mona", "vk")
    ds.union("vk", "xy")
    ds.union("456", "xy")
    for item in ["mona", "vk", "xy", "123", "456"]:
        print ds.find(item)
