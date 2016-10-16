#include "cpphelp.cpp"
class Solution {
private:
    int ret;
    vector<int> sum;
    vector<int> diff;
    int num;
public:
    int totalNQueens(int n) {
        sum.reserve(2*n-1);
        for (int i=0;i<2*n-1;i++) sum.push_back(0);
        diff.reserve(2*n-1);
        for (int i=0;i<2*n-1;i++) diff.push_back(0);
        ret=0;
        num=n;
        string line(n,'.');
        vector<string> chess(n,line);
        vector<int> column(n,0);
        backtracking(0, chess,column);
        return ret;
    };
    void backtracking(int hei, vector<string > &chess, vector<int> &column){
        if (hei<num){
            for (int wid=0;wid<num;wid++){
                if ( (sum[hei+wid]==0) && (diff[hei-wid+num-1]==0) &&(column[wid]==0) ){
                    sum[hei+wid] =1;
                    diff[hei-wid+num-1] = 1;
                    column[wid]=1;
                    chess[hei][wid]='Q';
                    backtracking(hei+1, chess,column);
                    sum[hei+wid] = 0;
                    diff[hei-wid+num-1] = 0;
                    chess[hei][wid]='.';
                    column[wid]=0;
                }
            }
        }else{
            ret++;
        };
    };
};
int main(){
    Solution so;
    cout<< so.totalNQueens(4) <<endl;;
};
