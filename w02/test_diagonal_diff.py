import pytest
from diagonal_diff import diagonalDifference


class TestDiagonalDifference:
    def test_diagonal_diff(self):
        assert diagonalDifference([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 0
        assert diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]) == 15
        assert diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -2]]) == 5


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
