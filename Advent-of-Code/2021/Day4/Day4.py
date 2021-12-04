with open("day4.txt", "r") as f:
    bingonumbers = list(f.readline().split(","))
    boards = f.readlines()[1:]

#with open("test.txt", "r") as f:
#    bingonumbers = list(f.readline().split(","))
#    boards = f.readlines()[1:]

TASK = 2

def isWinning(board):
    columncount = 0
    rowcount = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "":
                rowcount += 1
            if board[j][i] == "":
                columncount += 1
        if rowcount == 5 or columncount == 5:
            return True
        rowcount = 0
        columncount = 0
    return False

def checkBingo(board, number):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == number:
                board[i][j] = ""
    return board

def calculateBoard(board):
    sum = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != "":
                sum += int(board[i][j])
    return sum
   
board = []
refinedBoard = []
#test = [['83', '11', '47', '61', '45'], ['30', '74', '73', '14', '66'], ['53', '52', '10', '57', '15'], ['64', '50', '54', '28', '87'], ['26', '85', '63', '25', '86']]
#testnumbers = ['83', '11', '47', '61', '45']

#Filter out the empty strings and made each row in a list
for row in boards:
    t = row.strip()
    board.append(t.split(" "))
    for r in board:
        for item in r:
            if item == '':
                r.remove(item)

#Divide into boards [[]]
currentBoard = []

while len(board) > 0:
    for i in range(0, 5):
        currentBoard.append(board[0])
        board.remove(board[0])    
    if len(board) > 0:
        board.remove(board[0])
    refinedBoard.append(currentBoard)
    currentBoard = []

if TASK == 1:
    won = False
    for number in bingonumbers:
        for b in refinedBoard:
            checkedB = checkBingo(b, number)
            if isWinning(checkedB):
                winningNumber = int(number)
                sum = calculateBoard(checkedB)
                print(winningNumber * sum)
                won = True
            if won:
                break
        if won:
            break

if TASK == 2:
    winningBoards = []
    for number in bingonumbers:
        for idx, b in enumerate(refinedBoard):
            if b != "":
                checkedB = checkBingo(b, number)
                if isWinning(checkedB):
                    winningNumber = int(number)
                    sum = calculateBoard(checkedB)
                    winningBoards.append((winningNumber * sum))
                    #Deleting first item in for loop makes it "ignore it", set to "" instead
                    refinedBoard[idx] = ""
      
    print(winningBoards[-1])

        



    

