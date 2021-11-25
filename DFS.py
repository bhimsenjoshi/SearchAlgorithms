def bfs(g, s):
    stack = [s]
    while len(stack) > 0:
        current = stack.pop()
        print(current)
        for neighbour in g[current]:
            stack.append(neighbour)


g1 = {'a': ['b', 'c'],
      'b': ['d'],
      'c': [],
      'd': ['e', 'f'],
      'e': [],
      'f': []
      }

bfs(g1, 'a')
