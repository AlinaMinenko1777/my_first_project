def fn2(x):
    if x % 2 != 0:
        return True
    else:
        return False
print(list(filter(fn2, [2, 5, 9, 8])))


