import random

def A(a : list[int]) -> int:
   n : int = 0
   c : list[int] = []
   for i in range(len(a)):
       if n == 0:
           n += 1
           if a[i] % 2 == 0:
               c.append(a[i])
       else:
           n += -1
   work : int = 1
   for j in range(len(c)):
       work = c[j] * work
   return work

def stroka(st : str) -> str:
    arr : list[str] = st.split()

    slovo(arr)

    st = " ".join(arr)
    return st

def slovo(arr: list[str]) -> None:
    a: list[int] = []
    for i in range(len(arr) - 1):
        if arr[i+1] == arr[i]:
            a.append(i)
    count = 0
    for i in a:
        arr.pop(i - count)
        count += 1

a : list[int] = []
m = int(input())
if m <= 1:
    print("Try again")
    exit()

for i in range(m):
    el = int(input())
    if el >= 1 and el <= 200:
        a.append(el)
    else:
        print("Try again")
        exit()
print("a", (a))

b : list[int] = []
t = int(input())
if t <= 1:
    print("Try again")
    exit()

for i in range(t):
    el2 = random.randint(1,200)
    b.append(el2)
print("b", (b))

print("a* =", A(a))
print("b* =", A(b))
st = str(input())
print(stroka(st))