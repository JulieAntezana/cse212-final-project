





    def __iter__(self):
        # This function will iterate forward through a linked list.
        curr = self.head  # Start at the begining to go forward
        while curr is not None:
            yield curr.data  # Provide (yield) each item to the user
            curr = curr.next # Go forward in the linked list

    def __reversed__(self):
        This function will iterate backward through a linked list

        curr = self.tail  # Start at the tail to go backward.
        while curr is not None:
            yield curr.data  # Provide (yield) each item to the user
            curr = curr.prev # Go backward in the linked list

# To test the __reversed__ function, you can use the following code:
for item in reversed(my_linkedlist):
  print(item)
# Another option:
print(list(reversed(my_linkedlist)))