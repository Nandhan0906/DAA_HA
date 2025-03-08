class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Ensure nums1 is the smaller array for efficient binary search
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        x, y = len(nums1), len(nums2)
        low, high = 0, x

        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (x + y + 1) // 2 - partitionX  # Ensures left half is always <= right half

            # Handle edge cases where partition is at the beginning or end of the array
            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == x else nums1[partitionX]

            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == y else nums2[partitionY]

            # Check if the current partition is valid
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # Calculate median based on combined array length parity
                if (x + y) % 2 == 1:
                    return max(maxLeftX, maxLeftY)
                else:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
            # Adjust binary search boundaries
            elif maxLeftX > minRightY:
                high = partitionX - 1
            else:
                low = partitionX + 1

        raise ValueError("Input arrays are not sorted or have unexpected values")