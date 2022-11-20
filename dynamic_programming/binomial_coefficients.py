# (n) = (n-1) + (n-1)
# (k)   (k-1)   ( k )

# (n) = 1
# (n)

# (n) = 1
# (0)


def binomial_coefficients(n, k):
  result = [[0 for i in range(n+1)] for j in range(n+1)]
  for i in range(n):
    result[i][0] = 1
  
  for i in range(n):
    result[i][i] = 1

  for i in range(2, n+1):
    for j in range(1, i):
      result[i][j] = result[i-1][j-1] + result[i-1][j]
  
  return result[n][k]

if __name__ == '__main__':
  assert(binomial_coefficients(3, 2) == 3)
  assert(binomial_coefficients(5, 2) == 10)

# e.g. binomial_coefficients(3,2)
# (1,0) (2,1) ... (n,0) = 1
# (1,1) (2,2) ... (n,n) = 1
# (2,1) = (1,0) + (1,1)
# (3,1) = (2,0) + (2,1)
# (3,2) = (2,1) + (2,2)
