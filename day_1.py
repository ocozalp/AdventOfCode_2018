def main():
    with open('./inputs/day_1_1.txt', 'r') as f:
        numbers = list(map(int, [s[:-1] for s in f.readlines()]))

    print('Case 1: %d' % solve_case_1(numbers))

def solve_case_1(numbers):
    return sum(numbers)
    
if __name__ == '__main__':
    main()
