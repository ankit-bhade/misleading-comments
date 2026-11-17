# Prints characters L through R of "atcoder", counting from 1
def func():
    L, R = list(map(int, input().split()))

    s = "atcoder"
    print(s[L+1:R+1])

if __name__ == '__main__':
    func()
