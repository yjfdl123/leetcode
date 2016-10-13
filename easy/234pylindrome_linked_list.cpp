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
    bool isPalindrome(ListNode* head) {
        ListNode* prev,*node,*reverse;
        prev=NULL;
        node=head;
        while (node!=NULL){
            ListNode* newnode=new ListNode(node->val);
            newnode->next=prev;
            prev=newnode;
            node=node->next;
        }; 
        reverse=prev;
        ListNode* renode=reverse;
        node=head;
        while (node!=NULL){
            if (node->val!=renode->val){
                return false;
            }else{
                node=node->next;
                renode=renode->next;
            };
        };
        return true;
                
    }
};
int main(){
    cout<<123<<endl;
};
