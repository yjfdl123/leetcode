#include"cpphelp.cpp"

using namespace std;
class Solution {
public:
    vector<vector<int> > fourSum(vector<int>& nums, int target) {
        int len=nums.size();
        sort(nums.begin(),nums.end());
        vector<vector<int> > ret;
        vector<int > tmp(4,0);
        int start,end,newtarget,sum;
        bool same=false;
        for (int i=0;i<len-3;i++){
            for (int j=i+1;j<len-2;j++){
                start=j+1;
                end=len-1;
                tmp[0]=nums[i];
                tmp[1]=nums[j];
                newtarget=target-tmp[0]-tmp[1];
                while (start<end){
                    sum=nums[start]+nums[end];
                    if (sum==newtarget){
                        tmp[2]=nums[start];
                        tmp[3]=nums[end];
                        same=false;
                        for (int i=0;i<ret.size();i++){
                            if (ret[i]==tmp){
                                same=true;
                            };
                        };
                        if (!same){
                            ret.push_back(tmp);
                        };
                        start++;
                    }else if(sum<newtarget){
                        start++;
                    }else{
                        end--;
                    };
                };
            };
        };
        return ret;
    }
};
int main(){
    Solution so;
    int s[]={-3,-2,-1,0,0,1,2,3};
    int target=0;
    vector<int> test=array_to_vec(s, GETSIZE(s));
    printvec(test);
    print2vec( so.fourSum(test,target));
    
};
