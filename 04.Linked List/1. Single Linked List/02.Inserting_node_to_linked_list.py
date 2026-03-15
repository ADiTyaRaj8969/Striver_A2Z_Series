# Node insertAtBegining(Node head, int x) {
# Node temp = new Node(x);
# Function to insert a node at the end of the linked list.
# Node insertAtEnd(Node head, int x)  {
# Node curr = head;
# TODO: Add test cases
# Read the examples in the comments above and create appropriate test cases

Node *insertAtBegining(Node *head, int x) if(head==NULL) return new Node(x) Node* temp = new Node(x) temp->next = head return temp 

# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)
```
