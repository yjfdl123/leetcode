#include<iostream>
#include<vector>
#include<algorithm>
#define  GETSIZE(arr) (sizeof(arr)/sizeof(arr[0]))

using namespace std;
template<typename T>
void printvec(vector<T> &vec){
    typedef  typename vector<T>::iterator Iter;
    cout<<vec.size()<<endl;
    for (Iter iter=vec.begin();iter!=vec.end();iter++){
        cout<<*iter<<"   ";
    };
    cout<<endl;
};
class Solution {
public:
    vector<vector<int> > fourSum(vector<int>& nums, int target) {
        int len=nums.size();
        sort(nums.begin(),nums.end());
        vector<vector<int> > ret;
        vector<int > tmp;
        tmp.reserve(4);
        int start,end,newtarget,sum;
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
                        ret.push_back(tmp);
                        //cout<<tmp[0]<<tmp[1]<<tmp[2]<<tmp[3]<<endl;
                        printvec(tmp);
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
template<typename T>
void print2vec(vector<T> vec){
    typedef typename vector<T>::iterator Iter;
    for (Iter iter=vec.begin();iter!=vec.end();iter++){
        printvec(*iter);
    };
};
template<typename T>
vector<T> array_to_vec(T arr[],int len){
    vector<T> vec;
    vec.reserve(len);
    for (int i=0;i<len;i++){
        vec.push_back(arr[i]);
    };
    return vec;

};
int main(){
    Solution so;
    int s[]={1, 0, -1, 0, -2, 2};
    int target=0;
    vector<int> test=array_to_vec(s, GETSIZE(s));
    printvec(test);
    print2vec( so.fourSum(test,target));
    
};
