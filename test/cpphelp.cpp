#include<vector>
#include<iostream>
#include<algorithm>
using namespace std;
#define  GETSIZE(arr) (sizeof(arr)/sizeof(arr[0]))
template<typename T>
void printvec(vector<T> &vec){
    typedef  typename vector<T>::iterator Iter;
    for (Iter iter=vec.begin();iter!=vec.end();iter++){
        cout<<*iter<<"   ";
    };
    cout<<endl;
};
template<typename T>
void print2vec(vector<T> vec){
    typedef typename vector<T>::iterator Iter;
    for (Iter iter=vec.begin();iter!=vec.end();iter++){
        printvec(*iter);
    };
};
template<typename T>
vector<T> array_to_vec(T arr[],int len){
    vector<T> vec;
    vec.reserve(len);
    for (int i=0;i<len;i++){
        vec.push_back(arr[i]);
    };
    return vec;

};
