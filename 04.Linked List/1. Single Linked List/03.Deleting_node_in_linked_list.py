# Node deleteNode(Node head,int x)
# Node curr = head;
# TODO: Extract test cases from the examples above
# Call your function: deleteNode()
# Print linked list/tree (implement a helper function)

Node* deleteNode(Node *head,int x) if(x==1) return head->next cnt = 1 Node* curr = head while(cnt<x-1) cnt++ curr = curr->next curr->next = curr->next->next return head

# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(H)
```
