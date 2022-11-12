# Generate all permutations of {1,...,n}
# Solution vector is an array a of size n, each index is
# a number in the permutation
# is_a_solution is true when k == n
# construct_candidates returns all elements from {1,...n} NOT currently in a
# process_solution just print out the permutation

def is_a_solution(k, n):
  return k == n

def process_solution(a):
  print(''.join([str(item) for item in a if item != None]))

def construct_candidates(a, k, n):
  return [item for item in list(range(1, n+1)) if item not in a[:k]]

def backtrack(a, k, n):
  if is_a_solution(k, n):
    process_solution(a)
  else:
    k += 1
    c = construct_candidates(a, k, n)
    for item in c:
      a[k] = item
      backtrack(a, k, n)

if __name__ == '__main__':
  n = 3
  backtrack([None]*(n+1), 0, n)
