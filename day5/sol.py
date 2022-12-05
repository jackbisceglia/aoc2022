INPUT_FILE = "testinput.txt"
INPUT_FILE = "input.txt"


def pt1():
    with open(INPUT_FILE) as f:
        lines = [line.strip("\n") for line in f]

    crates = []
    alg = []
    addToCrates = True
    for line in lines:
        if line == "":
            addToCrates = False
            continue
        if addToCrates:
            crates.append(line)
        else:
            alg.append(line)

    newCrates = []
    for row in crates:
        newRow = []
        for i in range(0, len(row), 4):
            if row[i:i+3] == "   ":
                newRow.append("_")
            else:
                newRow.append(row[i:i+3])

        newCrates.append(newRow)

    crates = newCrates
    cols = [int(i) for i in crates[-1]]

    stacks = [[] for i in cols]

    for col in cols:
        for i in range(len(crates) - 2, -1, -1):
            if crates[i][col - 1] != '_':
                stacks[col - 1].append(crates[i][col - 1][1])

    for instruction in alg:
        instruction = instruction.split(' ')
        (_, qty, _, src, _, dest) = instruction
        qty, src, dest = int(qty), int(src), int(dest)
        for i in range(qty):
            curr = stacks[src - 1].pop()
            stacks[dest - 1].append(curr)

    st = ''.join([stack.pop() for stack in stacks])
    print(st)


def pt2():
    with open(INPUT_FILE) as f:
        lines = [line.strip("\n") for line in f]

    crates = []
    alg = []
    addToCrates = True
    for line in lines:
        if line == "":
            addToCrates = False
            continue
        if addToCrates:
            crates.append(line)
        else:
            alg.append(line)

    newCrates = []
    for row in crates:
        newRow = []
        for i in range(0, len(row), 4):
            if row[i:i+3] == "   ":
                newRow.append("_")
            else:
                newRow.append(row[i:i+3])

        newCrates.append(newRow)

    crates = newCrates
    cols = [int(i) for i in crates[-1]]

    stacks = [[] for i in cols]

    for col in cols:
        for i in range(len(crates) - 2, -1, -1):
            if crates[i][col - 1] != '_':
                stacks[col - 1].append(crates[i][col - 1][1])

    for instruction in alg:
        instruction = instruction.split(' ')
        (_, qty, _, src, _, dest) = instruction
        qty, src, dest = int(qty), int(src), int(dest)
        currOrder = []
        for i in range(qty):
            curr = stacks[src - 1].pop()
            currOrder = [curr] + currOrder
        stacks[dest - 1] = stacks[dest - 1] + currOrder

    st = ''.join([stack.pop() for stack in stacks])
    print(st)


print('part 1: ')
pt1()
print('part 2: ')
pt2()
