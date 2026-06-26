class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # s[:] = s[::-1]            #Shortcut = updating s[:] instead if return/print

        left = 0
        right= len(s) - 1
        while left<right:
            ''' 
            if left==right:
                break
                '''             #Ish line ki jarurat hi nahi h bcs loop(left<right)

            s[left], s[right] = s[right], s[left]
            left+=1
            right-=1
            
            '''temp = s[left]
            s[left] = s[right]          
            s[right] = temp   #We can also use this
            left+=1
            right-=1'''