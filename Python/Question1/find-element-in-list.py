'''
Time Complexity - O(logn)
Space Complexity - O(1)
'''
import sys


def find_target_in_nums(nums:list,target:int) -> list[int,int]:
    first_position,last_position=-1,-1

    if nums == []:
        return [first_position,last_position]
    
    start_seek = 0
    stop_seek = len(nums) - 1

    #finding the first position
    while start_seek <= stop_seek:
        midpoint = start_seek + (stop_seek-start_seek)//2
        if nums[midpoint] == target:
            first_position = midpoint
            stop_seek = midpoint - 1
        elif nums[midpoint] < target:
            start_seek = midpoint + 1
        else:
            stop_seek = midpoint - 1

    start_seek = 0
    stop_seek = len(nums) - 1

    #finding the last position
    while start_seek <= stop_seek:
        midpoint = start_seek + (stop_seek-start_seek)//2
        if nums[midpoint] == target:
            last_position = midpoint
            start_seek = midpoint + 1
        elif nums[midpoint] < target:
            start_seek = midpoint + 1
        else:
            stop_seek = midpoint - 1

    return [first_position,last_position]
    


if __name__ == "__main__":
    
    # creating an empty list
    nums = []
    
    while 1:
        try:
            n = input("Enter number inside the list. [Press * to stop entering any more elements] -> ")
            if n == '*':
                break
            nums.append(int(n))
        except Exception as e:
            print(f"There is an exception raised due to {e}. Terminating the code!")
            sys.exit(1)



    # # number of elements as input
    # n = int(input("Enter number of list elements : ")) # Example - 6

    # print("Enter elements into the list. Press Enter before entering the elements after the first element!")
    # for i in range(0, n):
    #     ele = int(input())
    #     nums.append(ele) 
    
    print(f"Entered list is :: {nums}")

    target = int(input("Enter the target: "))

    position = find_target_in_nums(nums=nums,target=target)

    print(f"Position inside the list -> {position}")