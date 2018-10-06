# find maze
# maze = {
#         'a': ['e'],
#         'b': ['c', 'f'],
#         'c': ['b', 'd'],
#         'd': ['c'],
#         'e': ['a', 'i'],
#         'f': ['b', 'g', 'j'],
#         'g': ['f', 'h'],
#         'h': ['g', 'l'],
#         'i': ['e', 'm'],
#         'j': ['n', 'f', 'k'],
#         'k': ['j', 'o'],
#         'l': ['h', 'p'],
#         'm': ['i', 'n'],
#         'n': ['m', 'j'],
#         'o': ['k'],
#         'p': ['l']
#     }
def find_maze(maze, start, end):
    remain_queue = []
    added_pos_set = set()
    remain_queue.append(start)
    added_pos_set.add(start)
    while remain_queue:
        p = remain_queue.pop(0)
        v = p[-1]
        if v == end:
            return p
        for x in maze[v]:
            if x not in added_pos_set:
                remain_queue.append(p+' => '+x)
                added_pos_set.add(x)
    return "Not found ways"