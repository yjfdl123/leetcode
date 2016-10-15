#include "cpphelp.cpp"
class Solution {
    private: 
        vector<vector<int> > ret;
    public:
            vector<vector<int> > subsetsWithDup(vector<int>& nums) {
                sort(nums.begin(),nums.end());
                vector<int> solu;
                for (int i=0;i<=nums.size();i++){
                    backtracking(nums,0,i,solu);
                };
                return ret;
            };
            void backtracking(vector<int>& nums, int start,int k, vector<int>& solu){
                if (k>0){
                    for (int i=start;i<nums.size();++i){
                        solu.push_back(nums[i]);
                        if (nums.size()-start>=k){
                            backtracking(nums, i+1,k-1,solu);
                        };
                        solu.pop_back();
                    };
                }else if (k==0){
                    for (int x=0;x<ret.size();++x){
                        if (ret[x]==solu) return ;
                    };
                    ret.push_back(solu);
                };
            };
};
int main(){
    int arr[]={1,2,2};
    vector<int> test = array_to_vec(arr,GETSIZE(arr));
    Solution so;
    print2vec( so.subsetsWithDup(test));
};
