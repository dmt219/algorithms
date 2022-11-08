class TreeNode:
  def __init__(self, item, left, right):
    self.item = item
    self.left = left
    self.right = right

class BinarySearchTree:
  def __init__(self, head):
    self.head = head

  def search(self, item): # O(h)
    if (self.head == None):
      return

    if (item == self.head.item):
      return self.head
    elif (item < self.head.item):
      tree = BinarySearchTree(self.head.left)
      return tree.search(item)
    elif (item > self.head.item):
      tree = BinarySearchTree(self.head.right)
      return tree.search(item)

  def find_min(self): # O(h)
    _min = self.head
    while(_min.left != None):
      _min = _min.left
    return _min

  def inorder_traversal(self, arr = []): # O(n)
    head = self.head
    if (head.left != None):
      leftTree = BinarySearchTree(head.left)
      leftTree.inorder_traversal(arr)
    arr.append(self.head.item)
    if (head.right != None):
      rightTree = BinarySearchTree(head.right)
      rightTree.inorder_traversal(arr)
    return arr

  def insert_tree(self, item, parent): # O(h)
    head = self.head

    if head == None:
      newNode = TreeNode(item, None, None)
      if parent.item < item:
        parent.right = newNode
      else:
        parent.left = newNode
      return

    if item == head.item:
      return None

    if item < head.item:
      leftTree = BinarySearchTree(head.left)
      return leftTree.insert_tree(item, head)
    elif item > head.item:
      rightTree = BinarySearchTree(head.right)
      return rightTree.insert_tree(item, head)

  def delete_tree():
    pass
    # TBI
    # 3 cases:
    # - Node with no child: simply delete the node - O(h)
    # - Node with 1 child: link the child with the node's parent - O(h)
    # - Node with 2 children: relabel the node with the smallest item of the
    # right substree, i.e. the left-most item of the right subtree. This item
    # has at most one child (i.e. a right child) => total operation takes at
    # most 2 searches, each of O(h)
  
if __name__ == '__main__':
  leftLeaf = TreeNode(1, None, None)
  rightLeaf = TreeNode(3, None, None)
  headNode = TreeNode(2, leftLeaf, rightLeaf)
  tree = BinarySearchTree(headNode)
  assert(tree.head.left == leftLeaf)
  assert(tree.head.right == rightLeaf)
  assert(tree.search(1) == leftLeaf)
  assert(tree.find_min().item == 1)
  assert(tree.inorder_traversal([]) == [1, 2, 3])
  tree.insert_tree(7, None)
  tree.insert_tree(5, None)
  tree.insert_tree(4, None)
  tree.insert_tree(6, None)
  assert(tree.inorder_traversal([]) == [1, 2, 3, 4, 5, 6, 7])

  
# Analysis: operations usually take O(h) time where h is the height of the
# tree. For balanced binary search tree, h is logN, but whether it's balanced
# or not depending on the order of insertion
