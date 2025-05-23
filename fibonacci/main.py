with open('./input.txt', 'r') as f:
  input = f.read().split("\n")

#fibonacci számolás
import functools

@functools.lru_cache(None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)



for item in input:
  fibs = []
  n = 0
  #int e az adatunk?  
  try:
    item = int(item)
  except ValueError:
    try:
      item = float(item)
    except ValueError:
      continue
  while item > fib(n + 1):
     fibs.append(fib(n))
     n += 1
  fibs = [item for item in fibs if item % 3 == 0]
  if len(fibs) != 0:
    print(*fibs, sep=", ") 