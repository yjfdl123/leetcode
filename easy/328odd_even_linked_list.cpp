#include<iostream>
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
    ListNode* oddEvenList(ListNode* head) {
        ListNode *oddhead, *oddnode, *evenhead, *evennode, *nextnode;
        oddhead=NULL;
        evenhead=NULL;
        int count=1;
        while (head!=NULL){
            nextnode = head->next;            
            if (count%2==0){
                if (evenhead==NULL){
                    evenhead=head;
                    evennode=head;
                }else{
                    evennode->next=head;
                    evennode = head;
                };
                evennode->next=NULL;
            }else{
                if (oddhead==NULL){
                    oddhead = head;
                    oddnode = head;
                }else{
                    oddnode->next = head;
                    oddnode = head;
                };
                oddnode->next = NULL;
            };
            head = nextnode;
            count++;
        };
        if (oddhead==NULL){
            return evenhead;
        }else{
            oddnode->next = evenhead;
            return oddhead;
        }
    }
};
int main(){
}
