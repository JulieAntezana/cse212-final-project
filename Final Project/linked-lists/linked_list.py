class LinkedList:

    class Node:
      # This function initializes the node object 
        def __init__(self, data):
            self.data = data # The node will contain data
            self.next = None # The pointer to next is initialized as null.
            self.prev = None # The pointer to prev is initialized as null.
          
    def __init__(self):
        # This function initializes an empty linked list.
        self.head = None
        self.tail = None
    def insert_head(self, value):
        # This function will insert a new node at the head of the linked list.
        # Create the new node
        new_node = LinkedList.Node(value)  
        
        # If the list is empty, then point both head and tail
        # to the new node.
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # If the list is not empty, then only connect self.head
        else:
            new_node.next = self.head # Connect new node to the previous head
            self.head.prev = new_node # Connect the previous head to the new node
            self.head = new_node      # Set the head to equal the new node

    def insert_tail(self, value):
        # Insert a new node at the tail end of the linked list.
          
        # Create the new node
        new_node = LinkedList.Node(value)  
        
        # If the list is empty, then point both tail and tail
        # to the new node.
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        # If the list is not empty, then only connect self.tail
        else:
            new_node.prev = self.tail # Connect the previous tail to the new node
            self.tail.next = new_node # Connect new node to the previous tail
            self.tail = new_node      # Update the tail to point to the new node

    
    def insert_after(self, value, new_value):
        # This function will insert into the middle of a linked list by adding a 
        # 'new_value' after the first occurance of 'value' in the linked list.

        # Search for the node that matches 'value' by starting at the 
        # head of the list.
        curr = self.head
        while curr is not None:
            if curr.data == value:
                # If the location of 'value' is at the end of the list,
                # then we can call insert_tail to add 'new_value'
                if curr == self.tail:
                    self.insert_tail(new_value)
                # For any other location of 'value', we need to create a 
                # new node and reconnect the links to insert.
                else:
                    new_node = LinkedList.Node(new_value)
                    new_node.prev = curr       # Connect new node to the node containing 'value'
                    new_node.next = curr.next  # Connect new node to the node after 'value'
                    curr.next.prev = new_node  # Connect node after 'value' to the new node
                    curr.next = new_node       # Connect the node containing 'value' to the new node
                return # We can exit the function after we insert
            curr = curr.next # Go to the next node to search for 'value'

    def remove_head(self):
        # This function will remove the head from the linked list
      
        # If the list has only one item in it, then set head and tail 
        # to None resulting in an empty list.  This condition will also
        # cover an empty list.  Its okay to set to None again.
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # If the list has more than one item in it, then only self.head
        # will be affected.
        elif self.head is not None:
            self.head.next.prev = None  # Disconnect the second node from the first node
            self.head = self.head.next  # Update the head to point to the second node
          
    def remove_tail(self):
        # This function will remove the tail end from the linked list.
    
        # If the list has only one item in it, then set head and tail 
        # to None resulting in an empty list.  This condition will also
        # cover an empty list.  Its okay to set to None again.
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # If the list has more than one item in it, then only self.tail
        # will be affected.
        elif self.head is not None:
            self.tail.prev.next = None  # Set the "next" of the second to last node to nothing
            self.tail = self.tail.prev  # Set the tail to be the second to last node

    def remove(self, value):
        # This function will remove the first node that contains 'value'.
        
        # Search for the node that matches 'value' by starting at the 
        # head of the list.
        curr = self.head
        # Loop until we have reached the end (None)
        while curr is not None:
            if curr.data == value:
                if curr == self.head:
                    self.remove_head()
                    return
                elif curr == self.tail:
                    self.remove_tail()
                    return                      
                else:
                    # Set the prev of the node after curr to the node before curr 
                    curr.next.prev = curr.prev
                    # Set the next of the node before curr to the node after curr 
                    curr.prev.next = curr.next 
                    curr = None
                    return
            # Follow the pointer to the next node
            curr = curr.next        
        # if value was not present in linked list
        if(curr == None):
            return

    #This function will search for all nodes that are equal to 'old_value' and replace them with 'new_value'
    def replace(self, old_value, new_value):
        """
        Search for all instances of 'old_value' and replace the value 
        to 'new_value'.
        """
        # Search for the node that matches 'old_value' by starting at the 
        # head of the list.
        curr = self.head
        # Loop until we have reached the end (None)
        while curr is not None:
            # Replace the current value in the node with the new value
            if curr.data == old_value:
                curr.data = new_value
            else:
                # Follow the pointer to the next node
                curr = curr.next
    def __str__(self):
        # This function will assist us in testing our code by returning a string representation of the linked list.
        output = "linkedlist["
        first = True
        for value in self:
            if first:
                first = False
            else:
                output += ", "
            output += str(value)
        output += "]"
        return output

    def __iter__(self):
        # This function will iterate forward through a linked list.
        curr = self.head  # Start at the begining to go forward
        while curr is not None:
            yield curr.data  # Provide (yield) each item to the user
            curr = curr.next # Go forward in the linked list

    def __reversed__(self):
        # This function will iterate backward through a linked list

        curr = self.tail  # Start at the tail to go backward.
        while curr is not None:
            yield curr.data  # Provide (yield) each item to the user
            curr = curr.prev # Go backward in the linked list

# Sample test cases for the Example Problem as "linkedlist[expected results]":
ll = LinkedList()
ll.insert_tail(1)
ll.insert_head(2)
ll.insert_head(2)
ll.insert_head(2)
ll.insert_head(3)
ll.insert_head(4)
ll.insert_head(5)
print(ll) # linkedlist[5, 4, 3, 2, 2, 2, 1]
ll.replace(1, 2)
print(ll) # linkedlist[5, 4, 3, 2, 2, 2, 2]
ll.replace(2, 1)
print(ll) # linkedlist[5, 4, 3, 1, 1, 1, 1]

# Sample test case for the Problem to Solve:
print(list(reversed(ll)))  # [1, 1, 1, 1, 3, 4, 5]