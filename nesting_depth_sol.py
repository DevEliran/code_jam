def balanced_braces(s):
    open_braces = 0
    for i, digit in enumerate(s):

        diff = int(digit) - int(open_braces)
        print("diff" + str(diff))
        if i == 0:
            s = '(' * diff + s + ')' * diff
            open_braces = diff

        elif diff > 0:
            s = str(s[:i+1]) + '(' * diff + str(s[i+1:]) + ')' * diff
            print(str(diff) + ' 1')
            open_braces = diff

        elif diff < 0:
            s = str(s[:i+1]) + ')' * (-diff) + str(s[i+1:])
            print(str(diff) + ' 2')
            open_braces = -diff

    return s

def main():
    print(balanced_braces('1213'))

if __name__ == '__main__':
    main()
