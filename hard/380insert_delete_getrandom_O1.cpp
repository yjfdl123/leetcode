#include "cpphelp.cpp"
class RandomizedSet {


private:
    unordered_map<int, int> wordmap;
    vector<int> order;
public:
    /** Initialize your data structure here. */
    RandomizedSet() {
        int x = 0;
    }

    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    bool insert(int val) {
        if (wordmap.count(val)==0){
            order.push_back(val);
            wordmap[val] = order.size() - 1;
            return true;
        }
        else{
            return false;
        }

    }

    /** Removes a value from the set. Returns true if the set contained the specified element. */
    bool remove(int val) {
        if (wordmap.count(val)>0){
            if (wordmap[val] == order.size() - 1){
                wordmap.erase(val);
                order.pop_back();
            }
            else{
                int index = wordmap[val];
                order[index] = order[order.size() - 1];
                wordmap[order[index]] = index;
                order.pop_back();
                wordmap.erase(val);
            }
            return true;
        }
        else{
            return false;
        }
    }

    /** Get a random element from the set. */
    int getRandom() {
        if (order.size() > 0){
            int index = rand() % (order.size());
            return order[index];
        }
        else{
            return 0;
        }
    }
};

/**
* Your RandomizedSet object will be instantiated and called as such:

*/
int main(){
    cout << rand()%10 << endl;
    RandomizedSet obj;
    int val = 3;
    bool param_1 = obj.insert(val);
    bool param_2 = obj.remove(val);
    int param_3 = obj.getRandom();


    int xxx;
    cin >> xxx;
};

