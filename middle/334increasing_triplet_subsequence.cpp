#include<iostream>
#include<vector>
using namespace std;
class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        int min_one = 2147483647;
        int min_two = 2147483647;
        for (int i=0;i<nums.size();i++){
            if (nums[i]>min_two){
                return true;
            }
            else if ( (nums[i]>min_one) and (nums[i]<min_two)){
                min_two = nums[i];
            }
            else if (nums[i]<min_one){
                min_one=nums[i];
            };
        };
        return false;
    }
};
int main(){
};
