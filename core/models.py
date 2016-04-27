

class ChessBoard:
    """
    Chess Board
    """

    def __init__(self, width, height):
        self.height = height
        self.width = width

        board = []
        for i in range(height):
            col = ['x' for _ in range(width)]
            board.append(col)

        self.board = board

    def __repr__(self):
        return '\n'.join(['|'.join([col for col in row]) for row in self.board])
