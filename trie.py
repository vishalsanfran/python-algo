class TNode:
    def __init__(self, char=None):
        self.char = char
        self.children = {}
        self.end = False

class PTrie:
    def __init__(self):
        self.root = TNode()

    def add(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TNode(c)
            cur = cur.children[c]
        cur.end = True


    def find(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.end

    def get_partial(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return []
            cur = cur.children[c]
        r = []
        self.dfs(cur, word, r)
        return r

    def dfs(self, cur, word, words):
        if cur.end:
            words.append(word)
        for c in cur.children:
            self.dfs(cur.children[c], word+c, words)


pt = PTrie()
il = ["cat", "cats", "mona", "moana", "mom"]
fl = ["cat", "cats", "mona", "moana", "mon"]
for w in il:
    pt.add(w)
for w in fl:
    print("w {0} r {1}".format(w, pt.find(w)))

print(pt.get_partial("mo"))
