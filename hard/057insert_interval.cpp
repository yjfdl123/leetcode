#include "cpphelp.cpp"
/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
struct Interval {
    int start;
    int end;
    Interval() : start(0), end(0) {}
    Interval(int s, int e) : start(s), end(e) {}
};
class Solution {
public:
    vector<Interval> insert(vector<Interval>& intervals, Interval newInterval) {
        vector<Interval> ret;
        int start=0,len=intervals.size();
        while ((start<len) && (intervals[start].end<newInterval.start)){
            ret.push_back(intervals[start++]);
        };
        ret.push_back(newInterval);
        int last=ret.size()-1;
        while ( (start<len) && (intervals[start].start<=ret[last].end)){
            ret[last].start= min(ret[last].min, intervals[start].start);
            ret[last].end = max( ret[last].end, intervals[start++].end);
        };
        while (start<len){
            ret.push_back(intervals[start++]);
        };
        return ret;
        
        
    }
};
int main(){
};
