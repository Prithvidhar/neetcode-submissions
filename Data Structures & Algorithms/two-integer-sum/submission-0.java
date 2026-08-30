class Solution {
    public int[] twoSum(int[] nums, int target) {

        int actT = 0;
        int[] ans = new int[2];
        for(int i = 0; i < nums.length -1; i++)
        {
            actT = target - nums[i];
            for(int j = i+1; j < nums.length; j++)
            {
                System.out.printf("i: %d, j: %d\n",i,j);
                if(nums[j] == actT)
                {
                    ans[0] = i;
                    ans[1] = j;
                    return ans;
                }
            }
        }

        return null;
        
    }
}
