import heapq

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

moves = {
    0: [1, 3], 1: [0, 2, 4], 2: [1, 5],
    3: [0, 4, 6], 4: [1, 3, 5, 7], 5: [2, 4, 8],
    6: [3, 7], 7: [4, 6, 8], 8: [5, 7]
}

def heuristic(state):
    distance = 0
    for index, tile in enumerate(state):
        if tile == 0:
            continue
        goal_index = goal.index(tile)
        row1, col1 = divmod(index, 3)
        row2, col2 = divmod(goal_index, 3)
        distance += abs(row1 - row2) + abs(col1 - col2)
    return distance

def solve(start):
    counter = 0
    queue = [(heuristic(start), counter, start, [])]
    visited = set([start])

    while queue:
        h, _, state, path = heapq.heappop(queue)

        if state == goal:
            return path + [state]

        zero = state.index(0)

        for move in moves[zero]:
            new_state = list(state)
            new_state[zero], new_state[move] = new_state[move], new_state[zero]
            new_state = tuple(new_state)

            if new_state not in visited:
                visited.add(new_state)
                counter += 1
                heapq.heappush(
                    queue,
                    (heuristic(new_state), counter, new_state, path + [state])
                )

    return None

start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

solution = solve(start)

if solution:
    print("Solution found in", len(solution) - 1, "moves:\n")
    for step in solution:
        print(step[0:3])
        print(step[3:6])
        print(step[6:9])
        print("Heuristic value =", heuristic(step))
        print()
else:
    print("No solution found")
