#include "cpphelp.cpp"

template <class T>
class comp : public binary_function<T,T,bool >{
    public:
            bool operator()(T& t1,T& t2){
                        int sum1 = t1.first + t1.second;
                        int sum2 = t2.first + t2.second;
                        return sum1 < sum2;
            };
};
class Solution {
    public:
            vector<pair<int, int> > kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
                        vector<pair<int,int> > ret;
                        priority_queue< pair<int,int>, vector<pair<int,int> >, comp<pair<int,int> > > que;
                        pair<int,int> tmp(0,0);
                        for (int i=0;i<nums1.size();i++){
                            for (int j=0;j<nums2.size();j++){
                                if (que.size()<k){
                                    tmp.first=nums1[i];
                                    tmp.second=nums2[j];
                                    que.push(tmp);
                                }else{
                                    tmp=que.top();
                                    if (nums1[i]+nums2[j]<=tmp.first+tmp.second){
                                        que.pop();
                                        tmp.first=nums1[i];
                                        tmp.second=nums2[j];
                                        que.push(tmp);
                                    };
                                };
                            };
                        };
                        while (!que.empty()){
                            ret.push_back( que.top());
                            que.pop();
                        };
                        return ret;
                    }
};
int main(){
};
