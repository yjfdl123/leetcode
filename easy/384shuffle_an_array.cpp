#include<iostream>
#include<stdlib.h>
#include<vector>
using namespace std;
class Solution {
private:
    vector<int> origin, cur;
public:
    Solution(vector<int> nums):origin(nums),cur(nums) {
    }
    
    /** Resets the array to its original configuration and return it. */
    vector<int> reset() {
        return origin ;
    }
    
    /** Returns a random shuffling of the array. */
    vector<int> shuffle() {
        int index;
        for (int i= cur.size()-1;i>0;--i){
            index = rand()%(i+1);
            swap( cur[i],cur[index]);
        };
        return cur;
        
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * vector<int> param_1 = obj.reset();
 * vector<int> param_2 = obj.shuffle();
 */
void printvec(vector<int> xx){
    for (int i=0;i<xx.size();i++){
        cout<<xx[i]<<"  ";
    };  
    cout<<endl;
};  
int main(){
    vector<int> test(3);
    for (int i=0;i<test.size();i++){
        test[i]=i+1;
    };
    Solution so(test);
    printvec(so.shuffle());
    printvec(so.reset());
    printvec(so.shuffle());
    
    
};
