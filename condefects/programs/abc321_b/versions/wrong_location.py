# Score range verified; check the trimmed sum drops exactly one highest and one lowest score
N,X = map(int,input().split())
A = list(map(int,input().split()))



def check():
  for i in range(0,100):
    A.append(i)
    A.sort(reverse=True)
    x = sum(A) - A[0] - A[-1]
    if x >= X:
      print(i)
      return
    A.remove(i)
  print(-1)

check()
