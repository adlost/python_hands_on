def insert_letter(letter, pos):
    board[pos] = letter


def space_free(pos):
    return board[pos] == ' '


def print_board(brd):
    print('   |   |   ')
    print(' ' + brd[1] + ' | ' + brd[2] + ' | ' + brd[3])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + brd[4] + ' | ' + brd[5] + ' | ' + brd[6])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + brd[7] + ' | ' + brd[8] + ' | ' + brd[9])
    print('   |   |   ')


def check_board(brd):
    if brd.count(' ') > 1:
        return False
    else:
        return True


def winner(b, l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
            (b[4] == l and b[5] == l and b[6] == l) or
            (b[7] == l and b[8] == l and b[9] == l) or
            (b[1] == l and b[4] == l and b[7] == l) or
            (b[2] == l and b[5] == l and b[8] == l) or
            (b[3] == l and b[6] == l and b[9] == l) or
            (b[1] == l and b[5] == l and b[9] == l) or
            (b[3] == l and b[5] == l and b[7] == l))


def player_move():
    run = True
    while run:
        move = input("please select a position to enter the X between 1 to 9: ")
        try:
            move = int(move)
            if move in range(11):
                if space_free(move):
                    run = False
                    insert_letter('X', move)
                else:
                    print('Sorry, this space is occupied')
            else:
                print('please type a number between 1 and 9')
        except:
            print('Please type a number')


def computer_move():
    possibleMoves = [i for i, letter in enumerate(board) if letter == ' ' and i != 0]

    for let in ['O', 'X']:
        for i in possibleMoves:
            board_copy = board[:]
            board_copy[i] = let
            if winner(board_copy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = select_random(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = select_random(edgesOpen)
        return move


def select_random(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


def main():
    print("Welcome to the game!")
    print_board(board)

    while not (check_board(board)):
        if not (winner(board, 'O')):
            player_move()
            print_board(board)
        else:
            print("sorry you loose!")
            break

        if not (winner(board, 'X')):
            move = computer_move()
            if move == 0:
                print(" ")
            else:
                insert_letter('O', move)
                print('computer placed an o on position', move, ':')
                print_board(board)
        else:
            print("you win!")
            break

    if check_board(board):
        print("Tie game")


while True:
    x = input("Do you want to play again? (y/n) :")
    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print('--------------------')
        main()
    else:
        break
