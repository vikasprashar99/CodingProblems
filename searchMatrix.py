# Search element in Sorted Matrix
# using two pointers

def searchMatrix():
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    
    
    row, col = 0, len(matrix[0]) - 1
            
    while row < len(matrix) and col >= 0:
        if matrix[row][col] == target:
            
            print("true")
            break
        elif matrix[row][col] < target: row += 1
        elif matrix[row][col] > target: col -= 1
        
