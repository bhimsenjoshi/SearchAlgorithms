# TBD .


map1 = {('s', 'f'): 99,
        ('f', 'b'): 211,
        ('s', 'r'): 80,
        ('r', 'p'): 97,
        ('p', 'b'): 101
        }

adjlst = {'s': ['f', 'r'],
          'f': ['b'],
          'r': ['p'],
          'p': ['b'],
          'b': []
          }


def UCS(s, e):
    frontier = [(0, s, '')]
    explored = []
    while len(frontier) > 0:
        frontier.sort()
        current = frontier.pop(0)
        explored.append(current)
        if current[1] == e:
            print("Goal Reached {}".format(current))
        for neighbour in adjlst[current[1]]:
            cost = map1[(current[1], neighbour)] + current[0]
            frontier.append((cost, neighbour, current[2]+current[1]))
        #print(frontier)
    return


UCS('s', 'b')
