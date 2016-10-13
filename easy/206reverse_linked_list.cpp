#include <iostream>
using namespace std;
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
 struct ListNode {
     int val;
     ListNode *next;
     ListNode(int x) : val(x), next(NULL) {}
 };
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode *prev, *cur, *tmp;
        cur = head;
        prev = NULL;
        while (cur!=NULL){
            tmp = cur->next;
            cur->next = prev;
            prev = cur;
            cur = tmp;
        };
        return prev;
    }
};
int main(){
};
