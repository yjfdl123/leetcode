#include "cpphelp.cpp"
class Solution {
private:
    int direct[4][2] = {{0,-1},{0,1},{-1,0},{1,0}};
public:
    bool exist(vector<vector<char> >& board, string word) {
        if (board.size()==0) return false;
        if (board[0].size()==0) return false;
        int height=board.size(),width=board[0].size();
        for (int h=0;h<height;h++){
            for (int w=0;w<width;w++){
                if (backtracking(board,word,h,w,height,width)) return true;
            };
        }
        return false;
    }
    bool backtracking(vector<vector<char> > &board,string word,int hei,int wid,int height,int width){
        if ( (hei<0)||(hei>=height) || (wid<0) || (wid>=width)) return false;
        if ( (board[hei][wid]!=word[0]) || (board[hei][wid]=='*')) return false;
        if (word.size()==1) {
            return true;
        }else{
            for (int i=0;i<4;i++){
                char tmp=board[hei][wid];
                board[hei][wid]='*';
                if (backtracking(board,word.substr(1),hei+direct[i][0],wid+direct[i][1],height,width)) return true;
                board[hei][wid]=tmp;
            };
            return false;
        };
        return false;
    };
};
int main(){
};
