class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        //declare the unorderd list 
        std::unordered_set<int> check_num;
        //itrating the loop 
        for(int num:nums){
            //checking if the value is present in the num or not
            if(check_num.find(num) != check_num.end()){
                return true;
            }
            check_num.insert(num);
        }
        return false;
    }
};
