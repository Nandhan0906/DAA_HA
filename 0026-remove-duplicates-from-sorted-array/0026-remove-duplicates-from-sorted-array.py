class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        # Pointer for the position of the next unique element
        unique_index = 0
        
        for i in range(1, len(nums)):
            if nums[i] != nums[unique_index]:  # Found a new unique element
                unique_index += 1
                nums[unique_index] = nums[i]  # Move it to the next position
        
        return unique_index + 1  # Number of unique elements
