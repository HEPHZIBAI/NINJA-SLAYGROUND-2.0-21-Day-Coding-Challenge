'''
Problem statement
There is an integer array ‘A’ of size ‘N’.



Number of inversions in an array can be defined as the number of pairs of ‘i’, ‘j’ such that ‘i’ < ‘j’ and ‘A[i]’ > ‘A[j]’.

You must return the number of inversions in the array.



For example,
Input:
A = [5, 3, 2, 1, 4], N = 5
Output:
7
Explanation: 
The pairs satisfying the condition for inversion are (1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), and (3, 4). 
The number of inversions in the array is 7.
Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1:
4
4 3 2 1
Sample Output 1:
6
Explanation Of Sample Input 1:
Input:
A = [4, 3, 2, 1], N = 4
Output:
6
Explanation: 
The pairs satisfying the condition for inversion are (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), and (3, 4).    
The number of inversions in the array is 6.
Sample Input 2:
5
1 20 6 4 5
Sample Output 2:
5
Constraints:
1 <= N <= 10^5
1 <= A[i] <= 10^9
Time Limit: 1 sec
'''

from typing import List

def numberOfInversions(a: List[int], n: int) -> int:
    def merge_and_count(temp_arr, left, mid, right):
        i, j, k = left, mid + 1, left
        inv_count = 0
        
        # Merge the two halves while counting inversions
        while i <= mid and j <= right:
            if a[i] <= a[j]:
                temp_arr[k] = a[i]
                i += 1
            else:
                temp_arr[k] = a[j]
                inv_count += (mid - i + 1)  # Count inversions
                j += 1
            k += 1
        
        # Copy remaining elements of left half
        while i <= mid:
            temp_arr[k] = a[i]
            i += 1
            k += 1
        
        # Copy remaining elements of right half
        while j <= right:
            temp_arr[k] = a[j]
            j += 1
            k += 1
        
        # Copy the sorted subarray back into the original array
        for i in range(left, right + 1):
            a[i] = temp_arr[i]
        
        return inv_count
    
    def merge_sort_and_count(temp_arr, left, right):
        inv_count = 0
        if left < right:
            mid = (left + right) // 2
            
            inv_count += merge_sort_and_count(temp_arr, left, mid)
            inv_count += merge_sort_and_count(temp_arr, mid + 1, right)
            inv_count += merge_and_count(temp_arr, left, mid, right)
        
        return inv_count
    
    temp_arr = [0] * n
    return merge_sort_and_count(temp_arr, 0, n - 1)
