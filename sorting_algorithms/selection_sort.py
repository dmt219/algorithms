# Selection sort works by repeatedly finding the smallest element from the
# unsorted subarray and insert it into the sorted subarray

def swap(arr, index1, index2):
  temp = arr[index1]
  arr[index1] = arr[index2]
  arr[index2] = temp

def selection_sort(arr):
  for i in range(0, len(arr)):
    min = arr[i]
    index_of_min = i
    for j in range(i, len(arr)):
      if arr[j] < min:
        min = arr[j]
        index_of_min = j

    swap(arr, index_of_min, i)


if __name__ == "__main__":
  arr_1 = [5, 10, 9, 15, 28, 100000, 1997, 1]
  assert(selection_sort(arr_1) == arr_1.sort())
