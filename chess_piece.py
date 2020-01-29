class ChessGame(object):
    def __init__(self):
        self.board = ["test"]
        # White moves first
        self.current_move = 0

    def move_piece(self, starting_position, ending_position):
        # Check if inside board
        if not valid_square(location[0]) or not valid_square(location[1]):
            raise Execption("Invalid square")
        # Check if not in check or relieving the check threat


    def valid_square(self, coordinate):
        return coordinate >= 0 and coordinate <= 7

    def generate_moves(self):
        pass

    def in_check(self):
        # Exhaust the possible checks
        # Iterate over board to check for attacked squares and see if that
        # list has the king's posistion in it
        pass




class ChessPiece(object):
    def __init__(self, color, current_position, board):
        self.color = color
        self.type = ("", "")
        self.current_position = current_position
        self.board = board.board

    # Returns bool if piece can move to location.
    def move(self, location):
        pass

    # Returns list of coordinates that are attacked by the piece.
    def attacked_squares(self):
        pass

    def same_pieces(self, attacked_squares_list):
        return list(filter(lambda x: (x.color != self.color or x.type[0] == ""), attacked_squares_list))

    def valid_square(self, coordinate):
        return (coordinate[0] >= 0 and coordinate[0] <= 7) and (coordinate[1] >= 0 and coordinate[1] <= 7)



class Pawn(ChessPiece):
    def __init__(self, color, current_position, board):
        ChessPiece.__init__(self, color, current_position, board)
        # super.__init__(color, current_position, board)
        self.type = ("Pawn", "")
    def move(self, location):
        # Check if going backwards
        # if location[0] != self.current
        pass
    def attacked_squares(self):
        # Pawn attacks (n+1, n+1) and (n-1, n+1)
        attacked_squares_list = []
        # Check if on left edge of board.
        if self.current_position[0] != 0:
            attacked_squares_list.append((self.current_position[0] - 1,
            self.current_position[1] + 1))
        # Check if on right edge of board
        if self.current_position[1] != 7:
            attacked_squares_list.append((self.current_position[0] + 1,
            self.current_position[1] + 1))
        return attacked_squares_list


class Rook(ChessPiece):
    def __init__(self, color, current_position, board):
        ChessPiece.__init__(self, color, current_position, board)
        self.type = ("Rook", "R")

    def move(self, location):
        pass

    def attacked_squares(self):
        # Rook attacks virtical and horizontal line extended.
        # Stops when piece is in the way
        attacked_squares_list = []
        # Board is 8x8
        # Check above rook
        for x in range(self.current_position[0] + 1, 8):
            attacked_squares_list.append((x, self.current_position[1]))
            if self.board[x][self.current_position[1]].type[0] != "":
                break
        # Check below Rook
        for x in reversed(range(self.current_position[0])):
            attacked_squares_list.append((x, self.current_position[1]))
            if self.board[x][self.current_position[1]].type[0] != "":
                break
        # Check to right of rook
        for y in range(self.current_position[1] + 1, 8):
            attacked_squares_list.append((self.current_position[0], y))
            if self.board[self.current_position[0]][y].type[0] != "":
                break
        # Check to left of Rook
        for y in reversed(range(self.current_position[1])):
            attacked_squares_list.append((self.current_position[0], y))
            if self.board[self.current_position[0]][y].type[0] != "":
                break
        return attacked_squares_list


class Bishop(ChessPiece):
    def __init__(self, color, current_position, board):
        ChessPiece.__init__(self, color, current_position, board)
        self.type = ("Bishop", "B")

    def attacked_squares(self):
        # Check right upper diagonal
        attacked_squares_list = []
        current_square = [self.current_position[0] + 1, self.current_position[1] + 1]
        for x in range(8):
            if not self.valid_square(current_square):
                continue
            attacked_squares_list.append(tuple(current_square))
            if self.board[current_square[0]][current_square[1]].type[0] != "":
                break
            current_square = [current_square[0] + 1, current_square[1] + 1]
        # Check right lower diagonal
        current_square = [self.current_position[0] + 1, self.current_position[1] - 1]
        for x in range(8):
            if not self.valid_square(current_square):
                continue
            attacked_squares_list.append(tuple(current_square))
            if self.board[current_square[0]][current_square[1]].type[0] != "":
                break
            current_square = [current_square[0] + 1, current_square[1] - 1]

        # Check left upper diagonal
        current_square = [self.current_position[0] - 1, self.current_position[1] + 1]
        for x in range(8):
            if not self.valid_square(current_square):
                continue
            attacked_squares_list.append(tuple(current_square))
            if self.board[current_square[0]][current_square[1]].type[0] != "":
                break
            current_square = [current_square[0] - 1, current_square[1] + 1]

        # Check left lower diagonal
        current_square = [self.current_position[0] - 1, self.current_position[1] - 1]
        for x in range(8):
            if not self.valid_square(current_square):
                continue
            attacked_squares_list.append(tuple(current_square))
            if self.board[current_square[0]][current_square[1]].type[0] != "":
                break
            current_square = [current_square[0] - 1, current_square[1] - 1]
        return attacked_squares_list

    def move(self, location):
        pass

class King(ChessPiece):
    def __init__(self, color, current_position, board):
        ChessPiece.__init__(self, color, current_position, board)
        self.type = ("King", "K")

    def attacked_squares(self):
        # Exhaust all possibilities
        attacked_squares_list = [
        (self.current_position[0] + 1, self.current_position[1]),
        (self.current_position[0], self.current_position[1] + 1),
        (self.current_position[0] + 1, self.current_position[1] + 1),
        (self.current_position[0] - 1, self.current_position[1]),
        (self.current_position[0] - 1, self.current_position[1] - 1),
        (self.current_position[0] - 1, self.current_position[1] + 1),
        (self.current_position[0] + 1, self.current_position[1] - 1),
        (self.current_position[0], self.current_position[1] + 1)
        ]

        return list(filter(self.valid_square, attacked_squares_list))

    def move(self, location):
        pass


class Queen(ChessPiece):
    def __init__(self, color, current_position, board):
        ChessPiece.__init__(self, color, current_position, board)
        self.type = ("Queen", "Q")

    def attacked_squares(self):
        # Check right upper diagonal
        attacked_squares_list = []
        current_square = [self.current_position[0] + 1, self.current_position[1] + 1]
        for x in range(8):
            if not self.valid_square(current_square):
                continue
            attacked_squares_list.append(tuple(current_square))
            if self.board[current_square[0]][current_square[1]].type[0] != "":
                break
            current_square = [current_square[0] + 1, current_square[1] + 1]
        # Check right lower diagonal
        current_square = [self.current_position[0] + 1, self.current_position[1] - 1]
        for x in range(8):
            if not self.valid_square(current_square):
                continue
            attacked_squares_list.append(tuple(current_square))
            if self.board[current_square[0]][current_square[1]].type[0] != "":
                break
            current_square = [current_square[0] + 1, current_square[1] - 1]

        # Check left upper diagonal
        current_square = [self.current_position[0] - 1, self.current_position[1] + 1]
        for x in range(8):
            if not self.valid_square(current_square):
                continue
            attacked_squares_list.append(tuple(current_square))
            if self.board[current_square[0]][current_square[1]].type[0] != "":
                break
            current_square = [current_square[0] - 1, current_square[1] + 1]

        # Check left lower diagonal
        current_square = [self.current_position[0] - 1, self.current_position[1] - 1]
        for x in range(8):
            if not self.valid_square(current_square):
                continue
            attacked_squares_list.append(tuple(current_square))
            if self.board[current_square[0]][current_square[1]].type[0] != "":
                break
            current_square = [current_square[0] - 1, current_square[1] - 1]

        # Check above rook
        for x in range(self.current_position[0] + 1, 8):
            attacked_squares_list.append((x, self.current_position[1]))
            if self.board[x][self.current_position[1]].type[0] != "":
                break
        # Check below Rook
        for x in reversed(range(self.current_position[0])):
            attacked_squares_list.append((x, self.current_position[1]))
            if self.board[x][self.current_position[1]].type[0] != "":
                break
        # Check to right of rook
        for y in range(self.current_position[1] + 1, 8):
            attacked_squares_list.append((self.current_position[0], y))
            if self.board[self.current_position[0]][y].type[0] != "":
                break
        # Check to left of Rook
        for y in reversed(range(self.current_position[1])):
            attacked_squares_list.append((self.current_position[0], y))
            if self.board[self.current_position[0]][y].type[0] != "":
                break
        return attacked_squares_list

    def move(self, location):
        pass


class Knight(ChessPiece):
    def __init__(self, color, current_position, board):
        ChessPiece.__init__(self, color, current_position, board)
        self.type = ("Knight", "K")

    def attacked_squares(self):
        # Manually exhaust all possibilities
        attacked_squares = [
        (self.current_position[0] - 2, self.current_position[1] + 1),
        (self.current_position[0] - 1, self.current_position[1] + 2),
        (self.current_position[0] + 1, self.current_position[1] + 2),
        (self.current_position[0] + 2, self.current_position[1] + 1),
        (self.current_position[0] + 1, self.current_position[1] - 2),
        (self.current_position[0] + 2, self.current_position[1] - 1),
        (self.current_position[0] - 2, self.current_position[1] - 1),
        (self.current_position[0] - 1, self.current_position[1] - 2)
        ]

        return list(filter(self.valid_square, attacked_squares))


    def move(self, location):
        pass

class EmptySquare(ChessPiece):
    def __init__(self, color, current_position, board):
        ChessPiece.__init__(self, color, current_position, board)
        self.type = ("", "")

new_chess_game = ChessGame()

a2 = Pawn(0, [0,1], new_chess_game)
b2 = Pawn(0, [0,1], new_chess_game)
c2 = Pawn(0, [0,1], new_chess_game)
d2 = Pawn(0, [0,1], new_chess_game)
e2 = Pawn(0, [0,1], new_chess_game)
f2 = Pawn(0, [0,1], new_chess_game)
g2 = Pawn(0, [0,1], new_chess_game)
h2 = Pawn(0, [0,1], new_chess_game)

a7 = Pawn(1, [0,6], new_chess_game)
b7 = Pawn(1, [0,6], new_chess_game)
c7 = Pawn(1, [0,6], new_chess_game)
d7 = Pawn(1, [0,6], new_chess_game)
e7 = Pawn(1, [0,6], new_chess_game)
f7 = Pawn(1, [0,6], new_chess_game)
g7 = Pawn(1, [0,6], new_chess_game)
h7 = Pawn(1, [0,6], new_chess_game)

Ra8 = Rook(1, [0,7], new_chess_game)
Nb8 = Knight(1, [1,7], new_chess_game)
Bc8 = Bishop(1, [2,7], new_chess_game)
Qd8 = Queen(1, [3,7], new_chess_game)
Ke8 = King(1, [4,7], new_chess_game)
Bf8 = Bishop(1, [5,7], new_chess_game)
Nb8 = Knight(1, [6,7], new_chess_game)
Ra8 = Rook(1, [7,7], new_chess_game)

Ra1 = Rook(0, [0,7], new_chess_game)
Nb1 = Knight(0, [1,7], new_chess_game)
Bc1 = Bishop(0, [2,7], new_chess_game)
Qd1 = Queen(0, [3,7], new_chess_game)
Ke1 = King(0, [4,7], new_chess_game)
Bf1 = Bishop(0, [5,7], new_chess_game)
Nb1 = Knight(0, [6,7], new_chess_game)
Ra1 = Rook(0, [7,7], new_chess_game)


new_chess_game.board = [
    [Ra8, Nb8, Bc8, Qd8, Ke8, Bf8, Nb8, Ra8],
    [a7, b7, c7, d7, e7, f7, g7, h7],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [a2, b2, c2, d2, e2, f2, g2, h2],
    [Ra1, Nb1, Bc1, Qd1, Ke1, Bf1, Nb1, Ra1]]

# Rook attack squares test
# rook_test = ChessGame()
# empty_space = EmptySquare(0,[0,0], rook_test)
# lone_rook = Rook(0, [0,0], rook_test)
# rook_test.board = [
#     [lone_rook, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space],
#     [empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space],
#     [empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space],
#     [empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space],
#     [empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space],
#     [empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space],
#     [empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space],
#     [empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space]
# ]
#
# lone_rook.board = rook_test.board
#
# lone_rook.attacked_squares()

# Bishop attacked squares test
# rook_test = ChessGame()
# empty_space = EmptySquare(0,[0,0], rook_test)
# lone_bishop = Bishop(0, [3,3], rook_test)
# rook_test.board = [
#     [empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space],
#     [empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space],
#     [empty_space, empty_space, lone_bishop, empty_space, lone_bishop, empty_space, empty_space, empty_space],
#     [empty_space, empty_space, empty_space, lone_bishop, empty_space, empty_space, empty_space, empty_space],
#     [empty_space, empty_space, lone_bishop, empty_space, lone_bishop, empty_space, empty_space, empty_space],
#     [empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space],
#     [empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space],
#     [empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space]
# ]
#
# lone_bishop.board = rook_test.board
#
# lone_bishop.attacked_squares()
# Queen Test
# rook_test = ChessGame()
# empty_space = EmptySquare(0,[0,0], rook_test)
# lone_queen = Queen(0, [3,3], rook_test)
# rook_test.board = [
#     [empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space],
#     [empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space],
#     [empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space],
#     [empty_space, empty_space, empty_space, lone_queen, empty_space, empty_space, empty_space, empty_space],
#     [empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space],
#     [empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space],
#     [empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space],
#     [empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space]
# ]
#
# lone_queen.board = rook_test.board
#
# print(lone_queen.attacked_squares())

# Knight Test
# rook_test = ChessGame()
# empty_space = EmptySquare(0,[0,0], rook_test)
# lone_knight = Knight(0, [7,1], rook_test)
# rook_test.board = [
#     [empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space],
#     [empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space],
#     [empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space],
#     [empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space],
#     [empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space],
#     [empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space],
#     [empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space],
#     [empty_space, lone_knight, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space]
# ]
#
# lone_knight.board = rook_test.board
#
# print(lone_knight.attacked_squares())

# King Test
rook_test = ChessGame()
empty_space = EmptySquare(0,[0,0], rook_test)
lone_king = King(0, [7,0], rook_test)
rook_test.board = [
    [empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space],
    [empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space],
    [empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space],
    [empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space],
    [empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space],
    [empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space],
    [empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space],
    [lone_king, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space, empty_space]
]

lone_king.board = rook_test.board

print(lone_king.attacked_squares())
