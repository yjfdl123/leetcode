#include <iostream>
#include <fstream>
#include <stdlib.h>
using namespace std;
int main(){
    ofstream fout("data.txt");
    int totalnum = 30;
    int range=100;
    for (int i=0;i<totalnum;i++){
        fout<< rand()%range<<endl;
    };
    fout<<"test"<<endl;
    fout.close();
    return 0;
};
