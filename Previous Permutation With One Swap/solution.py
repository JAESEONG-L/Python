class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:

        min_num=arr[len(arr)-1]

        for i in range(len(arr)-2, -1, -1):
            if arr[i]>min_num:
                jdx=-1

                for j in range(i+1, len(arr)):
                    if arr[j]<arr[i] and (jdx==-1 or arr[j]>arr[jdx]):
                        jdx= j

                (arr[i], arr[jdx]) = (arr[jdx], arr[i])

                break

            min_num= min(min_num, arr[i])

        return arr
