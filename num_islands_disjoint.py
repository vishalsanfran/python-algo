from disjoint_set import DisjointSet

class Solution:
    def set_init(self, grid):
        self.grid = grid
        self.rowsz = len(grid)
        self.colsz = len(grid[0])
        self.ds = DisjointSet()

    def num_islands(self, grid):
        self.set_init(grid)
        rowsz = len(grid)
        colsz = len(grid[0])
        for row in range(self.rowsz):
            for col in range(self.colsz):
                for move in self.get_moves(row, col):
                    orig = self.get_move_str(row, col)
                    nbor = self.get_move_str(move[0], move[1])
                    self.ds.union(orig, nbor)
        import pdb
        pdb.set_trace()
        return len(self.ds.get_roots())

    def get_moves(self, row, col):
        offs = [[x,y] for y in range(-1,2) for x in range(-1,2) if x != 0 and y != 0]
        moves = map(lambda off: [off[0] + row, off[1] + col], offs)
        moves = filter(lambda move: self.can_move(move[0], move[1]), moves)
        moves = filter(lambda move: self.grid[move[0]][move[1]] != 0, moves)
        return moves

    def get_vals(self, moves):
        return [grid[move[0]][move[1]] for move in moves]

    def get_move_str(self, row, col):
        return "{0},{1}".format(row, col)

    def can_move(self, row, col):
        return row > -1 and col > -1 and row < self.rowsz and col < self.colsz

grid1 = [
    [1,1,0,0,0],
    [1,1,0,0,0],
    [0,0,1,0,0],
    [0,0,0,1,1]]

grid2 = [
    [1,1,0,0,0],
    [1,1,1,1,0],
    [0,0,0,1,0],
    [0,0,0,1,1]]


for grid in [grid2]:
    print Solution().num_islands(grid)
