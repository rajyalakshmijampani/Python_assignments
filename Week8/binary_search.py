L = [1, 6, 8, 10, 38, 94, 219, 834, 1009]


def search(L, n):
  start = 0
  end = len(L)
  while start < end:
    mid = (start + end) // 2
    if L[mid] < n:
      start = mid + 1
    elif L[mid] > n:
      end = mid
    else:
      return mid
  return -1


print(search(L, 220))
