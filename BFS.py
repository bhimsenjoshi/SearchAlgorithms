def bfs(g, s, d):
    if s == d:
        print("Destination Reached")
        return

    frontier = [(s, 0)]
    explored = []
    path = {s: s}

    while len(frontier) > 0:
        node = frontier.pop(0)
        explored.append(node)
        print("Current {} required {}".format(node, d))
        for neighbour in g[node[0]]:
            # Check if this already explored
            if (neighbour, node[1]) not in explored or frontier:
                if neighbour == d:
                    print("Destination Reached, cost = {}, Path is {}".format((node[1]+1), path[node[0]]))
                    return
                # else append the frontier
                frontier.append((neighbour, (node[1]+1)))
                path[neighbour] = path[node[0]] + neighbour
            # If already explored then skip


g1 = {'a': ['b', 'c'],
      'b': ['d'],
      'c': [],
      'd': ['e', 'f'],
      'e': [],
      'f': []
      }

bfs(g1, 'a', 'e')
