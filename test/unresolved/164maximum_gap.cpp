#include "cpphelp.cpp"
#include "limits.h"
#include <math.h>
struct Grid{
    int minboard;
    int maxboard;
    int localnum;
    Grid():localnum(0){};
};
class Solution {
public:
    int maximumGap(vector<int>& nums) {
        if (nums.size()<2) return 0;
        if (nums.size()==2) return abs(nums[0]-nums[1]);
        int gapnum = nums.size()-1;
        int start=INT_MAX , end=INT_MIN;
        for (int i=0;i<nums.size();i++){
            start = min(start,nums[i]);
            end = max(end, nums[i]);
        };
        double interval = (double)(end-start)/gapnum;
        vector<Grid*> vec;
        vec.reserve(gapnum);
        for (int i=0;i<gapnum;i++){
            Grid * tmp = new Grid();
            tmp->minboard=0;
            tmp->maxboard=0;
            vec.push_back(tmp);
        };
        int level=0;
        for (int i=0;i<gapnum;i++){
            level = (floor)(nums[i]/interval);
            if (vec[level]->localnum==0){
                vec[level]->minboard = vec[level]->maxboard = nums[i];
            }else{
                vec[level]->minboard = min(vec[level]->minboard,nums[i]);
                vec[level]->maxboard = max(vec[level]->maxboard,nums[i]);
            };
            vec[level]->localnum++;
        };
        int previous=0;
        int ret=0;
        for (int i=1;i<gapnum;i++){
            if (vec[i]->localnum==0) continue;
            ret = max(ret, vec[i]->minboard - vec[previous]->maxboard);
            previous = i;
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
