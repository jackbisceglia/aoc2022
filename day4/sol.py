INPUT_FILE = "testinput.txt"
INPUT_FILE = "input.txt"


def pt1():
    def convertRange(range):
        nums = range.split("-")
        return (int(nums[0]), int(nums[1]))

    with open(INPUT_FILE) as f:
        lines = [line.strip() for line in f]

    pairs = [line.split(',') for line in lines]

    ranges = [(convertRange(pair1), convertRange(pair2))
              for pair1, pair2 in pairs]

    total = 0
    for range1, range2 in ranges:
        low1, high1 = range1
        low2, high2 = range2

        if (low1 <= low2 and high1 >= high2) or (low2 <= low1 and high2 >= high1):
            total += 1

    print(total)


def pt2():
    def convertRange(range):
        nums = range.split("-")
        return (int(nums[0]), int(nums[1]))

    with open(INPUT_FILE) as f:
        lines = [line.strip() for line in f]

    pairs = [line.split(',') for line in lines]

    ranges = [(convertRange(pair1), convertRange(pair2))
              for pair1, pair2 in pairs]

    total = 0
    for range1, range2 in ranges:
        low1, high1 = range1
        low2, high2 = range2

        set1 = set(i for i in range(low1, high1 + 1))
        set2 = set(i for i in range(low2, high2 + 1))

        if len(set1.intersection(set2)) > 0:
            total += 1

    print(total)


pt2()
