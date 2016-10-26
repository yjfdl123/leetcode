#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

vector<int> readdata( ){
    vector<int> ret;
    ifstream fin("data.txt");
    int tmp;
    while (fin>>tmp){
        ret.push_back(tmp);
    }
    fin.close();
    return ret;
};

template<class T>
void printvec(vector<T> vec){
    typedef typename vector<T>::iterator Iter;
    for (Iter iter=vec.begin();iter!=vec.end();++iter){
            cout<<*iter<<"  ";
    };
    cout<<endl;
};
