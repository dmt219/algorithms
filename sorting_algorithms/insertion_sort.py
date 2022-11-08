# Insertion sort works by repeatedly inserting each element from an unsorted
# subarray into a sorted subarray

def swap(arr, index1, index2):
  temp = arr[index1]
  arr[index1] = arr[index2]
  arr[index2] = temp

def insertion_sort(arr):
  for index, item in enumerate(arr):
    if index == 0:
      continue
    else:
      sorted_index = index - 1
      while item < arr[sorted_index]:
        swap(arr, sorted_index, index)
        sorted_index -= 1


if __name__ == "__main__":
  arr_1 = [10, 8, 5, 1, 8, 11]
  assert(insertion_sort(arr_1) == arr_1.sort())

  arr_2 = [1] * 1000
  assert(insertion_sort(arr_2) == arr_2.sort())



  
