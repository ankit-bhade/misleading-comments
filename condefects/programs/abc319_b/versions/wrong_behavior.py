# Collects N's divisors from 1 up to 8 and, for each i, picks the smallest one whose N/j divides i
def get_divisors_list(num):
    divisors = []
    for i in range(1, num+1 if num < 9 else 9):
        if num % i == 0:
            divisors.append(i)
    return divisors

def main():
    n = int(input())
    divisors = get_divisors_list(n)
    answer = ""

    for i in range(n+1):
        is_found = False
        for j in divisors:
            if i % (n / j) == 0:
                answer += str(j)
                is_found = True
                break
        if not is_found:
            answer += "-"
    print(answer)

if __name__ == "__main__":
    main()
