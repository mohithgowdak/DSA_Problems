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

    def sumofnodes(self,root:Optional[TreeNode])->int:
        if root is None:
            return 0
        return self.sumofnodes(root.left) + self.sumofnodes(root.right)+root.data

    def heightofNodes(self,root:Optional[TreeNode])->int:
        if root is None:
            return 0
        return max(self.heightofNodes(root.left),self.heightofNodes(root.right))+1

    def diameterOfTree_n2(self,root:Optional[TreeNode])->int:
        if root is None:
            return 0
        x=self.heightofNodes(root.right)
        y=self.heightofNodes(root.left)
        return max(x+y+1, self.diameterOfTree_n2(root.left), self.diameterOfTree_n2(root.right))
    class TreeInfo:
        def __init__(self, diameter, height):
            self.d = diameter
            self.h = height

    def diameterOfTree_n(self, root: Optional[TreeNode]) -> Optional[TreeInfo]:
        if root is None:
            return self.TreeInfo(0, 0)

        left = self.diameterOfTree_n(root.left)
        right = self.diameterOfTree_n(root.right)

        currentHeight = max(left.h, right.h) + 1
        currentDiameter = max(left.d, right.d, left.h + right.h + 1)

        return self.TreeInfo(currentDiameter, currentHeight)
    
    
    '''def ismatch(self, root: Optional[TreeNode],subroot:Optional[TreeNode]) -> bool:
        if not(root and subroot): return True
        if not(root or subroot): return False
        return self.ismatch(root.right,subroot.right) and self.ismatch(root.left,subroot.right)

    def issubtree(self, root: Optional[TreeNode],subroot:Optional[TreeNode]) -> bool:
        if not subroot: return None
        if not root: return False
        if root.data == subroot.data:
            if self.ismatch(root,subroot):
                return True
        return self.issubtree(root.left,subroot) or self.issubtree(root.right,subroot)'''


# Move the main function outside the Tree class
def main():
    nodes = [1, 2, 4, -1, -1, 5, -1, -1, 3, -1, 6, -1, -1]
    tree = Tree()
    root = tree.buildTree(nodes)
   # subtree=Tree()
   # root2=subtree.buildTree([1,2,3])
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
    print("\nsum of nodes")
    print(tree.sumofnodes(root))
    print("\nheight of nodes")
    print(tree.heightofNodes(root))
    print("\ndiameter of nodes(n^2)")
    print(tree.diameterOfTree_n2(root))
    print("\ndiameter of nodes(n)")
    print((tree.diameterOfTree_n(root)).d)


if __name__ == "__main__":
    main()
