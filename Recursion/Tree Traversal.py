from ..Trees.Trees import TreeNode

def Traversal(root: TreeNode) -> List[int]:
    if not root:
        return []
    return Traversal(root.left) + [root.val] + Traversal(root.right)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print(Traversal(root)) # [4, 2, 5, 1, 3]
    