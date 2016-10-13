#include<iostream>
#include<vector>
using namespace std;
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int start=0,end=nums.size()-1,mid;
        vector<int> ret(2,-1);
        while (start<=end){
            mid = (start+end)>>1;
            if (nums[mid]==target){
                int s1=mid,s2=mid;
                while ((s1>=0) and (nums[s1]==target))  s1--;
                while ((s2<nums.size()) and (nums[s2]==target)) s2++;
                ret[0]=s1+1;
                ret[1]=s2-1;
                return ret;
            }else if (nums[mid]<target){
                start=mid+1;
            }else{
                end=mid-1;
            };           
        };  
        return ret;
        
    }
};
int main(){
};
