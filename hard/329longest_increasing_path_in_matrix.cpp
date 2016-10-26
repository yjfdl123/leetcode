#include "cpphelp.cpp"
class Solution {
private:
    vector<vector<int> > dp;
    int direct[4][2]={{0,-1},{0,1},{-1,0},{1,0}};
public:
    int longestIncreasingPath(vector<vector<int> >& matrix) {
        if ( (matrix.size()==0) || (matrix[0].size()==0)) return 0;
        int height=matrix.size(), width = matrix[0].size();
        vector<int> tmp(width,0);
        for (int i=0;i<height;i++) dp.push_back(tmp);
        int ret=0;
        for (int i=0;i<height;i++){
            for (int j=0;j<width;j++){
                if (dp[i][j]==0){
                    dp[i][j]=backtracking(matrix,i,j,height,width);
                };
                ret=max(ret,dp[i][j]);
            };
        };
        return ret;
    }
    int  backtracking(vector<vector<int> >&matrix,int hei,int wid,int height,int width){
        if (dp[hei][wid]==0){
            int newhei,newwid;
            int ret=1;
            for (int i=0;i<4;i++){
                newhei = hei+direct[i][0];
                newwid = wid+direct[i][1];
                if ( (newhei>=0) && (newhei<height) && (newwid>=0) && (newwid<width)){
                    if (matrix[newhei][newwid]>matrix[hei][wid]){
                        ret = max(ret, backtracking(matrix,newhei,newwid,height,width)+1);
                    };
                };
            };
            dp[hei][wid]=ret;
            return ret;
        }else{
            return dp[hei][wid];
        };
    };
};
int main(){
};
