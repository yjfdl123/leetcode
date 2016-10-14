#include<iostream>
#include<vector>
using namespace std;
class Solution {
public:
    int integerReplacement(int n) {
        int even=0;
        if (n%2==0){
            even=n;
        }else{
            even=n+1;
        };
        vector<int> dp(even+1,0);
        dp[1]=0;
        dp[2]=1;
        int start=3;
        while (start<=even){
            dp[start+1]=dp[(start+1)/2]+1;
            dp[start] = min(dp[start-1],dp[start+1])+1;
            start+=2;
        };
        return dp[n];
    }
};
int main(){
    Solution so;
    cout<< so.integerReplacement(7);
    cout<< so.integerReplacement(8);
};
