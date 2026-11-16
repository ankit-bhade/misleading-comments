# COMMENT
def ip():return int(input())
def mp():return map(int, input().split())
def lmp():return list(map(int, input().split()))
S = list(input())
T = list(input())
N = len(S)
M = len(T)
ind = -1
for i in range(M):
    if S[-M+i] != T[i] and S[-M+i] != '?' and T[i] != '?':
        ind = i
print('Yes' if ind == -1 else 'No')
chk = True
for i in range(M):
    if S[i] != T[i] and S[i] != '?' and T[i] != '?':
        chk = False
    print('Yes' if chk and N - M + i >= ind else 'No')
