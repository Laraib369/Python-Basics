def sum_recursive(n):
    if n ==0:
      return 0

    else:
        return (n + sum_recursive(n-1))

a = sum_recursive(6)
print(a)