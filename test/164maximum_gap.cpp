#include "cpphelp.cpp"
#include "limits.h"
#include <math.h>
struct Grid{
    int minboard;
    int maxboard;
};
class Solution {
public:
    int maximumGap(vector<int>& nums) {
        if (nums.size()<2) return 0;
        int gapnum = nums.size()-1;
        int start=INT_MIN , end=INT_MIN;
        for (int i=0;i<nums.size();i++){
            start = min(start,nums[i]);
            end = max(end, nums[i]);
        };
        double interval = (double)(end-start)/gapnum;
        vector<Grid*> vec;
        vec.reserve(gapnum);
        for (int i=0;i<gapnum;i++){
            Grid * tmp = new Grid();
            tmp->minboard=INT_MAX;
            tmp->maxboard=INT_MIN;
            vec.push_back(tmp);
        };
        int level=0;
        for (int i=0;i<nums.size();i++){
            level = (floor)(nums[i]/interval);
            vec[level]->minboard = min(vec[level]->minboard,nums[i]);
            vec[level]->maxboard = max(vec[level]->maxboard,nums[i]);
        };
        int ret=INT_MIN;
        for (int i=1;i<nums.size();i++){
            ret = max(ret, vec[i]->minboard - vec[i]->maxboard);
        };
        return ret;
    }
};
int main(){
    cout<<INT_MAX<<endl;
    cout<<INT_MIN<<endl;
    Solution so;
    int arr[]={1,10000};
    vector<int> test = array_to_vec(arr,GETSIZE(arr));
    cout<< so.maximumGap( test);
};
