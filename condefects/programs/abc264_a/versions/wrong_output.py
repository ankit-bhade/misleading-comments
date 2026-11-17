# Example: input '1 3' prints co
def func():
    L, R = list(map(int, input().split()))

    s = "atcoder"
    print(s[L+1:R+1])

if __name__ == '__main__':
    func()
