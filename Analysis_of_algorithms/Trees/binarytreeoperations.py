from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None


class Tree:  # This class contains all the methods for tree operations
    idx = -1

    def buildTree(self, nodes: list) -> Optional[TreeNode]:
        self.idx += 1
        if nodes[self.idx] == -1:
            return None
        newNode = TreeNode(nodes[self.idx])
        newNode.left = self.buildTree(nodes)
        newNode.right = self.buildTree(nodes)
        return newNode

    def preordertraversal(self, root: Optional[TreeNode]):
        if root is None:
            return
        print(root.data, end=" ")
        self.preordertraversal(root.left)
        self.preordertraversal(root.right)
    
    def inordertraversal(self, root: Optional[TreeNode]):
        if root is None:
            return
        self.inordertraversal(root.left)
        print(root.data, end=" ")
        self.inordertraversal(root.right)

    def postordertraversal(self, root: Optional[TreeNode]):
        if root is None:
            return
        self.postordertraversal(root.left)
        self.postordertraversal(root.right)
        print(root.data, end=" ")

    def levelordertraversal(self, root: Optional[TreeNode]):
        if root is None:
            return
        queue = deque([root,None])
       
        while queue:
            node = queue.popleft()
            if node is None:
                print()
                if not queue:
                    break
                else:
                    queue.append(None)
            else:
                print(node.data,end=" ")
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

    def countofNodes(self,root:Optional[TreeNode])->int:
        if root is None:
            return 0
        return self.countofNodes(root.left) + self.countofNodes(root.right)+1


# Move the main function outside the Tree class
def main():
    nodes = [1, 2, 4, -1, -1, 5, -1, -1, 3, -1, 6, -1, -1]
    tree = Tree()
    root = tree.buildTree(nodes)
    print("Preorder Traversal: ", end="")
    tree.preordertraversal(root)
    print("\nInorder Traversal: ", end="")
    tree.inordertraversal(root)
    print("\nPostorder Traversal: ", end="")
    tree.postordertraversal(root)
    print("\nLevel-order Traversal: ")
    tree.levelordertraversal(root)
    print("\nCount of nodes")
    print(tree.countofNodes(root))

if __name__ == "__main__":
    main()
