#include "cpphelp.cpp"
class Solution {
public:
    int findMin(vector<int>& nums) {
        int len=nums.size();
        int start=0,end=len-1;
        int mid=0;
        while (start<=end){
            if (start==end) return nums[start];
            mid=(start+end)/2;
            if (nums[start]<nums[end]){
                return nums[start];
            }else if (nums[start]==nums[end]){
                start++;
            }else if (nums[start]>nums[end]){
                if (nums[mid]>=nums[start]){
                    start=mid+1;
                }else{
                    end=mid;
                };
            };
        };
        return nums[mid];
    }
};
int main(){
};
