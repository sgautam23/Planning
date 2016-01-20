grid = [[0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0]]

heuristic = [[9, 8, 7, 6, 5, 4],
             [8, 7, 6, 5, 4, 3],
             [7, 6, 5, 4, 3, 2],
             [6, 5, 4, 3, 2, 1],
             [5, 4, 3, 2, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right


def search(grid,init,goal,cost,heuristic):

    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[init[0]][init[1]] = 1

    x = init[0]
    y = init[1]
    g = 0

    open = [[g, x, y]]

    found = False  # flag that is set when search is complete
    resign = False # flag set if we can't find expand

    expand=[[-1 for row in range(len(grid[0]))] for col in range(len(grid))]  #To track nodes that we expand
    count=1

    min=1000
    #prev=init

    while not found and not resign:
        if len(open) == 0:
            resign = True
            return 'fail'
        else:
            open.sort()
            open.reverse()
            for i in range(len(open)):
                curr=open[i][0]+ heuristic[open[i][1]][open[i][2]]
                if curr<min:
                    min=curr
                    idx=i

            next = open[idx]
            open.remove(next)

            x = next[1]
            y = next[2]
            g = next[0]

            expand[x][y] = count
            count += 1


            if x == goal[0] and y == goal[1]:
                found = True
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    #expand the new node as long as
                    #It is not an obstacle, lies within the grid,
                    #Has not already been expanded
                    if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and closed[x2][y2] == 0 and \
                                    grid[x2][y2] == 0:
                        g2 = g + cost
                        open.append([g2, x2, y2])
                        closed[x2][y2] = 1

    return expand

expand=search(grid,init,goal,cost,heuristic)

for i in expand:
    print(i)
    print "\n"
