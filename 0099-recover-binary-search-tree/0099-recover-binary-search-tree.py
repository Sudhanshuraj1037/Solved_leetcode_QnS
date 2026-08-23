class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first = None
        second = None
        prev = None

        def inorder(node):
            nonlocal first, second, prev

            if not node:
                return

            inorder(node.left)

            # Found an inversion
            if prev and prev.val > node.val:
                if first is None:
                    first = prev

                second = node

            prev = node

            inorder(node.right)

        inorder(root)

        # Swap the incorrect values
        first.val, second.val = second.val, first.val