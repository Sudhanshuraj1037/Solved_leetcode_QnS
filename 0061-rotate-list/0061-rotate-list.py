class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head

        # Find length and last node
        n = 1
        tail = head

        while tail.next:
            tail = tail.next
            n += 1

        # Avoid unnecessary rotations
        k %= n
        if k == 0:
            return head

        # Make the list circular
        tail.next = head

        # Find the new tail
        steps = n - k
        new_tail = head

        for _ in range(steps - 1):
            new_tail = new_tail.next

        # Break the circle
        new_head = new_tail.next
        new_tail.next = None

        return new_head