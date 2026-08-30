// import java.util.Set;
// import java.util.HashSet
class Solution {
    public boolean hasDuplicate(int[] nums) {

        Set<Integer> set = new HashSet<Integer>();

        for( int i = 0; i < nums.length; i++)
        {
            set.add(nums[i]);
        }

        if(set.size() == nums.length)
        {
            return false;
        }
        return true;
        // for(int key : count.keySet())
        // {
        //     if(count.get(key)>1)
        //     {
        //         return true;
        //     }
        // }

        // return true;
 
    }
}
