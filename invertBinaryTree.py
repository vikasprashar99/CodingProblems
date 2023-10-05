class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_tree(root):
    if root is None:
        return None
    
    # Swap the left and right subtrees of the current node
    root.left, root.right = root.right, root.left
    
    # Recursively invert the left and right subtrees
    invert_tree(root.left)
    invert_tree(root.right)
    
    return root

# Helper function to print the binary tree (for visualization)
def print_tree(root):
    if root is None:
        return
    print(root.val, end=" -> ")
    print_tree(root.left)
    print_tree(root.right)

def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print("Original Tree:")
    print_tree(root)
    print("\nInverted Tree:")
    inverted_root = invert_tree(root)
    print_tree(inverted_root)

main();