#include "cpphelp.cpp"
class Solution {
    int count;
    int direct[4][2]={{0,-1},{0,1},{-1,0},{1,0}};
public:
    int numIslands(vector<vector<char> >& grid) {
        if ((grid.size()==0) || (grid[0].size()==0)) return 0;
        int height=grid.size(),width=grid[0].size();
        count=0;
        for (int i=0;i<height;i++){
            for (int j=0;j<width;j++){
                if (grid[i][j]=='1'){
                    count++;
                    backtracking(grid,i,j,height,width);
                };
            };
        };
        return count;
    }
    void backtracking(vector<vector<char> >&grid,int hei,int wid,int height,int width){
        int newhei,newwid;
        grid[hei][wid]='0';
        for (int i=0;i<4;i++){
            newhei = hei+direct[i][0];
            newwid = wid+direct[i][1];
            if ( (newhei>=0) && (newhei<height) && (newwid>=0) && (newwid<width)){
                if (grid[newhei][newwid]=='1')  backtracking(grid,newhei,newwid,height,width);
            };
        };
    };
};
int main(){
};
