class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowHash = defaultdict(int)
        #Check rows for dupes
        for row in board:
            for cell in row:
                rowHash[cell] = rowHash[cell] + 1
                if cell != "." and rowHash[cell] > 1: 
                    print("hey")
                    return False
            rowHash = defaultdict(int)
        # Check columns for dupes
        colHash = defaultdict(int)

        for i in range(9):
            for j in range(9):
                colHash[board[j][i]] = colHash[board[j][i]] + 1
                if board[j][i]!= "." and colHash[board[j][i]] > 1: 
                    # print("hey")
                    return False
            colHash = defaultdict(int)
        # chekc squares for dupes
        squareHash = defaultdict(int)
        for i in range(1,9,3):
            for j in range(1,9,3):
                squareHash[board[i-1][j-1]] = squareHash[board[i-1][j-1]] + 1
                # print("boo", board[i-1][j-1])
                squareHash[board[i-1][j]] = squareHash[board[i-1][j]] + 1
                squareHash[board[i-1][j+1]] = squareHash[board[i-1][j+1]] + 1
                squareHash[board[i][j-1]] = squareHash[board[i][j-1]] + 1
                squareHash[board[i][j]] = squareHash[board[i][j]] + 1
                squareHash[board[i][j+1]] = squareHash[board[i][j+1]] + 1
                squareHash[board[i+1][j]] = squareHash[board[i+1][j]] + 1
                squareHash[board[i+1][j-1]] = squareHash[board[i+1][j-1]] + 1
                squareHash[board[i+1][j+1]] = squareHash[board[i+1][j+1]] + 1
                # check for dupes
                for k in squareHash:
                    if k != "." and squareHash[k] > 1: 
                        # print(k, squareHash)
                        return False
                squareHash = defaultdict(int)
        return True
                
        