class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original = image[sr][sc]

        # If the color is already the same, nothing to do
        if original == color:
            return image

        rows = len(image)
        cols = len(image[0])

        def dfs(r, c):
            # Outside the grid
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            # Not part of the original region
            if image[r][c] != original:
                return

            # Change color
            image[r][c] = color

            # Visit four directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)

        return image