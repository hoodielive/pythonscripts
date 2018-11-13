# Reverses the linked list without using recursion 
# head: first node in the original linked list
# Return value: the first node of the reversed linked list 

@staticmethod



def reverse(head):
    cur_node = head 
    prev_node = None 

    while (cur_node): 
        # Store the next node in a temporary variable 
        next_node = cur_node.next 

        # Reverse the link
        cur_node.next = prev_node

        # Update the previous node to the current node
        prev_node = cur_node

        # Proceed to the next node in the original linked list 
        cur_node = prev_node 
    
    # Once the linked list has been reversed, prev_node will be referring to the new head, so return it
    return prev_node

    reverse(head = ["A", "B", "C", "D", "E"]) 