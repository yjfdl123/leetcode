#include "cpphelp.cpp"
class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        int len=nums.size();
        vector<int> ret(len,0);
        vector<int> minarr;
        vector<int>::iterator iter;
        int index;
        for (int i=len-1;i>=0;i--){
            if (i==len-1){
                minarr.push_back(nums[i]);
                ret[i]=0;
            }else{
                iter=lower_bound( minarr.begin(),minarr.end(),nums[i]); 
                index=distance(minarr.begin(),iter);
                if (index==minarr.size()){
                    minarr.push_back(nums[i]);
                    ret[i]=index;
                }else if (nums[i]==*iter){
                    ret[i]=index;
                }else if(nums[i]<*iter){
                    ret[i]=index;
                    *iter = nums[i];
                };
            }; 
        };
        return ret;
    }
};
int main(){
    int arr[]={5, 2, 6, 1};
    Solution so;
    vector<int> nums;
    for (int i=0;i<GETSIZE(arr);i++){
        nums.push_back(arr[i]);
    };
    vector<int> ret= so.countSmaller(nums);
    printvec(ret);
};
