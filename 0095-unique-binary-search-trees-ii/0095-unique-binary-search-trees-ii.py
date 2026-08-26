class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        def build(start, end):
            if start > end:
                return [None]

            result = []

            # Try every value as the root
            for root_val in range(start, end + 1):

                left_trees = build(start, root_val - 1)
                right_trees = build(root_val + 1, end)

                # Combine every left tree with every right tree
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(root_val)
                        root.left = left
                        root.right = right
                        result.append(root)

            return result

        return build(1, n)