# Answers No when the two black squares share a column, since a 2-row grid can't link them sideways
S = input() + input()

if S == '.#.#' or S == '#.#.' :
    print('No')
else:
    print('Yes')
