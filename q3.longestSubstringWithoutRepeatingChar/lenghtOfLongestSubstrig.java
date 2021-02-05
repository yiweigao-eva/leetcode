class Solution {
    public int lengthOfLongestSubstring(String s) {
        String sub = "";
        int longest = 0;
        int left = 0;
        int right = 0;
        int len = s.length();
        
        while (right<len){
            // not occured in substring
            if (sub.indexOf(s.charAt(right)) < 0) {
                // then add it to substring, and move right pointer 
                sub += s.charAt(right);
                right++;
            } 
            // the char occured in substing
            else {
                // then only move the left pointer, but not the right
                left++;
                sub = sub.substring(1);
            }
            // can change to Math.max()
            if (sub.length() > longest){
                longest = sub.length();
            }
        }
        return longest;
    }
}

// improvement: change the substring variable to hastable instead of string
// then no need to check the uniquness
