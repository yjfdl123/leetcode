#include <iostream>
#include <map>
using namespace std;
class Solution {
public:
    int longestPalindrome(string s) {
        map<char,int> tongji;
        for (int i=0;i<s.length();i++){
            if (tongji.count(s[i])==0){
                tongji[s[i]]=1;
            }else{
                tongji[s[i]]++;
            };
        }
        int num=0;
        int simple=0;
        typedef map<char,int>::iterator Iter;
        for (Iter iter=tongji.begin();iter!=tongji.end();iter++){
            if (iter->second%2==0){
                num+=iter->second;
            }else{
                simple=1;
                num+=iter->second-1;
            }
        };
        num+=simple; 
        return num;
        
    };
};
int main(){
    Solution so;
    cout<<so.longestPalindrome("abccccdd");
    cout<<so.longestPalindrome("ccc");
    cout<<123<<endl; 
};
