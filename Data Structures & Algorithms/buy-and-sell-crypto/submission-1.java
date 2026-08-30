class Solution {
    public int maxProfit(int[] prices) {

        int min = 999;
        int minIndex = -1;
        int ans = 0;
        int start = 0;
        int end = start +1;

        while(start < prices.length && end < prices.length)
        {
            // System.out.printf("start: %d index %d, end: %d index %d", prices[start], start, prices[end], end);
            if(prices[start] >= prices[end])
            {
                start = end;
                end = start +1;
            }
            else
            {
                
                int diff = prices[end] - prices[start];
                ans = Math.max(ans,diff);
                end++;
            }
        }

        return ans;
        

        
    }
}
