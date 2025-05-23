import functools

with open("./input.txt", "r") as f:
    input = f.read().split("\n")


@functools.lru_cache(None)
def fib(n):
    """
    Python dokumentációban talált mód fibonacci számok generálására: 
    https://docs.python.org/3/library/functools.html#functools.lru_cache
    
    Args:
        n (int): A szám aminek a fibonacci értékére kíváncsiak vagyunk.

    Returns:
        int: A megadott szám fibonacci értéke
    """
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


for item in input:
    fibs = []
    n = 0

    # Int vagy float e az adat?
    try:
        item = int(item)
    except ValueError:
        try:
            item = float(item)
        except ValueError:
            continue
    # A vizsgálandó lista elkészítése.
    while item > fib(n + 1):
        fibs.append(fib(n))
        n += 1
    # A lista kiválogatása
    fibs = [item for item in fibs if item % 3 == 0]
    # A lista konzolra kiírása, abban az esetben ha ez szükséges.
    if len(fibs) != 0:
        print(*fibs, sep=", ")
