def priority(char):
    if char.isupper():
        return ord(char) - ord('A') + 27
    else:
        return ord(char) - ord('a') + 1

# pt1
def pt1():
    with open('input.txt') as f:
        lines = [line.strip() for line in f]

        allSacks = [[line[:len(line) // 2], line[len(line) // 2:]] for line in lines]
        totalPriority = 0
        for (sack1, sack2) in allSacks:
            seen = set(sack2)

            for char in sack2:
                if char in sack1:
                    totalPriority += priority(char)
                    break

        return totalPriority

# pt2
def pt2():
    with open('input.txt') as f:
        lines = [line.strip() for line in f]

        groups = [lines[i: i + 3] for i in range(0, len(lines), 3)]
        totalPriority = 0

        for (elf1, elf2, elf3) in groups:
            s = set(elf1)

            s2 = set()
            for char in elf2:
                if char in s:
                    s2.add(char)

            for char in elf3:
                if char in s2:
                    totalPriority += priority(char)
                    break

        return totalPriority

print(pt2())