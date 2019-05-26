import random

def get_n_random_integer(n):
    random.seed(100)
    numbers = []
    for i in range(n):
        s = random.randint(-100,100)
        numbers.append(s)
    return numbers

def shell_sort(arr):
  n = len(arr)
  gap = int(n / 2)
  karsilastirma_sayisi = 0
  swap_sayisi = 0
  while(gap > 0):
    for i in range(gap,n):
      karsilastirma_sayisi += 1
      temp = arr[i]
      j = i
      while j >= gap and arr[j - gap] > temp:
          swap_sayisi += 1
          karsilastirma_sayisi += 1
          arr[i] = arr[j - gap]
          j -= gap
      arr[j] = temp
    gap = gap // 2
  return arr,karsilastirma_sayisi,swap_sayisi

a = get_n_random_integer(100)
print(a)
print(shell_sort(a))
