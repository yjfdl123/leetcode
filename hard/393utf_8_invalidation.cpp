#include "cpphelp.cpp"
class Solution {
public:
    bool validUtf8(vector<int>& data) {
        int len=data.size();
        if (len==0) return false;
        int count=0;
        int num=data[0];
        int bit=32;
        int tmp;
        while ((bit >0) &&(num!=0)  ){
            tmp= 1<<bit;
            if (( tmp&num)!=0){
                bit--;
                count++;
                if (count>5) break;
            }else{
                break;
            };
        };
        if (count==0){
            return true;
        }else if (count==1){
            return false;
        }else if (count>4){
            return false;
        }else if (data.size()<count){
            return false; 
        }else{
            int xxx=1;
            int bit1=xxx<<32;
            int bit2=xxx<<31;
            for (int i=1;i<count;i++){
                if ((data[i]&bit1)==0) return false;
                if ((data[i]&bit2)!=0) return false;
            };
        };
        return true;
    }
};
int main(){
    int x=0;
    cout<<sizeof(x)<<endl;
};
