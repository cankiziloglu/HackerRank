"""Tests for Flipping Bits Module"""

import pytest
from flipping_bits import flippingBits


class TestFlippingBits:
    def test_flipping_1(self):
        assert flippingBits(2147483647) == 2147483648

    def test_flipping_2(self):
        assert flippingBits(1) == 4294967294

    def test_flipping_3(self):
        assert flippingBits(0) == 4294967295

    def test_flipping_4(self):
        assert flippingBits(35601423) == 4259365872


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
