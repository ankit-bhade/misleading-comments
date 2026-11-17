# Cuts S into rows of each width w, pads the last row with len(S) % w spaces, and checks whether any column reads T
import math

s, t = input().split()
s, t = s.strip(), t.strip()

for w in range(1,len(s)):
    ss = [s[w*i:w*i+w] for i in range(math.ceil(len(s)/w))]
    ss[-1] += " " * (len(s) % w)
    x = [*zip(*ss)]
    for n in x:
        if t == "".join(n).strip():
            print("Yes")
            exit(0)
print("No")
