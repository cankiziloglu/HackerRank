"""
Merge two sorted arrays in-place.

Array1 has length (m+n) with first m elements sorted and remaining n elements as 0.
Array2 has length n with sorted elements.
The algorithm merges Array2 into Array1 in O(m+n) time.
"""


def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Merge nums2 into nums1 in-place.

    Uses a two-pointer approach starting from the end of both arrays
    to achieve O(m+n) time complexity without extra space.

    Args:
        nums1: First sorted array with length m+n (last n elements are 0 placeholders)
        m: Number of actual elements in nums1
        nums2: Second sorted array with length n
        n: Number of elements in nums2

    Returns:
        None (modifies nums1 in-place)

    Example:
        >>> nums1 = [1, 2, 3, 0, 0, 0]
        >>> nums2 = [2, 5, 6]
        >>> merge(nums1, 3, nums2, 3)
        >>> nums1
        [1, 2, 2, 3, 5, 6]
    """
    # Start from the end of both arrays
    p1 = m - 1  # Pointer for nums1's actual elements
    p2 = n - 1  # Pointer for nums2
    p = m + n - 1  # Pointer for the final position in nums1

    # Merge from the back
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    # If there are remaining elements in nums2, copy them
    # (No need to copy remaining nums1 elements as they're already in place)
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1
