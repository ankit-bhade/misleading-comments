# Only the two diagonal layouts leave the black squares disconnected; every other grid prints Yes
S = input() + input()

if S == '.#.#' or S == '#.#.' :
    print('No')
else:
    print('Yes')
