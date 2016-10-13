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
    ListNode* insertionSortList(ListNode* head) {
        if (head==NULL) return head;
        ListNode *insert_node = head->next;
        ListNode *insert_prev = head;
        ListNode *insert_back = NULL;
        ListNode *prev = NULL;
        ListNode *node = head;
        ListNode *iter = head;
        while (insert_node!=NULL){
            insert_back = insert_node->next;
            iter=head;
            prev=NULL;
            while ((insert_node->val > iter->val) and (iter!=insert_node)){
                prev = iter;
                iter=iter->next;
            };
            if (iter==head){
                insert_node->next=head;
                head=insert_node;
                insert_prev->next=insert_back;
            }else if(iter==insert_node){
                insert_prev = insert_node;
            }else{
                insert_prev->next=insert_back;
                insert_node->next=iter;
                prev->next=insert_node;
            };
            insert_node = insert_back;
        };
        return head;
    }
};
int main(){
};
