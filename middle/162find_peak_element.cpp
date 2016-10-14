#include<iostream>
#include<vector>
using namespace std;
class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int start=0,end=nums.size()-1;
        int len = nums.size()-1;
        if (end<0) return 0;
        if (len==0) return 0;
        int mid=0;
        while (start<=end){
            mid = (start+end)>>1;
            if (mid==0){
                if (nums[mid]>nums[mid+1]){
                    return mid;
                }else{
                    start=mid+1;
                };
            }else if (mid==len){
                if (nums[mid]>nums[mid-1]){
                    return mid;
                }else{
                    end=mid-1;
                };
            }else{
                if ( (nums[mid]>nums[mid-1]) and (nums[mid]>nums[mid+1])){
                    return mid;
                }else if (nums[mid]<nums[mid-1]){
                    end = mid-1;
                }else if (nums[mid]<nums[mid+1]){
                    start=mid+1;
                }else{
                    start++;
                };
            }; 
        };
        
    }
};
int main(){
    Solution so;
    vector<int> x;
    x.push_back(1);
//    x.push_back(2);
//    x.push_back(3);
//    x.push_back(1);
    cout<< so.findPeakElement(x)<<endl;
};
