# Minimal cost of changes to convert one string to another
# Operations: Substitution, Insertion, Deletion

# Recurrence Relation to convert the first i characters of string S to first
# j characters of string T:

# min of:
# MATCH : D[i, j] = D[i-1, j-1]
# SUBS  : D[i, j] = D[i-1, j-1] + 1
# INSERT: D[i, j] = D[i, j-1] + 1
# DELETE: D[i, j] = D[i-1, j] + 1

def match(char1, char2):
  if char1 == char2:
    return 0
  else:
    return 1

def edit_distance(s, t):
  max_range = max(len(s), len(t))
  m = [[None for i in range(0, max_range+1)] for j in range(0, max_range+1)]

  # initialize matrix
  for i in range(0, max_range+1):
    m[0][i] = i
    m[i][0] = i

  for i in range(1, len(s)+1):
    for j in range(1, len(t)+1):
      MATCH = m[i-1][j-1] + match(s[i-1], t[j-1])
      INSERT = m[i][j-1] + 1
      DELETE = m[i-1][j] +1
      m[i][j] = min(MATCH, INSERT, DELETE)

  return m[len(s)][len(t)]


if __name__ == '__main__':
  s = 'thou shalt'
  t = 'you should'
  assert(edit_distance(s, t) == 5)
