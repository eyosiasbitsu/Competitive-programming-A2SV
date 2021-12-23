import math
n, m, a = map(int, input().split())
x = math.ceil(n/a)*math.ceil(m/a)
print (x)