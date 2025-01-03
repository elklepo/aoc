class IntcodeVM:
    def __init__(self, inst):
        self.inst = inst
        self.ip = 0

    def run(self):
        while True:
            op, a, b, c = (self.inst[self.ip + off] for off in range(4))
            match op:
                case 1:
                    self.inst[c] = self.inst[a] + self.inst[b]
                case 2:
                    self.inst[c] = self.inst[a] * self.inst[b]
                case 99:
                    return
                case _:
                    raise Exception(f'Unknown opcode: {op}')
            self.ip += 4


def task1(cnt):
    inst = list(map(int, cnt.split(',')))
    inst[1:3] = [12, 2]
    vm = IntcodeVM(inst)
    vm.run()
    print(vm.inst[0])


def task2(cnt):
    inst_ref = list(map(int, cnt.split(',')))
    for i in range(len(inst_ref)):
        for j in range(len(inst_ref)):
            inst = inst_ref[:1] + [i, j] + inst_ref[3:]
            vm = IntcodeVM(inst)
            vm.run()
            if vm.inst[0] == 19690720:
                print(100 * i + j)
                break