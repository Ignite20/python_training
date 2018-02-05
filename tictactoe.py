import os

board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


boardIsFilled = False
isXTurn = True
winner = ""
game_modes = {
    1: "Player vs Computer",
    2: "Player vs Player"
}


def print_board(b):
    for line in b:
        print(line)
    print("\n\n")


def check_winner(player_board, player):
    player_won = False
    #Check rows
    if player_board[0][0] == player and player_board[0][1] == player and player_board[0][2] == player:
        player_won = True
    elif player_board[1][0] == player and player_board[1][1] == player and player_board[1][2] == player:
        player_won = True
    elif player_board[2][0] == player and player_board[2][1] == player and player_board[2][2] == player:
        player_won = True

    #Check columns
    elif player_board[0][0] == player and player_board[1][0] == player and player_board[2][0] == player:
        player_won = True
    elif player_board[0][1] == player and player_board[1][1] == player and player_board[2][1] == player:
        player_won = True
    elif player_board[0][2] == player and player_board[1][2] == player and player_board[2][2] == player:
        player_won = True

    #Check diagonals
    elif player_board[0][0] == player and player_board[1][1] == player and player_board[2][2] == player:
        player_won = True
    elif player_board[2][0] == player and player_board[1][1] == player and player_board[0][2] == player:
        player_won = True


    return player_won


def check_for_draw(mboard):
    draw = True
    count = 0
    for row in mboard:
        for col in row:
            if col == " ":
                count += 1

    if count > 0:
        draw = False
    return draw


print(game_modes)
game_mode = int(input("Select game mode: "))

if game_mode == 2:
    while not boardIsFilled:
        print("Player 1") if isXTurn else print("Player 2")

        keyX = input("insert X coordinate: ")

        keyY = input("insert Y coordinate: ")

        if len(keyX) == 1 and len(keyY) == 1 and ord("0") <= ord(keyX) <= ord("2") and ord("0") <= ord(keyY) <= ord("2"):
            if int(keyX) < 3 and int(keyY) < 3 and keyX is not None and keyY is not None and board[int(keyY)][int(keyY)] == " ":
                board[int(keyX)][int(keyY)] = "X" if isXTurn else "Y"
                if isXTurn:
                    isXTurn = False
                else:
                    isXTurn = True
            else:
                print("invalid coordinate")

            if check_winner(board, "X"):
                winner = "X"
                boardIsFilled = True
            elif check_winner(board, "Y"):
                winner = "Y"
                boardIsFilled = True
            elif check_for_draw(board):
                winner = "Draw"
                boardIsFilled = True

        print_board(board)
    print("Winner is %s" % winner) if winner != "Draw" else print("Game is %s" % winner)

