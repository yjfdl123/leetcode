#include "cpphelp.cpp"
struct POS
{
    int h;
    int w;
    POS(int newh, int neww): h(newh), w(neww) {}
};
class Solution {
public:
    void solve(vector<vector<char> >& board) {
        int height=board.size();
        if (height==0) return ;
        int width =board[0].size();
        int posh,posw;
        for (int hei=0;hei<height;hei++){
            for (int wid=0;wid<width;wid++){
                if ( (  board[hei][wid]=='O') && ((hei==0)||(hei==height-1)||(wid==0)||(wid==width-1) )) {
                    queue<POS*> que;
                    que.push( new POS(hei,wid));
                    while (!que.empty()){
                        POS * point=que.front();
                        que.pop();
                        posh = point->h;
                        posw = point->w;
                        board[posh][posw]='D';
                        if ( (posh>0) && (board[posh-1][posw]=='O'))  que.push( new POS(posh-1,posw)    );
                        if ( (posh<height-1) && (board[posh+1][posw]=='O')) que.push( new POS(posh+1,posw));
                        if ( (posw>0) && (board[posh][posw-1]=='O'))  que.push( new POS(posh,posw-1)   );
                        if ( (posw<width-1)  && (board[posh][posw+1]=='O')) que.push( new POS(posh,posw+1));
                        delete point;
                    };
                };
            };
        };
        for (int i=0;i<height;i++){
            for (int j=0;j<width;j++){
                if (board[i][j]=='O'){
                    board[i][j]='X';
                }else if (board[i][j]=='D'){
                    board[i][j]='O';
                }
            }
        };
    };
};
int main(){
    
};

