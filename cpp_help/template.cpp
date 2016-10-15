#define  GETSIZE(arr) (sizeof(arr)/sizeof(arr[0]))

template<typename T>
void printvec(vector<T> vec){
    typedef  typename vector<T>::iterator Iter;
    for (Iter iter=vec.begin();iter!=vec.end();iter++){
        cout<<*iter<<"   ";
    };
    cout<<endl;
};


vector<int> array_to_vec(int arr[],int len){
    vector<int> vec;
    cout<< sizeof(arr)<< "   "<<sizeof(arr[0])<<endl;
    vec.reserve(len);
    for (int i=0;i<len;i++){
        vec.push_back(arr[i]);
    };
    return vec;

};