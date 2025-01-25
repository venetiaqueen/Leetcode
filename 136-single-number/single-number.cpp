class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int num1 = 0, num2 = 0, num3 = 0;
        for( int i = 0; i < nums.size() ; i++) 
        {
            num1 ^= nums[i];
            num2 |= num1 & nums[i];
            num3 = num1 & num2;
            
        }
        return num1;
    }
};