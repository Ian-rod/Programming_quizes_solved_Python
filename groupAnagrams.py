from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        compList=[]
        retList: List[List[str]] = []
        for s in strs:
            sortedS=sorted(s)
            if(compList.__contains__(sortedS)):
                index=compList.index(sortedS)
                retList[index].append(s)
            else:
                compList.append(sortedS)
                retList.append([s])
            print(sortedS)

        return retList

mySolution=Solution()
print(mySolution.groupAnagrams([""]))
