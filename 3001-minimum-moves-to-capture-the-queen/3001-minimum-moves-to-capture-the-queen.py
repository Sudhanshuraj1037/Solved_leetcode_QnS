class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:

        # Rook
        if a == e:
            if not (c == a and min(b, f) < d < max(b, f)):
                return 1

        if b == f:
            if not (d == b and min(a, e) < c < max(a, e)):
                return 1

        # Bishop
        if abs(c - e) == abs(d - f):
            # Rook is not blocking the bishop
            if not (abs(a - c) == abs(b - d) and
                    min(c, e) < a < max(c, e) and
                    min(d, f) < b < max(d, f)):
                return 1

        return 2