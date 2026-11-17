# Slice bounds verified; check that L and R are parsed in the right order
def func():
    L, R = list(map(int, input().split()))

    s = "atcoder"
    print(s[L+1:R+1])

if __name__ == '__main__':
    func()
