#include "cpphelp.cpp"
class Solution {
public:
    string toHex(int num) {
        if (num==0) return "0";
        char dic[]={'0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'};
        int tmp;
        string ret(8,'0');
        for (int i=0;i<8;i++){
            tmp = num& 0b1111;
            num=num>>4;
            ret[i]=dic[tmp];
        };
        reverse(ret.begin(),ret.end());
        while (ret[0]=='0'){
            ret=ret.substr(1);
        };
        return ret;
    }
};
int main(){
    Solution so;
    string tmp;
    tmp=so.toHex(26);
    cout<<tmp.c_str()<<endl;
    
};
