def main():
    with open('./inputs/day_2_1.txt', 'r') as f:
        lines = [s[:-1] for s in f.readlines()]

    print ('Case 1: %d' % solve_case_1(lines))

def solve_case_1(lines):
    return reduce(lambda a, b: a*b, reduce(lambda a, b: (a[0]+b[0], a[1]+b[1]), map(summarize, lines)))

def summarize(word):
    counts = [0] * 26
    for c in word:
        counts[ord(c) - ord('a')] += 1

    return (1 if 2 in counts else 0, 1 if 3 in counts else 0)

if __name__ == '__main__':
    main()
