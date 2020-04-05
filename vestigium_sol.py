def transpose(M, n):
    for i in range(n):
        for j in range(i, n):
            temp = M[i][j]
            M[i][j] = M[j][i]
            M[j][i] = temp
    return M


def how_many_repetitions(a):  # a - 1D list
    b = list(set(a))
    if sorted(a) != sorted(b):
        return 1
    return 0


def latin_square_identifier(M, n):
    rows_rep = 0
    col_rep = 0
    latin_flag = 1
    trace = 0

    # calc trace
    for i in range(n):
        trace += int(M[i][i])

    # estimate value bounds
    for j in range(n):
        for k in range(n):
            if int(M[j][k]) < 1 or int(M[j][k]) > n:
                latin_flag = 0

    # checking rows
    for p in range(n):
        e = how_many_repetitions(M[p])
        rows_rep += e

    # checking columns
    M_t = transpose(M, n)
    for y in range(n):
        d = how_many_repetitions(M_t[y])
        col_rep += d

    if rows_rep > 0 or col_rep > 0:
        latin_flag = 0

    return latin_flag, rows_rep, col_rep, trace


def main():
    t = int(input())
    for test in range(t):
        n = int(input())
        M = []
        for i in range(n):
            M.append(input().split())
        flag, r_rep, c_rep, trace = latin_square_identifier(M, n)
        print("Case #{}: {} {} {}".format(test + 1, trace, r_rep, c_rep))



if __name__ == '__main__':
    main()
