#include"cpphelp.cpp"
#include <stdio.h>
class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string> ret;
        int len=nums.size();
        if (len==0) return ret;
        int start=0,end=1;
        string range="";
        char data1[32],data2[32];
        while (end<len){
            if  (nums[end]==nums[end-1]+1) {
                end++;
            }else{
                sprintf(data1,"%d",nums[start]);
                range = data1;
                if (end!=start+1){
                    sprintf(data2,"%d",nums[end-1]);
                    range += string("->")+data2;
                };
                ret.push_back(range);
                start=end;
                end++;
            };
        };
        sprintf(data1,"%d",nums[start]);
        range = data1;
        if (end!=start+1){
            sprintf(data2,"%d",nums[end-1]);
            range += string("->")+data2;
        };
        ret.push_back(range);
        return ret;
    }
};
int main(){
};
