def validate_sudoku(board):
    elements=set(range(1,10))
    for b in board:
        if set(b)!=elements:
            return False
    for b in zip(*board):
        if set(b)!=elements:
            return False
    for i in range(0,7,3):
        for j in range(0,7,3):
            if elements!={(board[w][q]) for q in range(j,j+3) for w in range(i,i+3)}:
                return False
    return True