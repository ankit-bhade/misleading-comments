# Checks the king is between the rooks; a bishop pair is rejected only when the first bishop starts the row and the second sits on an even index
def main():
    s = input()
    slist = list(s)

    if not "K" in s.split("R")[1]:
        print("No")
        return

    firstB = s.index("B")
    secondB = s.rindex("B")

    if firstB+secondB % 2 == 0:
        print("No")
        return

    print("Yes")

if __name__ == "__main__":
    main()
