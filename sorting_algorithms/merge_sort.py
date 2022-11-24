# Merge sort is based off the idea of "divide and conquer"
# It works by repeatedly dividing the array in halves, then merge the subarrays
# in sorted order
#         5,4,1,3
#     5,4          1,3
#    5   4        1   3
#     4,5          1,3
#         1,3,4,5
# Time complexity: O(nlogn), Space Complexity: O(n)

def merge_sort(nums):
  if len(nums) == 1: return nums

  halfPoint = len(nums) // 2
  L = merge_sort(nums[:halfPoint])
  R = merge_sort(nums[halfPoint:])
  index, i, j = 0, 0, 0

  while(i < len(L) and j < len(R)):
    if L[i] < R[j]:
      nums[index] = L[i]
      i+=1
    else:
      nums[index] = R[j]
      j+=1
    index+=1

  while(i < len(L)):
    nums[index] = L[i]
    index+=1
    i+=1

  while(j < len(R)):
    nums[index] = R[j]
    index+=1
    j+=1

  return nums


if __name__ == '__main__':
  arr1 = [10,2,1,3,5,83,24,100]
  assert(merge_sort(arr1) == sorted(arr1))
  arr2 = ['b','a','d','f','c']
  assert(merge_sort(arr2) == sorted(arr2))
