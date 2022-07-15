# LinkedList class
class LinkedList:

  # This function intializes the LinkedList object.
  def __init__(self):
    self.head = None

  # This function traverses the linked list and prints the data, starting with the head
  def printLinkedList(self):
    pll = self.head
    while (pll):
      print(pll.data)
      pll = pll.next
    

class Node:
  # This function initalizes the Node object.
  def __init__(self, data):
    self.data = data # The node will contain data
    self.next = None # The pointer to next is initialized as null.

  

# We will begin by creating a linked list with three nodes.

# Begin to execute code:
if __name__=='__main__':

  # Assign an empty linked list
  newlist = LinkedList()

  # Create the nodes
  newlist.head = Node(1)
  newlist.n2 = Node(2)
  newlist.n3 = Node(3)

  # Link the first two nodes by setting the pointer on the head, which is called "next,"" to point to node 2 (n2) 
  newlist.head.next = newlist.n2

  # Link the next two nodes
  newlist.n2.next = newlist.n3

  newlist.printLinkedList()