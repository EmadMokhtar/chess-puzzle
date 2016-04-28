import unittest

from core.models import ChessBoard, King, Queen, Rook, Bishop, Knight


class ChessBoardTestCases(unittest.TestCase):

    def test_initialize_3_by_3_chess_board(self):
        new_board = ChessBoard(3, 3)
        expected_board = '\n'.join(['|'.join(['X' for _ in range(3)]) for _ in range(3)])
        self.assertEqual(expected_board, repr(new_board))

    def test_initialize_7_by_7_chess_board(self):
        new_board = ChessBoard(7, 7)
        expected_board = '\n'.join(['|'.join(['X' for _ in range(7)]) for _ in range(7)])
        self.assertEqual(expected_board, repr(new_board))

    def test_initialize_3_by_7_chess_board(self):
        new_board = ChessBoard(3, 7)
        expected_board = '\n'.join(['|'.join(['X' for _ in range(3)]) for _ in range(7)])
        self.assertEqual(expected_board, repr(new_board))

    def test_initialize_empty_chess_board(self):
        new_board = ChessBoard(0, 0)
        expected_board = ''''''
        self.assertEqual(expected_board, repr(new_board))

    def test_place_king_on_board_and_move_it(self):
        new_board = ChessBoard(3, 3)
        king = King(new_board, 0, 0)
        self.assertEqual(King.symbol, new_board[0, 0])
        self.assertEqual('X:0, Y:0', king.position)
        king.move_to(0, 2)
        self.assertEqual(King.symbol, new_board[0, 2])
        self.assertNotEqual(King.symbol, new_board[0, 0])
        self.assertEqual('X:0, Y:2', king.position)

    def test_place_rook_on_board_and_move_it(self):
        new_board = ChessBoard(3, 3)
        rook = Rook(new_board, 0, 0)
        self.assertEqual(Rook.symbol, new_board[0, 0])
        self.assertEqual('X:0, Y:0', rook.position)
        rook.move_to(0, 2)
        self.assertEqual(Rook.symbol, new_board[0, 2])
        self.assertNotEqual(Rook.symbol, new_board[0, 0])
        self.assertEqual('X:0, Y:2', rook.position)

    def test_place_queen_on_board_and_move_it(self):
        new_board = ChessBoard(3, 3)
        queen = Queen(new_board, 0, 0)
        self.assertEqual(Queen.symbol, new_board[0, 0])
        self.assertEqual('X:0, Y:0', queen.position)
        queen.move_to(0, 2)
        self.assertEqual(Queen.symbol, new_board[0, 2])
        self.assertNotEqual(Queen.symbol, new_board[0, 0])
        self.assertEqual('X:0, Y:2', queen.position)

    def test_place_bishop_on_board_and_move_it(self):
        new_board = ChessBoard(3, 3)
        bishop = Bishop(new_board, 0, 0)
        self.assertEqual(Bishop.symbol, new_board[0, 0])
        self.assertEqual('X:0, Y:0', bishop.position)
        bishop.move_to(0, 2)
        self.assertEqual(Bishop.symbol, new_board[0, 2])
        self.assertNotEqual(Bishop.symbol, new_board[0, 0])
        self.assertEqual('X:0, Y:2', bishop.position)

    def test_place_knight_on_board_and_move_it(self):
        new_board = ChessBoard(3, 3)
        knight = Knight(new_board, 0, 0)
        self.assertEqual(Knight.symbol, new_board[0, 0])
        self.assertEqual('X:0, Y:0', knight.position)
        knight.move_to(0, 2)
        self.assertEqual(Knight.symbol, new_board[0, 2])
        self.assertNotEqual(Knight.symbol, new_board[0, 0])
        self.assertEqual('X:0, Y:2', knight.position)


if __name__ == '__main__':
    unittest.main()
