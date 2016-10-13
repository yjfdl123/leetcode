#include<iostream>
#include<vector>
using namespace std;
class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        int cha=0;
        for (int i=0;i<nums.size();i++){
            cha = cha ^ nums[i];
        };
        int fir=1;
        while ((fir & cha)==0){
            fir = fir<<1;
        };
        vector<int> nums1;
        vector<int> nums2;
        for (int i=0;i<nums.size();i++){
            if ((nums[i]&fir)==0){
                nums1.push_back(nums[i]);
            }else{
                nums2.push_back(nums[i]);
            };
        };
        int a=0;
        int b=0;
        for (int i=0;i<nums1.size();i++){
            a=a^nums1[i];
        };
        for (int i=0;i<nums2.size();i++){
            b=b^nums2[i];
        };
        //cout<<a<<b<<endl;
        vector<int> ret;
        ret.push_back(a);
        ret.push_back(b);
        return ret;
    }
};
int main(){
    Solution so;
    int a[10]={1,1,2,3,4,4,6,6,7,7};
    vector<int> x;
    for (int i=0;i<sizeof(a)/sizeof(a[0]);i++){
        x.push_back(a[i]);
    };
    so.singleNumber(x);

};
