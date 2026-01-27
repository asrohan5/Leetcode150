class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None: return root
        q = [root]
        while q:
            n = len(q)
            pre = None
            for i in range(n):
                cur = q[i]
                if pre:
                    pre.next = cur
                pre = cur
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            q = q[n:]
        return root
