#include<iostream>
#include<vector>
using namespace std;
class Solution {
public:
    void rotate(vector<vector<int> >& matrix) {
        int n = matrix.size()-1;
        int hstart=0,wstart=0;
        int hend=n,  wend=n;
        int idx=0,tmp=0;
        while (wstart<wend){
            for (idx=0;idx<wend-wstart;idx++){
                tmp = matrix[hstart][wstart+idx];
                matrix[hstart][wstart+idx] = matrix[hend-idx][wstart];
                matrix[hend-idx][wstart] = matrix[hend][wend-idx];
                matrix[hend][wend-idx] = matrix[hstart+idx][wend];
                matrix[hstart+idx][wend]=tmp;
            };
            wstart++;
            wend--;
            hstart++;
            hend--;
        };
    }
};
int main(){
};
