#include "cpphelp.cpp"
class Solution {
public:
    int candy(vector<int>& ratings) {
        int len=ratings.size();
        vector<int> ret(len,1);
        for (int i=1;i<len;++i){
            if (ratings[i]>ratings[i-1]){
                ret[i]=ret[i-1]+1;
            };
        };
        for (int i=len-2;i>=0;--i){
            if (ratings[i]>ratings[i+1]){
                ret[i]=max(ret[i],ret[i+1]+1);
            };
        };
        int total=accumulate(ret.begin(),ret.end(),0);
        return total;
    }
};
int main(){
};
