"""
Auxiliary Given a singly linked list, find the middle of the linked list. 
For example, if the given linked list is 1->2->3->4->5 then the output should be 3. 
If there are even nodes, then there would be two middle nodes, we need to print the second middle element. 
For example, if the given linked list is 1->2->3->4->5->6 then the output should be 4.
"""

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class NodeOperation:
    def pushNode(self, head_ref, data_val):
        new_node = Node(data=data_val)
        new_node.next = head_ref[0]
        head_ref[0] = new_node

if __name__ == "__main__":
    head = [None]
    temp = NodeOperation()
    for i in range(5, 0, -1):
        temp.pushNode(head, i)
    
    v = []
    while(head[0]):
        v.append(head[0].data)
        head[0] = head[0].next
    for i in v:
        print(i)
    print("Middle Value Of Linked List is :", v[len(v)//2])
