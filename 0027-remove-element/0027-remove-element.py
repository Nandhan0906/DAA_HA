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
    
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0  # Pointer for the next position of a non-val element
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # Move non-val element to the front
                k += 1
        
        return k  # Number of elements not equal to val