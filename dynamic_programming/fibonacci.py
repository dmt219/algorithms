def fib_dp(n: int):
  result = [None] * n
  result[0] = 0
  result[1] = 1
  for i in range(2, n):
    result[i] = result[i - 1] + result[i - 2]
  
  return result

if __name__ == '__main__':
  print(fib_dp(10))
