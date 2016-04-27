import unittest

from core.models import ChessBoard


class ChessBoardTestCases(unittest.TestCase):

    def test_initialize_3_by_3_chess_board(self):
        new_board = ChessBoard(3, 3)
        expected_board = '\n'.join(['|'.join(['x' for _ in range(3)]) for _ in range(3)])
        self.assertEqual(expected_board, repr(new_board))

    def test_initialize_7_by_7_chess_board(self):
        new_board = ChessBoard(7, 7)
        expected_board = '\n'.join(['|'.join(['x' for _ in range(7)]) for _ in range(7)])
        self.assertEqual(expected_board, repr(new_board))

    def test_initialize_3_by_7_chess_board(self):
        new_board = ChessBoard(3, 7)
        expected_board = '\n'.join(['|'.join(['x' for _ in range(3)]) for _ in range(7)])
        self.assertEqual(expected_board, repr(new_board))

    def test_initialize_empty_chess_board(self):
        new_board = ChessBoard(0, 0)
        expected_board = ''''''
        self.assertEqual(expected_board, repr(new_board))


if __name__ == '__main__':
    unittest.main()
