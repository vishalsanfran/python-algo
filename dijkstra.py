import sys
import pprint

class Move:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.dist = sys.maxint
    def __cmp__(self, other):
        if self.dist < other.dist:
            ret = -1
        elif self.dist > other.dist:
            ret = 1
        else:
            ret = 0
        return ret

    def __str__(self):
        return Move.to_str(self.row, self.col)

    @staticmethod
    def to_str(row, col):
        return "{0},{1}".format(row, col)

import heapq


class Dijkstra:
    def __init__(self, grid, st):
        self.grid = grid
        self.st = st
        self.prev = {}
        self.pos_to_move = self.get_pos_to_move()
        self.pq = self.pos_to_move.values()
        self.get_obj(st).dist = 0
        heapq.heapify(self.pq)
        self.visited = set()

    def run(self):
        while len(self.pq) > 0:
            src_obj = heapq.heappop(self.pq)
            src = [src_obj.row, src_obj.col]
            for move in self.get_moves(src):
                move_obj = self.get_obj(move)
                if src_obj.dist + 1 < move_obj.dist:
                    move_obj.dist = src_obj.dist + 1
                    heapq.heapify(self.pq)
                    self.prev[Move.to_str(move[0], move[1])] = Move.to_str(src[0], src[1])
                self.visited.add(Move.to_str(src[0], src[1]))

    def get_min_path(self, end):
        self.run()
        cur = Move.to_str(end[0], end[1])
        path = [cur]
        while cur in self.prev:
            cur = self.prev[cur]
            path.append(cur)
        return path

    def get_moves(self, orig):
        offs = [[0,1], [1,0], [0,-1], [-1,0]]
        moves = map(lambda off: [off[0] + orig[0], off[1] + orig[1]], offs)
        is_valid_row = lambda row: row > -1 and row < len(self.grid)
        is_valid_col = lambda col: col > -1 and col < len(self.grid[0])
        moves = filter(lambda move: is_valid_row(move[0]) and is_valid_col(move[1]), moves)
        moves = filter(lambda move: self.grid[move[0]][move[1]] != '*', moves)
        return filter(lambda move: Move.to_str(move[0], move[1]) not in self.visited, moves)

    def get_obj(self, move):
        return self.pos_to_move[Move.to_str(move[0], move[1])]

    def get_pos_to_move(self):
        moves = [ Move(row, col) for col in range(len(self.grid[0])) for row in range(len(self.grid)) ]
        return {format(move): move for move in moves }


grid = [
['_','s','_','_','_'],
['_','_','*','_','_'],
['_','*','e','_','_'],
['_','*','*','_','_'],
['_','_','_','_','_']
]
pprint.pprint(grid)
print Dijkstra(grid, [0,1]).get_min_path([2,2])
print Dijkstra(grid, [0,1]).get_min_path([4,2])
