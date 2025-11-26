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
    # Manhattan + 2*conflicts
    man = h_manhattan(state, goal)
    conflicts = 0

    # Rows
    for row in range(3):
        row_tiles = [state[row*3 + col] for col in range(3)]
        goal_row = {goal[i]: i % 3 for i in range(9)}
        for i in range(3):
            for j in range(i+1, 3):
                t1, t2 = row_tiles[i], row_tiles[j]
                if t1 != 0 and t2 != 0:
                    if goal_row[t1] > goal_row[t2]:
                        conflicts += 1

    # Columns
    for col in range(3):
        col_tiles = [state[row*3 + col] for row in range(3)]
        goal_col = {goal[i]: i // 3 for i in range(9)}
        for i in range(3):
            for j in range(i+1, 3):
                t1, t2 = col_tiles[i], col_tiles[j]
                if t1 != 0 and t2 != 0:
                    if goal_col[t1] > goal_col[t2]:
                        conflicts += 1

    return man + 2 * conflicts
