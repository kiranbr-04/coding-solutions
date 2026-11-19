class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        a = []
        for i in nums:
            if val != i:
                a.append(i)

        k = len(a)
        nums[:k] = a
        return k
        

        