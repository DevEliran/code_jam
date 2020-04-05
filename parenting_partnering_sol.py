def schedule(assignments):
    j_end = 0
    c_end = 0
    res = []
    res_str = ""
    # print(assignments)
    for assign in assignments:
        if int(assign[0]) >= j_end:
            res.append((assign[2], 'J'))
            j_end = int(assign[1])
        elif int(assign[0]) >= c_end:
            res.append((assign[2], 'C'))
            c_end = int(assign[1])
        else:
            return "IMPOSSIBLE"

    for i in sorted(res):
        res_str += str(i[1])

    return res_str


def main():
    a = []
    t = int(input())
    for test in range(t):
        n = int(input())
        for i in range(n):
            x, y = input().split()
            a.append((int(x), int(y), i))
        # print(a)
        print("Case #{}: {}".format(test+1, schedule(sorted(a))))
        a = []
    # a = [(7, 8, 0), (9, 10, 1), (1, 8, 2), (2, 5, 3), (150, 250, 4)]
    # print(schedule(sorted(a)))


if __name__ == '__main__':
    main()
