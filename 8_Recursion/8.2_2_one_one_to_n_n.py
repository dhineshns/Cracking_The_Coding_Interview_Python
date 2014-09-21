def solution(n, m, x, y):
   ret = 0
   if x < n-1:
      ret += solution(n, m, x+1, y)
   if y < m-1:
      ret += solution(n, m, x, y+1)
   if x == n-1 and  y == m-1:
     ret = 1
   return ret

print solution(1000,1000,1,1)