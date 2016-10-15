#include "cpphelp.cpp"
class MedianFinder {
private:
    priority_queue<int, vector<int>, greater<int> > minque;
    priority_queue<int> maxque;
public:

    // Adds a number into the data structure.
    void addNum(int num) {
        if (minque.size()+maxque.size()<2) {
            minque.push(num);
        }else if (num>=minque.top()){
            minque.push(num);
        }else if (num<=maxque.top()){
            maxque.push(num);
        }else if (minque.top()-num<=num-maxque.top()){
            minque.push(num); 
        }else{
            maxque.push(num);
        };
        if (minque.size() -maxque.size()==2){
            maxque.push(minque.top());
            minque.pop();
        }else if (maxque.size()-minque.size()==2){
            minque.push(maxque.top());
            maxque.pop(); 
        };
    }

    // Returns the median of current data stream
    double findMedian() {
        if ( minque.size()+maxque.size()==0) return 0.0;
        if ( minque.size()==maxque.size()){
            return double(minque.top()+maxque.top())/2;
        }else if (minque.size()<maxque.size()){
            return maxque.top();
        }else if (minque.size()>maxque.size()){
            return minque.top();
        };
        return 0.0;

    }
};

// Your MedianFinder object will be instantiated and called as such:
int main(){
 MedianFinder mf;
 mf.addNum(1);
 cout<<mf.findMedian();
};
