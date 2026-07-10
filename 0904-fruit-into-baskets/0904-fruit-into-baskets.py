class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        left = 0
        fre = {}
        res = 0

        for high in range(n):
            fre[fruits[high]] = fre.get(fruits[high],0)+1
            #shrink if fruits exceed to 2
            while len(fre)>2:
                fre[fruits[left]]-=1
                if fre[fruits[left]]==0:
                    del fre[fruits[left]]
                left+=1
                    
            res = max(res,high-left+1)
        return res


        