def bfs(g, s):
    que = [s]
    while len(que) > 0:
        current = que.pop(0)
        print(current)
        for neighbour in g[current]:
            que.append(neighbour)


g1 = {'a': ['b', 'c'],
      'b': ['d'],
      'c': [],
      'd': ['e', 'f'],
      'e': [],
      'f': []
      }

bfs(g1, 'a')
