import pytest
from counting_valleys import countingValleys


class CountingValleysTest:
    def test_counting_valleys(self):
        assert countingValleys(8, "UDDDUDUU") == 1
        assert countingValleys(12, "DDUUDDUDUUUD") == 2


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
