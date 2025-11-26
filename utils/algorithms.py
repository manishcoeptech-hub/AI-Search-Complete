import heapq
from collections import deque
from utils.heuristics import h_misplaced, h_manhattan, linear_conflict

MOVES = {
    0: [1,3], 1: [0,2,4], 2: [1,5],
    3: [0,4,6], 4: [1,3,5,7], 5: [2,4,8],
    6: [3,7], 7: [4,6,8], 8: [5,7]
}

def reconstruct(came, current):
    path = [current]
    while tuple(current) in came:
        current = came[tuple(current)]
        if current is None:
            break
        path.append(current)
    path.reverse()
    return path

def bfs(start, goal):
    start_t = tuple(start)
    goal_t = tuple(goal)
    q = deque([start_t])
    came = {start_t: None}
    expanded = 0

    while q:
        current = q.popleft()
        expanded += 1

        if current == goal_t:
            return reconstruct(came, list(current)), expanded

        blank = current.index(0)
        for m in MOVES[blank]:
            nxt = list(current)
            nxt[blank], nxt[m] = nxt[m], nxt[blank]
            n_t = tuple(nxt)
            if n_t not in came:
                came[n_t] = list(current)
                q.append(n_t)

    return None, expanded

def dfs(start, goal, limit=20000):
    stack = [tuple(start)]
    came = {tuple(start): None}
    expanded = 0

    while stack:
        current = stack.pop()
        expanded += 1
        if expanded > limit:
            break

        if current == tuple(goal):
            return reconstruct(came, list(current)), expanded

        blank = current.index(0)
        for m in MOVES[blank]:
            nxt = list(current)
            nxt[blank], nxt[m] = nxt[m], nxt[blank]
            n_t = tuple(nxt)
            if n_t not in came:
                came[n_t] = list(current)
                stack.append(n_t)

    return None, expanded

def greedy_best_first(start, goal, heuristic="misplaced"):
    hfn = h_misplaced if heuristic=="misplaced" else h_manhattan

    start_t = tuple(start)
    goal_t = tuple(goal)

    open_list = []
    heapq.heappush(open_list, (0, start_t))
    came = {start_t: None}
    expanded = 0

    while open_list:
        _, current = heapq.heappop(open_list)
        expanded += 1

        if current == goal_t:
            return reconstruct(came, list(current)), expanded

        blank = current.index(0)
        for m in MOVES[blank]:
            nxt = list(current)
            nxt[blank], nxt[m] = nxt[m], nxt[blank]
            n_t = tuple(nxt)

            if n_t not in came:
                came[n_t] = list(current)
                h = hfn(nxt, goal)
                heapq.heappush(open_list, (h, n_t))

    return None, expanded
