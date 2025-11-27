def h_misplaced(state, goal):
    return sum(1 for i in range(9) if state[i] != goal[i] and state[i] != 0)

def h_manhattan(state, goal):
    dist = 0
    for tile in range(1, 9):
        s = state.index(tile)
        g = goal.index(tile)
        dist += abs(s//3 - g//3) + abs(s%3 - g%3)
    return dist

def linear_conflict(state, goal):
    conflicts = 0
    man = h_manhattan(state, goal)

    # rows
    for row in range(3):
        row_tiles = state[row*3:(row+1)*3]
        for i in range(3):
            for j in range(i+1, 3):
                t1, t2 = row_tiles[i], row_tiles[j]
                if t1 and t2:
                    if goal.index(t1)//3 == row and goal.index(t2)//3 == row:
                        if goal.index(t1) > goal.index(t2):
                            conflicts += 1

    # columns
    for col in range(3):
        col_tiles = [state[col+r*3] for r in range(3)]
        for i in range(3):
            for j in range(i+1, 3):
                t1, t2 = col_tiles[i], col_tiles[j]
                if t1 and t2:
                    if goal.index(t1)%3 == col and goal.index(t2)%3 == col:
                        if goal.index(t1) > goal.index(t2):
                            conflicts += 1

    return man + 2 * conflicts
