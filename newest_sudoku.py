
def solver(board):
    """
    This function solves a sudoku board using backtracking.
    parameter board: sudoku board 2d list of integers
    
    """
    if not empty_slot(board):
        return True
    
    else:
        row,column = empty_slot(board)

        for i in range(1,10):
            if(isvalid(board, i, (row,column))):
                board[row][column] = i
                
                """
                 Backtracking step. 
                 If it returns false it means that there are no valid positions so, that location has to set zero.
                 Function should search for different values.
                """  
                if(solver(board)):  
                    return True
                board[row][column] = 0
        
        return False


def empty_slot(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if(board[i][j]) == 0:
                return (i,j)     # return row column
    return None


def isvalid(board, num, position):

    # checking row
    for i in range(len(board[0])):
        if(board[position[0]][i] == num and position[1] != i):
            return False

    # checking column        
    for i in range(len(board)):
        if(board[i][position[1]] == num and position[0] != i):
            return False

    # checking boxes
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y*3, box_y*3 +3):
        for j in range(box_x*3, box_x*3 +3):
            if(board[i][j] == num and (i,j) != position):
                return False

    return True

def print_board(board):
    for i in range(len(board)):
        if(i % 3 == 0 and i != 0):
            print("-----------------------")

        for j in range(len(board[0])):
            if(j % 3 == 0 and j != 0):
                print(" | ", end = "")
            
            if (j == 8):
                print(board[i][j])            
            else:
                print(str(board[i][j]), end = " ")

