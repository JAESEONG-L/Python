class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        count=1

        while 26*(26**count-1)//25<columnNumber:
            count += 1

        columnNumber -= 26*(26**(count-1)-1)//25


        column_title=chr(65+(columnNumber-1)//(26**(count-1)))

        columnNumber -= 26**(count-1)*((columnNumber-1)//(26**(count-1)))

        for i in range(count-1, 0, -1):
            column_title += chr(65+(columnNumber-1)//(26**(i-1)))

            columnNumber -= 26**(i-1)*((columnNumber-1)//(26**(i-1)))

        return column_title
