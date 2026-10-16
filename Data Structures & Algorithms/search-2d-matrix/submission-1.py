class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end  = len(matrix[0])-1 # length of row :3

        for row in range(len(matrix)):
            start = 0
            end  = len(matrix[0])-1
            mid = (start + end) // 2
            while(start<=end):
                mid = (start + end) // 2
                print(mid, row)
                if matrix[row][mid] < target:
                    start = mid + 1
                elif matrix[row][mid] == target:
                    return True
                else:
                    end = mid - 1
        return False


        