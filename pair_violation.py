class Solution:
    def pairsViolatingBST(self, n : int, root : Optional['Node']) -> int:
        # code here
        inorder = []
        
        def INORDER(root):
            if not root:
                return 
            INORDER(root.left)
            inorder.append(root.data)
            INORDER(root.right)
            
        INORDER(root)
        if len(inorder) <=1:
            return 0
        
        pq = []
        for i, val in enumerate(inorder):
            pq.append((val, i))
        pq.sort()
                
        ans = 0
        x = []
        while pq:
            val, i = pq.pop(0)
            cnt = bisect_right(x, i)
            ans +=i-cnt
            x.insert(cnt, i)
        
        return ans  
