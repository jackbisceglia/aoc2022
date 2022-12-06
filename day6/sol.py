INPUT_FILE = "testinput.txt"
INPUT_FILE = "input.txt"


def pt1():
    def chrToIdx(c):
        return ord(c) - ord('a')

    with open(INPUT_FILE) as f:
        line = f.read().strip()

    frequency = [0 for i in range(26)]
    unique = 0
    l, r = 0, 0
    while r < len(line):
        # add right
        frequency[chrToIdx(line[r])] += 1
        unique = unique + 1 if frequency[chrToIdx(line[r])] == 1 else unique
        r += 1

        if r - l == 4:
            if unique == 4:
                return r
            else:
                frequency[chrToIdx(line[l])] -= 1
                unique = unique - \
                    1 if frequency[chrToIdx(line[l])] == 0 else unique
                l += 1

    return r


def pt2():
    def chrToIdx(c):
        return ord(c) - ord('a')

    with open(INPUT_FILE) as f:
        line = f.read().strip()

    frequency = [0 for i in range(26)]
    unique = 0
    l, r = 0, 0
    while r < len(line):
        # add right
        frequency[chrToIdx(line[r])] += 1
        unique = unique + 1 if frequency[chrToIdx(line[r])] == 1 else unique
        r += 1

        if r - l == 14:
            if unique == 14:
                return r
            else:
                frequency[chrToIdx(line[l])] -= 1
                unique = unique - \
                    1 if frequency[chrToIdx(line[l])] == 0 else unique
                l += 1

    return r


print('part 1: ')
print(pt1())
print('part 2: ')
print(pt2())
