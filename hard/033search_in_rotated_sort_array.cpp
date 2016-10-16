#include "cpphelp.cpp"
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int len=nums.size();
        int start=0,end=len-1;
        int mid=0;
        while (start<=end){
            mid=(start+end)>>1; 
            if (nums[mid]==target) return mid;
            if (nums[mid]>nums[start]){
                if ( (target>=nums[start]) &&(target<nums[mid])){
                    end=mid-1;
                }else{
                    start=mid+1;
                };
            }else if (nums[mid]<nums[start]){
                if ( (target>nums[mid]) && (target<=nums[end])){
                    start=mid+1;
                }else{
                    end=mid-1;
                };
            }else{
                start++;
            };
        }
        return -1;
    }
};
int main(){
};
