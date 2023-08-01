def is_valid(x, y):
    return 0 <= x < 3 and 0 <= y < 3

def swap(board, x1, y1, x2, y2):
    board[x1][y1], board[x2][y2] = board[x2][y2], board[x1][y1]

def find_blank(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j

def is_goal_state(board, goal_state):
    return board == goal_state

def dfs(board, depth, max_depth, goal_state, visited):
    if depth > max_depth:
        return False

    if is_goal_state(board, goal_state):
        return True

    blank_x, blank_y = find_blank(board)

    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        new_x, new_y = blank_x + dx, blank_y + dy

        if is_valid(new_x, new_y):
            swap(board, blank_x, blank_y, new_x, new_y)
            board_hash = tuple(tuple(row) for row in board)

            if board_hash not in visited:
                visited.add(board_hash)
                if dfs(board, depth + 1, max_depth, goal_state, visited):
                    return True
                visited.remove(board_hash)

            swap(board, blank_x, blank_y, new_x, new_y)

    return False

def solve_8_puzzle(initial_state, goal_state):
    max_depth = 30  # Adjust the maximum depth as needed
    visited = set()
    initial_state_hash = tuple(tuple(row) for row in initial_state)
    visited.add(initial_state_hash)

    if is_goal_state(initial_state, goal_state):
        return initial_state

    for depth in range(1, max_depth + 1):
        if dfs(initial_state, 0, depth, goal_state, visited):
            return initial_state

    return None

if __name__ == "__main__":
    initial_state = [
        [2, 8, 3],
        [1, 6, 4],
        [7, 0, 5]
    ]

    goal_state = [
        [1, 2, 3],
        [8, 0, 4],
        [7, 6, 5]
    ]
    solution = solve_8_puzzle(initial_state, goal_state)

    if solution:
        print("Solution Found:")
        for row in solution:
            print(row)
    else:
        print("No solution found within the given depth limit.")
