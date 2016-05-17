import sys


# 3 consecutive numbers == [x, x+1, x+2] or [x, x - 1, x - 2]

def find_consecutive_runs(list):
    run_indices = []
    range_begin = 0
    range_end = 3
    index = 0

    while range_end <= len(list):  # ends loop when final slice of 3 has been found
        slice = list[range_begin:range_end]  # break array into a slices of 3 with increasing indices
        x = slice[0]
        if slice == [x, x + 1, x + 2] or slice == [x, x - 1, x - 2]:
            # Verify consecutive numbers that increase or decrease by 1 and add index of 1st element
            run_indices.append(index)
        range_begin += 1
        range_end += 1
        index += 1

    if run_indices:
        print '[Result]: ' + str(run_indices)
        return run_indices

    return None


def main():
    if len(sys.argv) == 1 or len(sys.argv) > 3:
        print 'Using Example Integer list of [1, 2, 3, 5, 10, 9, 8, 9, 10, 11, 7, 8, 7]'
        return find_consecutive_runs([1, 2, 3, 5, 10, 9, 8, 9, 10, 11, 7, 8, 7])
    else:
        return find_consecutive_runs(eval(sys.argv[1]))


if __name__ == '__main__':
    main()
