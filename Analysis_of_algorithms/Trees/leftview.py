from os import *
from sys import *
from collections import *
from math import *

# Binary tree node class for reference
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def getLeftView(root)->list:
    # Write your code here
    # Return a list
    if root is None: return []
    que=deque([root])
    res=[]
    while que:
        n=len(que)
        for i in range(n):
            node=que.popleft()
            if i==0:
                res.append(int(node.data))
            if node.left is not None: que.append(node.left)
            if node.right is not None: que.append(node.right)
    return res

    pass
def build_tree(values):
  if not values:
      return None
  root = BinaryTreeNode(values[0])
  queue = deque([root])
  index = 1
  while queue and index < len(values):
      node = queue.popleft()
      if values[index] is not None:
          node.left = BinaryTreeNode(values[index])
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          node.right = BinaryTreeNode(values[index])
          queue.append(node.right)
      index += 1
  return root


# Test cases
test_cases = [
  ([], []),  # Test Case 1
  ([1], [1]),  # Test Case 2
  ([1, 2, None, 3, None, 4], [1, 2, 3, 4]),  # Test Case 3
  ([1, None, 2, None, 3, None, 4], [1, 2, 3, 4]),  # Test Case 4
  ([1, 2, 3, 4, 5, None, 6], [1, 2, 4]),  # Test Case 5
  ([1, 2, 3, 4, 5, 6, 7], [1, 2, 4]),  # Test Case 6
  ([1, 2, 3, 4, 5], [1, 2, 4]),  # Test Case 7
  ([1, None, 2, 3, 4], [1, 2, 3]),  # Test Case 8
  ([1, 2, 3, None, 4], [1, 2, 4]),  # Test Case 9
]

# Run test cases
for i, (tree_values, expected) in enumerate(test_cases):
  root = build_tree(tree_values)
  result = getLeftView(root)
  assert result == expected, f"Test case {i+1} failed: expected {expected} but got {result}"
  print(f"Test case {i+1} passed: {result}")
