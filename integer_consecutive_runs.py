import sys


def find_consecutive_runs(list):
    print '[Result]: ' + str(list)


def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print 'Using Example Integer list of [1, 2, 3, 5, 10, 9, 8, 9, 10, 11, 7, 8, 7]'
        print find_consecutive_runs([1, 2, 3, 5, 10, 9, 8, 9, 10, 11, 7, 8, 7])
    else:
        find_consecutive_runs(eval(sys.argv[1]))


if __name__ == '__main__':
    main()
