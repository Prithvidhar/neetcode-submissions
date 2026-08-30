class Solution {
    public boolean isPalindrome(String s) {

        String reverse = "";

        s = s.replaceAll("[^a-zA-Z0-9]","").toLowerCase();

        for(int i = s.length()-1; i >= 0; i--)
        {
            reverse += s.charAt(i);
        }
        reverse = reverse.replaceAll("[^a-zA-Z0-9]","");
        // System.out.println(reverse);

        if(s.equals(reverse))
        {
            return true;
        }

        return false;
        
    }
}
