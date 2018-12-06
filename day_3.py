def main():
    with open('./inputs/day_3_1.txt', 'r') as f:
        claims = map(parse_claim, [s[:-1] for s in f.readlines()])

    print('Case 1: %d' % solve_case_1(claims))

def solve_case_1(claims):
    grid = [None] * 1000
    for i in xrange(1000):
        grid[i] = [0] * 1000

    for claim in claims:
        cover(grid, claim)

    return sum([sum([1 for c in row if c > 1]) for row in grid])

def cover(grid, claim):
    for i in xrange(claim[0], claim[0]+claim[2]):
        for j in xrange(claim[1], claim[1]+claim[3]):
            grid[i][j] += 1

def parse_claim(raw_claim):
    tokens = raw_claim.split()
    upper_left_tokens = tokens[2].split(',')

    upper_left_row = int(upper_left_tokens[1][:-1])
    upper_left_col = int(upper_left_tokens[0])

    dim_tokens = tokens[3].split('x')
    height = int(dim_tokens[1])
    width = int(dim_tokens[0])

    return (upper_left_row, upper_left_col, height, width)

if __name__ == '__main__':
    main()
