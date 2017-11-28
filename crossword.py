def get_wrds(grid, d):
    found_words = set()
    visited = set()
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            visit_point = row + len(grid)*col
            if visit_point not in visited:
                visited.add(visit_point)
                dfs(grid, d, grid[row][col], row, col, found_words, visited)
                visited.remove(visit_point)
    return found_words

def dfs(grid, d, cur_word, row, col, found_words, visited):
    if cur_word in d:
        found_words.add(cur_word)
    for move in get_valid_moves(row, col, len(grid), len(grid[0])):
        #print("cur word {0} move {1}".format(cur_word, move))
        new_row = move[0]
        new_col = move[1]
        visit_point = new_row + len(grid)*new_col
        if visit_point not in visited:
            visited.add(visit_point)
            new_cur_word = cur_word+grid[new_row][new_col]
            dfs(grid, d, new_cur_word, new_row, new_col, found_words, visited)
            visited.remove(visit_point)


def get_valid_moves(row, col, rowsz, colsz):
    dir_offs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    all_moves = map(lambda off: [off[0] + row, off[1] + col], dir_offs)
    all_moves = filter(lambda move: move[0] > -1 and move[0] < rowsz and move[1] > -1 and move[1] < colsz , all_moves)
    return all_moves

grid = [["C", "A", "T"],
        ["O", "S", "K"],
        ["P", "Y", "U"]]
d = set(["CAT", "COPY", "ASK", "CATK", "SOS", "CAST", "SOPYUKTAC"])
from trie import PTrie
pt = PTrie()
for w in d:
    pt.add(w)
print(get_wrds(grid, d))
