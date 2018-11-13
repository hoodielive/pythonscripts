@staticmethod 
def reverse(head):
    cur_node = head
    prev_node = None 

    while (cur_node):
        # Store next node in a temporary variable
        next_node = cur_node.next 

        # Reverse the link 
        cur_node.next = prev_node 

        # Update the previous node to the current node 
        prev_node = cur_node 

        # Proceed to the next node in the original linked list
        cur_node = next_node 

    # Once the linked list has been reversed, prev_node will be
    # Referring to the new head. So return it:
    return prev_node 

reverse(10)
