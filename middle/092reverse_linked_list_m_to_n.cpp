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
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        ListNode* node=head;
        ListNode *m_node=NULL,*n_node=NULL;
        ListNode *m_pre_node=head;
        ListNode *n_bac_node=NULL;
        ListNode * prev_node = NULL;
        int length = 0;
        while (node != NULL){
            length++;
            if (length == m ){
                m_pre_node = prev_node;
                m_node = node;
            };
            if (length == n){
                n_node = node;
                n_bac_node = node->next;
            };
            prev_node = node;
            node = node->next;
        };
        if (m<1) m=1;
        if (n>length) n=length;
        if (n<=m) return head;
        ListNode * cur=m_node;
        ListNode * prev=NULL, *nextnode=NULL;
        while (cur!=n_bac_node){
            nextnode = cur->next;
            cur->next=prev;
            prev = cur;
            cur=nextnode;    
        };
        m_node->next=n_bac_node;
        if (m==1){
            head=n_node;
        }else{
            m_pre_node->next=n_node;
        };
        return head;
    }
};
int main(){
};
