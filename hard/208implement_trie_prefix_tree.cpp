#include "cpphelp.cpp"
class TrieNode {
public:
    char var;
    bool isword;
    TrieNode* arr[26];
public:
    // Initialize your data structure here.
    TrieNode(char w) {
        var=w;
        isword=false;
        for (int i=0;i<26;i++){
            arr[i]=NULL;
        };
    }
    TrieNode(){
        var='*';
        isword=false;
        for (int i=0;i<26;i++){ 
            arr[i]=NULL;
        };
    };
};

class Trie {
public:
    Trie() {
        root = new TrieNode();
    }

    // Inserts a word into the trie.
    void insert(string word) {
        TrieNode* node=root;
        int index;
        for (int i=0;i<word.size();i++){
            index=word[i]-'a'; 
            if ((node->arr)[index]==NULL){
                TrieNode* newnode= new TrieNode(word[i]);
                (node->arr)[index]=newnode;
                node=newnode;
            }else{
                node = (node->arr)[index];
            };
            if (i==word.size()-1){
                node->isword=true;
            }
        };
    }

    // Returns if the word is in the trie.
    bool search(string word) {
        TrieNode* node=root;
        int index;
        for (int i=0;i<word.size();i++){
            index=word[i]-'a';
            if ( (node->arr)[index]==NULL){
                return false;
            }else{
                node= (node->arr)[index];
                if (i==word.size()-1){
                    return node->isword;
                };
            }
        };
        return false;
    }

    // Returns if there is any word in the trie
    // that starts with the given prefix.
    bool startsWith(string prefix) {
        TrieNode * node=root;
        int index;
        for (int i=0;i<prefix.size();i++){
            index=prefix[i]-'a';
            if ( (node->arr)[index]==NULL){
                return false;
            }else{
                node = (node->arr)[index];
            };
        };
        return true; 
    }

private:
    TrieNode* root;
};

// Your Trie object will be instantiated and called as such:
// Trie trie;
// trie.insert("somestring");
// trie.search("key");
int main(){
};
