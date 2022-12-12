class Dir(dict):
    def __init__(self, name, parent):
        super().__init__()
        self.name = name
        self.parent = parent
        self.files = {}
        self.dirs = {}
        self._size = None

    def get_size(self):
        if not self._size:
            self._size = sum(d.get_size() for d in self.dirs.values()) + sum(f.size for f in self.files.values())
        return self._size


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


def _parse_dir(lines):
    root = Dir('/', None)

    current_dir = root
    for line in lines[1:]:  # skip "cd /"
        if line.startswith('$ cd ..'):
            current_dir = current_dir.parent
        elif line.startswith('$ cd'):
            dir_name = line[len('$ cd'):].strip()
            current_dir = current_dir.dirs[dir_name]
        elif line.startswith('$ ls'):
            pass  # next lines will be the dir content
        else:  # does not start with $
            val, name = line.strip().split(' ')
            if val == 'dir':
                current_dir.dirs[name] = Dir(name, current_dir)
            else:  # file
                current_dir.files[name] = File(name, int(val))
    return root


def task1(cnt):
    root = _parse_dir(cnt.splitlines())

    result = 0

    to_check = [root]
    while to_check:
        d = to_check.pop()
        if d.get_size() <= 100000:
            result += d.get_size()
        to_check.extend(d.dirs.values())

    print(result)


def task2(cnt):
    root = _parse_dir(cnt.splitlines())

    space_to_free = 30000000 - (70000000 - root.get_size())

    to_delete = root.get_size()

    to_check = [root]
    while to_check:
        d = to_check.pop()
        if space_to_free <= d.get_size() < to_delete:
            to_delete = d.get_size()
        to_check.extend(d.dirs.values())

    print(to_delete)
