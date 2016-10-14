#include<iostream>
#include<vector>
using namespace std;
class Solution {
public:
    int maxProduct(vector<string>& words) {
        vector<int> hash(words.size());
        int wordnum = words.size();
        int code = 0;
        vector<int> initmap(26, 0);
        vector<int> charmap(26, 0);
        for (int i = 0; i<wordnum; i++){
            charmap = initmap;
            string word = words[i];
            for (int j = 0; j<word.length(); j++){
                charmap[word[j] - 'a'] = 1;
            };
            code = 0;
            for (int j = 0; j<26; j++){
                code = code << 1 | charmap[j];
            };
            hash[i] = code;
        };
        int maximum = 0;
        for (int i = 0; i<wordnum - 1; i++){
            for (int j = i + 1; j<wordnum; j++){
                int  tmp = hash[i] & hash[j];
                if ( (hash[i] & hash[j]) == 0){
                    if (words[i].length()*words[j].length()>maximum){
                        maximum = words[i].length()*words[j].length();
                    };
                };
            };
        };
        return maximum;
    }
};
int main(){
    cout << (2 | 1==0) << endl;
    string test[6] = { "abcw", "baz", "foo", "bar", "xtfn", "abcdef" };
    //string test[2] = { "abcw", "efg" };
    vector<string> xx;
    int len = sizeof(test) / sizeof(test[0]);
    xx.reserve(len);
    for (int i = 0; i < len; i++){
        xx.push_back(test[i]);
    };
    Solution so;
    cout << so.maxProduct(xx);
    int x;
    cin >> x;
};
