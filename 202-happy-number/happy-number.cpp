class Solution {
public:
 bool isHappy(int n) {
        set<int> num_set; 
        int sum = n;
        while(true){
            sum = sum_digit_squared(sum);
            if(sum == 1)
                return true;
            else{
                if(num_set.find(sum) != num_set.end())
                    return false;
                else
                    num_set.insert(sum);
            }
        }
    }
    
    int sum_digit_squared(int n){
        int sum = 0;
        while(true){
            int d = n % 10; 
            sum += (d*d);
            n = n/10;
            if(n == 0)
                break;
        }
        
        return sum;
    }
};