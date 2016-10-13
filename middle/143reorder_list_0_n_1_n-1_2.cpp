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
    void reorderList(ListNode* head) {
        if (head == NULL) return;
        ListNode *slow = head;
        ListNode *fast = head;
        ListNode *prev = NULL;
        while (fast != NULL){
            prev = slow;
            slow = slow->next;
            fast = fast->next;
            if (fast != NULL)  fast = fast->next;
        };
        prev->next = NULL;
        ListNode * back_head = slow;
        ListNode * back_prev = NULL;
        ListNode * back_node = back_head;
        ListNode * back_next = NULL;
        while (back_node != NULL){
            back_next = back_node->next;
            back_node->next = back_prev;
            back_prev = back_node;
            back_node = back_next;
        };
        back_head = back_prev;
        ListNode *prev_node = head;
        back_node = back_head;
        ListNode * node = head->next;
        ListNode * tmp = NULL;
        while (node!= NULL){
            tmp = back_node->next;
            prev_node->next = back_node;
            back_node->next = node;
            back_node = tmp;
            prev_node = node;
            node = node->next;
        };
        if (back_node != NULL) prev_node->next = back_node;
    }
};
int main(){
};
