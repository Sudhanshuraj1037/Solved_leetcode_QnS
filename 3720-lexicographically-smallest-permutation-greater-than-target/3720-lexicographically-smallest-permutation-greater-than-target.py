class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        n = len(s)

        for i in range(n - 1, -1, -1):
            # Try to match target[0:i]
            # Rebuild the character counts for this prefix.
            if i == n:
                continue

            # At position i, we want the smallest character
            # greater than target[i].
            prefix_count = count[:]

            # Remove characters used by target[0:i]
            possible = True

            for j in range(i):
                idx = ord(target[j]) - ord('a')
                if prefix_count[idx] == 0:
                    possible = False
                    break
                prefix_count[idx] -= 1

            if not possible:
                continue

            target_idx = ord(target[i]) - ord('a')

            # Find the smallest available character > target[i]
            for c in range(target_idx + 1, 26):
                if prefix_count[c] > 0:
                    prefix_count[c] -= 1

                    result = target[:i] + chr(c + ord('a'))

                    # Append remaining characters in sorted order
                    for x in range(26):
                        result += chr(x + ord('a')) * prefix_count[x]

                    return result

        return ""