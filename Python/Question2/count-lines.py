'''
Time Complexity - O(n*2)
Space Complexity - O(1)
'''

def count_lines(arr:list[list]) -> int | str:

    rows = len(arr)
    cols = len(arr[0])

    line_count = 0

    left, right, top, bottom = 0, 0, 0, 0
    
    #As we traverse through the 2D, columnwise ➡️ and rowwise ⬇️, the left and top of an array element is its history and right and bottom is its future. 
    for row in range(rows):
        for col in range(cols):
            if arr[row][col] == 'X':
                if (col != 0 and arr[row][col - 1] == 'X'): #there is an X present to left of element
                    left = 1
                if (col != cols - 1 and arr[row][col + 1] == 'X'): #there is an X present to right of element
                    right = 1
                if (row != 0 and arr[row - 1][col] == 'X'): #there is an X present to top of element
                    top = 1
                if (row != rows - 1 and arr[row + 1][col] == 'X'): #there is an X present to bottom of element
                    bottom = 1
                
                if top == 1 and bottom == 1 and left == 0 and right == 0: 
                    bottom = 0

                if top == 0 and bottom == 0 and left == 1 and right == 1:
                    left,right = 0,0
    
                if ((left + right + top + bottom) > 1):
                    return 'invalid'

                if(left == 0 and top == 0):
                    line_count += 1

                left, right, top, bottom = 0, 0, 0, 0
    
    return line_count


if __name__ == "__main__":
    rows = int(input("Enter the number of rows of the 2D matrix :: "))
    columns = int(input("Enter the number of columns of the 2D matrix :: "))
    matrix = []
    for i in range(rows):
        row = []
        for j in range(columns):
            while 1:
                element = input(f"Enter values for the position row :: {i} and column :: {j} ->")
                if element not in ["X", "."]:
                    print("Please enter a valid input - (X or .) else we are stuck here forever!")
                else:
                    row.append(element)
                    break
        matrix.append(row)
    
    print(f"Matrix entered :: {matrix}")

    num_of_lines = count_lines(arr=matrix)
    print(f"Number of lines in matrix - {num_of_lines}")