"""Tests for merge_sorted_arrays module."""

import pytest
from merge_sorted_arrays import merge


class TestMergeSortedArrays:
    """Test cases for the merge function."""

    def test_basic_merge(self):
        """Test basic merge with equal sized arrays."""
        nums1 = [1, 2, 3, 0, 0, 0]
        nums2 = [2, 5, 6]
        merge(nums1, 3, nums2, 3)
        assert nums1 == [1, 2, 2, 3, 5, 6]

    def test_nums2_all_smaller(self):
        """Test when all nums2 elements are smaller than nums1."""
        nums1 = [4, 5, 6, 0, 0, 0]
        nums2 = [1, 2, 3]
        merge(nums1, 3, nums2, 3)
        assert nums1 == [1, 2, 3, 4, 5, 6]

    def test_nums2_all_larger(self):
        """Test when all nums2 elements are larger than nums1."""
        nums1 = [1, 2, 3, 0, 0, 0]
        nums2 = [4, 5, 6]
        merge(nums1, 3, nums2, 3)
        assert nums1 == [1, 2, 3, 4, 5, 6]

    def test_empty_nums1(self):
        """Test when nums1 has no actual elements (m=0)."""
        nums1 = [0, 0, 0]
        nums2 = [1, 2, 3]
        merge(nums1, 0, nums2, 3)
        assert nums1 == [1, 2, 3]

    def test_empty_nums2(self):
        """Test when nums2 is empty (n=0)."""
        nums1 = [1, 2, 3]
        nums2 = []
        merge(nums1, 3, nums2, 0)
        assert nums1 == [1, 2, 3]

    def test_both_empty(self):
        """Test when both arrays are empty."""
        nums1 = []
        nums2 = []
        merge(nums1, 0, nums2, 0)
        assert nums1 == []

    def test_single_elements(self):
        """Test with single element arrays."""
        nums1 = [2, 0]
        nums2 = [1]
        merge(nums1, 1, nums2, 1)
        assert nums1 == [1, 2]

    def test_duplicate_elements(self):
        """Test with duplicate elements across arrays."""
        nums1 = [1, 2, 2, 0, 0, 0]
        nums2 = [1, 2, 3]
        merge(nums1, 3, nums2, 3)
        assert nums1 == [1, 1, 2, 2, 2, 3]

    def test_negative_numbers(self):
        """Test with negative numbers."""
        nums1 = [-3, -1, 0, 0, 0]
        nums2 = [-2, 1, 2]
        merge(nums1, 2, nums2, 3)
        assert nums1 == [-3, -2, -1, 1, 2]

    def test_interleaved_elements(self):
        """Test when elements are interleaved."""
        nums1 = [1, 3, 5, 7, 0, 0, 0, 0]
        nums2 = [2, 4, 6, 8]
        merge(nums1, 4, nums2, 4)
        assert nums1 == [1, 2, 3, 4, 5, 6, 7, 8]

    def test_large_arrays(self):
        """Test with larger arrays."""
        m, n = 100, 100
        nums1 = list(range(0, 200, 2)) + [0] * n  # Even numbers 0-198
        nums2 = list(range(1, 200, 2))  # Odd numbers 1-199
        merge(nums1, m, nums2, n)
        assert nums1 == list(range(200))


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
