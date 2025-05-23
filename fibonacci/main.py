with open('./input', 'r') as f:
  input = f.read()

print(input)

#fibonacci számolás
import functools

@functools.lru_cache(None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


fibs = []
n = 0
for item in input:
  #int e az adatunk?
  if type(item) != int:
    print("N/A")
    continue
  while input < fib(n + 1):
    fibs = fib(n)
    n += 1
print("asd")