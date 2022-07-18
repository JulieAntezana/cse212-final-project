from logging import root


class BST:
    """
    Implement the Binary Search Tree (BST) data structure.  The Node 
    class below is an inner class.  An inner class means that its real 
    name is related to the outer class.  To create a Node object, we will 
    need to specify BST.Node
    """

    class Node:
        """
        Each node of the BST will have data and links to the 
        left and right sub-tree. 
        """

        def __init__(self, data):
            """ 
            Initialize the node to the data provided.  Initially
            the links are unknown so they are set to None.
            """
       
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        """
        Initialize an empty BST.
        """
        self.root = None

    def insert(self, data):
        """
        Insert 'data' into the BST.  If the BST
        is empty, then set the root equal to the new 
        node.  Otherwise, use _insert to recursively
        find the location to insert.
        """
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)  # Start at the root

    def _insert(self, data, node):
        """
        This function will look for a place to insert a node
        with 'data' inside of it.  The current sub-tree is
        represented by 'node'.  This function is intended to be
        called the first time by the insert function.
        """

        if data == node.data:
            return
        elif data < node.data:
            # The data belongs on the left side.
            if node.left is None:
                # We found an empty spot
                node.left = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the left sub-tree.
                self._insert(data, node.left)
        else: 
            # The data belongs on the right side.
            if node.right is None:
                # We found an empty spot
                node.right = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the right sub-tree.
                self._insert(data, node.right)
  
    # ###################
    # # Example Problem #
    # ###################

    def get_height(self):
        """
        Determine the height of the BST.  Note that an empty tree
        will have a height of 0 and a tree with one item (root) will
        have a height of 1.
        
        If the tree is empty, then return 0.  Otherwise, call 
        _get_height on the root which will recursively determine the 
        height of the tree.
        """
        if self.root is None:
            return 0
        else:
            return self._get_height(self.root)  # Start at the root

    def _get_height(self, node):
        """
        Determine the height of the BST.  The height of a sub-tree 
        (represented by 'node') is 1 plus the height of either the 
        left sub-tree or the right sub-tree (whichever one is bigger).

        This function intended to be called the first time by 
        get_height.
        """
        # base case
        if node is None:
            return 0

        # Use recursion to get height of left side
        height_left = self._get_height(node.left)
        # Use recursion to get height of right side
        height_right = self._get_height(node.right)

        # Use max to determine which is greater height and add 1
        return 1 + max(height_left, height_right) 
            
    # ##################
    # Problem to Solve #
    # ##################

def create_bst_from_sorted_list(sorted_list):
    """
    Given a sorted list (sorted_list), create a balanced BST.  If 
    the values in the sorted_list were inserted in order from left
    to right into the BST, then it would resemble a linked list (unbalanced). 
    To get a balanced BST, the _insert_middle function is called to 
    find the middle item in the list to add first to the BST.  The 
    _insert_middle function takes the whole list but also takes a 
    range (first to last) to consider.  For the first call, the full 
    range of 0 to len()-1 used.
    """
    bst = BST()  # Create an empty BST to start with 
    _insert_middle(sorted_list, 0, len(sorted_list)-1, bst)
    return bst

def _insert_middle(sorted_list, first, last, bst):
    """
    This function will attempt to insert the item in the middle
    of 'sorted_list' into the 'bst' tree.  The middle is 
    determined by using indicies represented by 'first' and 'last'.
    For example, if the function was called on:

    sorted_list = [10, 20, 30, 40, 50, 60]
    first = 0
    last = 5

    then the value 30 (index 2 which is the middle) would be added 
    to the 'bst' (the insert function above can be used to do this).   

    Subsequent recursive calls are made to insert the middle from the values 
    before 30 and the values after 30.  If done correctly, the order
    in which values are added (which results in a balanced bst) will be:

    30, 10, 20, 50, 40, 60

    This function is intended to be called the first time by 
    create_bst_from_sorted_list.

    The purpose for having the first and last parameters is so that we do 
    not need to create new sublists when we make recursive calls.  Avoid 
    using list slicing to create sublists to solve this problem.
    """
    # Check base case
    if first > last:
        return bst
    
    # Find the middle element of the sorted list
    middle = (first + last) // 2
    
    # Insert the middle element of the sorted list into the bst
    bst.insert(sorted_list[middle])

    # Create a new node from the middle element
    node = BST.Node(sorted_list[middle])
    
    # Wrap the recursion into an if statement to prevent max recursions 
    if middle > first:
        # Use recursion to continue inserting higher values on the left
        node.left = _insert_middle(sorted_list, first, middle - 1, bst)

    # Wrap the recursion into an if statement to prevent max recursions
    if middle < last:
        # Use recursion to continue inserting lower values on the right
        node.right = _insert_middle(sorted_list, middle + 1, last, bst)
    
    return root


print("\n=========== TESTS FOR PROBLEM TO SOLVE ===========")
tree1 = create_bst_from_sorted_list([10, 20, 30, 40, 50, 60])
tree2 = create_bst_from_sorted_list([x for x in range(127)]) # 2^7 - 1 nodes
tree3 = create_bst_from_sorted_list([x for x in range(128)]) # 2^7 nodes
tree4 = create_bst_from_sorted_list([42])
tree5 = create_bst_from_sorted_list([])
print(tree1.get_height()) # 3
print(tree2.get_height()) # 7 .. any higher and its not balanced
print(tree3.get_height()) # 8 .. any higher and its not balanced
print(tree4.get_height()) # 1
print(tree5.get_height()) # 0



