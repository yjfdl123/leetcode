#include<iostream>
#include<vector>
#include<queue>
using namespace std;
class Solution {
public:
    int numIslands(vector<vector<char> >& grid) {
        queue<pair<int,int> > que;
        int height =grid.size(), width=grid[0].size();
        int numisland = 0;
        for (int h=0;h<height;++h){
            for( int w=0;w<width;++w){
                if ( grid[h][w]==1){
                    pair<int,int> tmp(h,w); 
                    que.push( tmp);
                    while (!que.empty()){
                        numisland++;
                        tmp = que.front();
                        que.pop();
                        int x=tmp.first, y=tmp.second;
                        if ( (x>0) && (grid[x-1][y]==1)){
                            pair<int,int> adj(x-1,y);
                            que.push(adj);
                        };
                        if ( (y>0) && (grid[x][y-1]==1)){
                            pair<int,int> adj(x,y-1);
                            que.push(adj);
                        };
                        if ( (x<width-1) && (grid[x+1][y]==1)){
                            pair<int,int> adj(x+1,y);
                            que.push(adj);
                        };
                        if ( (y<height-1) && (grid[x][y+1]==1)){
                            pair<int,int> adj(x,y+1);
                            que.push(adj);
                        };
                        grid[x][y]=2; 
                    };
                };
            };
        };
        return numisland;
        
    }
};
int main(){
};
