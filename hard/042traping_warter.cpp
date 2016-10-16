#include "cpphelp.cpp"
class Solution {
public:
    int trap(vector<int>& height) {
        int len=height.size();
        if (len<3) return 0;
        int left=0,right=len-1;
        int ret =0;
        int base=0;
        while (left<right){
            if (height[left]<=height[right]){
                base=height[left++];
                while (height[left]<base){
                    ret+=base-height[left++];
                } ;
            }else{
                base=height[right--];
                while (height[right]<base){
                    ret+=base-height[right--];
                };
            };
        };
        return ret;
    }
};
int main(){
};
