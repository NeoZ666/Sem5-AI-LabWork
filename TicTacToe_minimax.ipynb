player, opponent = 'x', 'o'

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def evaluate(board):
    for row in range(3):
        if (board[row][0] == board[row][1] and board[row][1] == board[row][2]):
            if (board[row][0] == player):
                return +10
            if (board[row][0] == opponent):
                return -10
    for col in range(3):
        if (board[0][col] == board[1][col] and board[1][col] == board[2][col]):
            if (board[0][col] == player):
                return +10
            if (board[0][col] == opponent):
                return -10
    if (board[0][0] == board[1][1] and board[1][1] == board[2][2]):
        if (board[0][0] == player):
            return +10
        if (board[0][0] == opponent):
            return -10
    if (board[0][2] == board[1][1] and board[1][1] == board[2][0]):
        if (board[0][2] == player):
            return +10
        if (board[0][2] == opponent):
            return -10
    return 0

def movesLeft(board):
    for i in range(3):
        for j in range(3):
            if (board[i][j] == '_'):
                return True
    return False

def minimax(board, depth, isMax):
    score = evaluate(board)
    if(score == +10):
        return score - depth
    
    if(score == -10):
        return score + depth
    
    if(movesLeft(board) == False):
        return 0
    
    if(isMax):
        best = -1000
        for i in range(3):
            for j in range(3):
                if(board[i][j] == '_'):
                    board[i][j] = player
                    best = max(best, minimax(board, depth+1, not isMax))
                    board[i][j] = '_'
        return best
    
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if(board[i][j] == '_'):
                    board[i][j] = opponent
                    best = min(best, minimax(board, depth+1, not isMax))
                    board[i][j] = '_'
        return best

def findBestMove(board):
    bestVal = -1000
    bestMove = (-1, -1)
    
    for i in range(3):
        for j in range(3):
            if (board[i][j] == '_'):
                board[i][j] = player
                moveVal = minimax(board, 0, False)
                board[i][j] = '_'
                
                if (moveVal > bestVal):
                    bestMove = (i, j)
                    bestVal = moveVal
    
    return bestMove

# Initialize the board
board = [['_', '_', '_'],
         ['_', '_', '_'],
         ['_', '_', '_']]

# Game loop
while True:
    print_board(board)
    player_row = int(input("Enter row (0, 1, or 2): "))
    player_col = int(input("Enter column (0, 1, or 2): "))
    
    if board[player_row][player_col] == '_':
        board[player_row][player_col] = player
    else:
        print("Invalid move. Try again.")
        continue
    
    if evaluate(board) == 10:
        print_board(board)
        print("Player wins!")
        break
    
    if not movesLeft(board):
        print_board(board)
        print("It's a draw!")
        break
    
    best_move = findBestMove(board)
    board[best_move[0]][best_move[1]] = opponent
    
    if evaluate(board) == -10:
        print_board(board)
        print("Opponent wins!")
        break
