#include "cpphelp.cpp"
/**
 * Definition for singly-linked list with a random pointer.
 * struct RandomListNode {
 *     int label;
 *     RandomListNode *next, *random;
 *     RandomListNode(int x) : label(x), next(NULL), random(NULL) {}
 * };
 */
struct RandomListNode {
    int label;
    RandomListNode *next, *random;
    RandomListNode(int x) : label(x), next(NULL), random(NULL) {}
};
class Solution {
public:
    RandomListNode *copyRandomList(RandomListNode *head) {
        if (head==NULL) return head;
        RandomListNode *node=head;
        RandomListNode *next=NULL;
        while (node!=NULL){
            next=node->next;
            RandomListNode* newnode=new RandomListNode(node->label); 
            node->next=newnode;
            newnode->next=next;
            node=next;
        } 
        node = head;
        RandomListNode *random,*randomnext;
        while (node!=NULL){
            next=node->next;
            if (node->random!=NULL){
                random = node->random;
                randomnext = random->next;
                next->random = randomnext;
            }
            node=next->next;
        };
        node=head;
        RandomListNode* ret=head->next;
        RandomListNode* retnode=head->next;
        while (node!=NULL){
            retnode=node->next;
            node->next=retnode->next;
            node=node->next;
            if (node!=NULL) retnode->next=node->next;
        }
        return ret;
    }
};
int main(){
};
