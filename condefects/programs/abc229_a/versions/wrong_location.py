# Pattern strings verified; check the two rows are joined in the right order
S = input() + input()

if S == '.#.#' or S == '#.#.' :
    print('No')
else:
    print('Yes')
