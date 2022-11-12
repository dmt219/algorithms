# Place 8 queens on a 8x8 chessboard so that no queens threaten each other
# Because no 2 queens can be in the same row, solution vector a will be an array of 8 elements, with index i represents a queen position in the ith row
# process_solution just prints out solution vector
# is_a_solution is true when k == n
# construct_candidate select the possible location for queen in the kth row that does not violate the rule

def is_a_solution(k, n):
  return k == n

def process_solution(a):
  print(a[1:])

def construct_candidates(a, k, n):
  c = []
  if k == 1:
    return list(range(1, 9))
  for x in range(1, n+1): # iterate over possible value of candidate (1-8), check if each is valid
    valid = True
    for y in range(1, k): # already filled values
      if abs(k - y) == abs(x - a[y]): # diagonal violation
        valid = False
      elif x == a[y]: # column violation
        valid = False
    if valid:
      c.append(x)

  return c

def backtrack(a, k, n):
  if is_a_solution(k, n):
    process_solution(a)
  else:
    k += 1
    c = construct_candidates(a, k, n)
    for candidate in c:
      a[k] = candidate
      backtrack(a, k, n)

if __name__ == '__main__':
  backtrack([None]*9, 0, 8)
