INPUT_FILE = "testinput.txt"
INPUT_FILE = "input.txt"


def getInput():
    with open(INPUT_FILE) as f:
        i = [i.strip() for i in f.readlines()]
    arr = []
    for st in i:
        arr.append([int(char) for char in st])

    return arr


def pt1():
    trees = getInput()

    numVisible = 0
    for i, row in enumerate(trees):
        for j, tree in enumerate(row):
            allShortOnLeft = True
            allShortOnRight = True
            allShortAbove = True
            allShortBelow = True
            for left in range(0, j):
                allShortOnLeft = allShortOnLeft and trees[i][left] < tree
            for right in range(j + 1, len(trees[0])):
                allShortOnRight = allShortOnRight and trees[i][right] < tree
            for above in range(0, i):
                allShortAbove = allShortAbove and trees[above][j] < tree
            for below in range(i+1, len(trees)):
                allShortBelow = allShortBelow and trees[below][j] < tree

            if allShortOnLeft or allShortOnRight or allShortAbove or allShortBelow:
                numVisible += 1

    return numVisible


def pt2():
    trees = getInput()

    maxScore = float('-inf')
    for i, row in enumerate(trees):
        for j, tree in enumerate(row):
            lScore = 0
            rScore = 0
            aScore = 0
            bScore = 0
            for left in range(j - 1, -1, -1):
                lScore += 1
                if trees[i][left] >= tree:
                    break
            for right in range(j + 1, len(trees[0])):
                rScore += 1
                if trees[i][right] >= tree:
                    break
            for above in range(i - 1, -1, -1):
                aScore += 1
                if trees[above][j] >= tree:
                    break
            for below in range(i+1, len(trees)):
                bScore += 1
                if trees[below][j] >= tree:
                    break
            maxScore = max(maxScore, lScore * rScore * aScore * bScore)

    return maxScore


print('part 1: ')
print(pt1())
print()
print('part 2: ')
print(pt2())
