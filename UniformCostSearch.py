# Uniform Cost Search.
# Undirected cyclic graph
# Bhimsen Joshi / Hyderabad / India
# 1st Dec 2021

# Cost of routes
map1 = {('s', 'f'): 99,
        ('f', 'b'): 211,
        ('s', 'r'): 80,
        ('r', 'p'): 97,
        ('p', 'b'): 101,
        ('f', 's'): 99,
        ('b', 'f'): 211,
        ('r', 's'): 80,
        ('p', 'r'): 97,
        ('b', 'p'): 101
        }

# Possible lists
# This can be generated as well
adjlst = {'s': ['f', 'r'],
          'f': ['b', 's'],
          'r': ['p', 's'],
          'p': ['b', 'r'],
          'b': ['f', 'p']
          }

# Function / Algorithm
# feed in the start and end location
# returns all possible path with cost
def UCS(s, e):
    frontier = [(0, s, '')]
    explored = []
    exploredNode = []
    result = []
    while len(frontier) > 0:

        #sort as per minimum cost
        frontier.sort()
        #popout the minimum cost node
        current = frontier.pop(0)
        explored.append(current)
        exploredNode.append(current[1])

        # Reached the goal
        if current[1] == e:
            result.append(current)

        # search all the neighbours
        for neighbour in adjlst[current[1]]:
            # ignore if already explored
            if neighbour in exploredNode:
                continue
            # compute the cost of reaching this node
            cost = map1[(current[1], neighbour)] + current[0]
            # add it to frontier as we need to explore
            frontier.append((cost, neighbour, current[2]+current[1]))

    # return all possible results
    return result


print(UCS('f', 'p'))
