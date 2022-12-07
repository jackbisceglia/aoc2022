
# INPUT_FILE = "testinput.txt"
INPUT_FILE = "input.txt"


def pt1():
    with open(INPUT_FILE) as f:
        cmds = [i.strip() for i in f.readlines()]

    def search(commands, depth, valid_dirs):
        file_tree_size = 0
        idx = 0
        while idx < len(commands):
            command = commands[idx]
            piecesOfCommand = command.split(' ')
            if piecesOfCommand[0] == "$":
                if piecesOfCommand[1] == "cd":
                    if piecesOfCommand[2] == "..":
                        if file_tree_size <= 100000:
                            valid_dirs.append(file_tree_size)
                        return file_tree_size, idx + 1
                    else:
                        newSum, nextCommand = search(commands[idx+1:],
                                                     depth + 1, valid_dirs)
                        file_tree_size += newSum
                        idx += nextCommand

            else:
                if piecesOfCommand[0] != "dir":
                    file_tree_size += int(piecesOfCommand[0])

            idx += 1

        if file_tree_size <= 100000:
            valid_dirs.append(file_tree_size)
        return file_tree_size, idx

    valid_dirs = []

    search(cmds[1:], 0, valid_dirs)

    return sum(valid_dirs)


def pt2():
    with open(INPUT_FILE) as f:
        cmds = [i.strip() for i in f.readlines()]

    def getLeastSpaceNeeded(dir_sizes):
        total_disk_size = 70000000
        update_size = 30000000
        disk_space_taken = dir_sizes[-1]
        disk_space_free = total_disk_size - disk_space_taken

        space_we_need_to_free = update_size - disk_space_free

        sorted_space = sorted(dir_sizes)

        for space in sorted_space:
            if space_we_need_to_free <= space:
                return space
        return None

    def search(commands, depth, dir_sizes):
        file_tree_size = 0
        idx = 0
        while idx < len(commands):
            command = commands[idx]
            piecesOfCommand = command.split(' ')
            if piecesOfCommand[0] == "$":
                if piecesOfCommand[1] == "cd":
                    if piecesOfCommand[2] == "..":
                        dir_sizes.append(file_tree_size)
                        return file_tree_size, idx + 1
                    else:
                        newSum, nextCommand = search(commands[idx+1:],
                                                     depth + 1, dir_sizes)
                        file_tree_size += newSum
                        idx += nextCommand

            else:
                if piecesOfCommand[0] != "dir":
                    file_tree_size += int(piecesOfCommand[0])

            idx += 1

        dir_sizes.append(file_tree_size)
        return file_tree_size, idx

    dir_sizes = []

    search(cmds[1:], 0, dir_sizes)

    return getLeastSpaceNeeded(dir_sizes)


print('part 1: ')
print(pt1())
print()
print('part 2: ')
print(pt2())
