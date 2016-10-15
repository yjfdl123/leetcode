#include<vector>
#include<iostream>
#include<algorithm>
#include<queue>
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
void print_vec_pair(vector<pair<int,int> > &vec){
    typedef typename vector<pair<int,int> >::iterator Iter;
    for (Iter iter=vec.begin();iter!=vec.end();iter++){
        cout<< iter->first<<"  "<<iter->second<<endl;
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
template <class T>
class comp : public binary_function<T,T,bool >{
    public:
            bool operator()(T& t1,T& t2){
                        int sum1 = t1.first + t1.second;
                        int sum2 = t2.first + t2.second;
                        return sum1 < sum2;
            };
};
