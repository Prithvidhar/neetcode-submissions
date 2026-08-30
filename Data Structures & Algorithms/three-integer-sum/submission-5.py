class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        left = 0
        right = len(nums) - 1
        ans = []
        nums.sort()
        # print("after sort", nums)
        for i in range(len(nums)):
            print(" i is", i)
            if i > 0 and nums[i] == nums[i-1]: continue
            setty = []
            left = i +1
            right = len(nums) - 1
            while(left< right):
                # print(nums[left] + nums[right], -nums[i], nums[left] + nums[right] == -nums[i])
                # print(nums[left], nums[right], left, right)
                if nums[left] + nums[right] < -nums[i]:
                    left = left +1
                elif nums[left] + nums[right] > -nums[i]:
                    right = right -1
                else:
                    print("f")
                    # print(nums[left],nums[right], nums[i])
                    setty = []
                    setty.append(nums[i])
                    setty.append(nums[left])
                    setty.append(nums[right])
                    setty.sort()
                    ans.append(setty)
                    left = left +1
                    right = right -1
                    while left < right and nums[left] == nums[left-1]:
                        left = left +1
                    while left < right and nums[right] == nums[right+1]:
                        right = right - 1




        return ans



        