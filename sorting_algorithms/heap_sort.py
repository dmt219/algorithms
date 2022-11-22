# A heap is basically a binary tree where each node dominates its children.
# We're building a min heap, i.e. the key of each node is smaller than its
# children. Root node will have the smallest key.
# We'll use an array to represent the heap, the children of node i will have
# indexes 2i and 2i+1
# Heapsort is basically selection sort, but for selection sort picking the
# minimum element from an array is O(n), for heapsort it's O(nlogn)
# Required heap opeartions:
# - Insert
# - Extract min

def initialize_heap(nums):
  heap = []
  for num in nums:
    insert(heap, num)
  return heap

def heap_swap(heap, index1, index2):
  temp = heap[index1]
  heap[index1] = heap[index2]
  heap[index2] = temp

def bubble_up(heap, index):
  if (index == 0): return # root node
  if(heap[index//2] > heap[index]):
    heap_swap(heap, index//2, index)
    bubble_up(heap, index//2)

def bubble_down(heap, index):
  if(index*2 >= len(heap)): return #child node
  indexToSwap = index*2
  if(index*2 + 1 < len(heap)):
    indexToSwap = index*2 +1 if heap[index*2+1] < heap[index*2] else index*2
  if(heap[index] > heap[indexToSwap]):
    heap_swap(heap, index, indexToSwap)
    bubble_down(heap, indexToSwap)

def insert(heap, num):
  heap.append(num)
  bubble_up(heap, len(heap) - 1)

def extract_min(heap):
  root = heap[0]
  heap_swap(heap, 0, len(heap)-1)
  heap.pop()
  bubble_down(heap, 0)
  return root
  
def heap_sort(nums):
  heap = initialize_heap(nums)
  for i,_ in enumerate(nums):
    nums[i] = extract_min(heap)
  return nums

if __name__ == '__main__':
  arr1 = [3,5,2,1,3,4,6]
  arr2 = [13, 12, 11, 7, 15, 16, 1, 17]
  arr3 = ['x', 'b', 'a', 'a', 'c', 'z', 'f']
  assert(heap_sort(arr1) == sorted(arr1))
  assert(heap_sort(arr2) == sorted(arr2))
  assert(heap_sort(arr3) == sorted(arr3))
  
