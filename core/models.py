
class ChessBoard:
    """
    Chess Board
    """

    def __init__(self, width, height):
        self.height = height
        self.width = width

        board = []
        for i in range(height):
            col = ['X' for _ in range(width)]
            board.append(col)

        self.board = board

    def __getitem__(self, position):
        row, col = position
        return self.board[row][col]

    def __setitem__(self, position, value):
        row, col = position
        self.board[row][col] = value

    def __repr__(self):
        return '\n'.join(['|'.join([col for col in row]) for row in self.board])


class AbstractChessPiece:
    """
    Abstract Chess Piece
    """
    symbol = 'X'
    board = None

    def __init__(self, board, row, col):
        self.board = board
        self.column = col
        self.row = row
        self.set_position(row, col)

    @property
    def position(self):
        return 'X:{0}, Y:{1}'.format(self.row, self.column)

    def set_position(self, row, col):
        """
        Set initial piece position
        :param row: board row index
        :param col: board column index
        """
        self.board[row, col] = self.symbol
        self.row = row
        self.column = col

    def move_to(self, row, col):
        """
        Move the price to chess board cell
        :param row: board row index
        :param col: board column index
        :return: new position
        """
        old_col = self.column
        old_row = self.row
        self.board[row, col] = self.symbol
        self.row = row
        self.column = col
        self.board[old_row, old_col] = 'X'
        return self.row, self.column


class Knight(AbstractChessPiece):
    """
    Knight Chess Piece
    """
    symbol = 'N'


class Queen(AbstractChessPiece):
    """
    Queen Chess Piece
    """
    symbol = 'Q'


class Bishop(AbstractChessPiece):
    """
    Bishop Chess Piece
    """
    symbol = 'B'


class Rook(AbstractChessPiece):
    """
    Rook Chess Piece
    """
    symbol = 'R'


class King(AbstractChessPiece):
    """
    King Chess Piece
    """
    symbol = 'K'
