# Generate all subsets from the n-elements set {1,2,...,n}
# Solution vector will be an array of n elements, each either True or False. True means element is present in the subset.
# is_a_solution returns true when k == n (i.e. went through all elements)
# process_solution just print out the set
# construct_candidate returns [True, False] as these are potential next candidate

def construct_candidate(c):
  c[0] = True
  c[1] = False

def process_solution(a):
  print('{', end =' ')
  for index, item in enumerate(a):
    if item:
      print(f'{index} ', end='')
  print('}')
  
def is_a_solution(k, n):
  return k == n

def backtrack(a, k, n):
  c = [None] * 2

  if (is_a_solution(a, k, n)):
    process_solution(a, k, n)
  else:
    k += 1
    construct_candidate(a, k, n, c)
    for candidate in c:
      a[k] = candidate
      backtrack(a, k, n)

if __name__ == '__main__':
  n = 3
  backtrack([None] * (n+1), 0, n)
  
  
