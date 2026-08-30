// import java.util.Stack;
class Solution {
    public boolean isValid(String s) {

        Stack<Character> stacky = new Stack<>();
        for(char c : s.toCharArray())
        {
            //Check if open char
            if(c == '(' || c == '[' || c == '{')
            {
                stacky.push(c);
            }
            else
            {
                if(stacky.isEmpty())
                {
                    return false;
                }
                char check = stacky.pop();
                if(check == '(' && c != ')')
                {
                    return false;
                }
                else if(check == '[' && c != ']')
                {
                    return false;
                }
                else if(check == '{' && c != '}')
                {
                    return false;
                }
            }


        }

        if(!stacky.isEmpty())
        {
            return false;
        }

        return true;

        
    }
}
