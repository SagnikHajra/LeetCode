class FindTheSingleNum(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 1:
            return nums[0]
        i = 0
        nums = sorted(nums)
        while i < l-1:
            if nums[i] != nums[i+1]:
                return nums[i]
            if nums[l-1-i] != nums[l-2-i]:
                return nums[l-1-i]
            i += 2

        return nums[i]

