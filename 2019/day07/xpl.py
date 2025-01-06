from dataclasses import dataclass
from enum import Enum
from itertools import permutations, cycle


class IntcodeVM:
    def __init__(self, inst):
        self.inst = inst
        self.input = []
        self.output = []
        self.ip = 0
        self.status = self.Status.INITIALIZED

    class Status(Enum):
        INITIALIZED = 0
        RUNNING = 1
        EXIT_SUCCESS = 2
        HALTED_NO_INPUT = 3

    @dataclass
    class Parameter:
        val: int
        immediate: bool

    def eval_param(self, p: Parameter):
        return p.val if p.immediate else self.inst[p.val]

    def add(self, a, b, c):
        self.inst[c.val] = self.eval_param(a) + self.eval_param(b)

    def mul(self, a, b, c):
        self.inst[c.val] = self.eval_param(a) * self.eval_param(b)

    def inp(self, a):
        if self.input:
            self.inst[a.val] = self.input.pop(0)
        else:
            self.status = self.Status.HALTED_NO_INPUT

    def out(self, a):
        self.output.append(self.eval_param(a))

    def jt(self, a, b):
        return self.eval_param(b) if self.eval_param(a) else None

    def jf(self, a, b):
        return self.eval_param(b) if not self.eval_param(a) else None

    def slt(self, a, b, c):
        self.inst[c.val] = int(self.eval_param(a) < self.eval_param(b))

    def se(self, a, b, c):
        self.inst[c.val] = int(self.eval_param(a) == self.eval_param(b))

    def ext(self):
        self.status = self.Status.EXIT_SUCCESS

    def run(self):
        self.status = self.Status.RUNNING

        while True:
            op = self.inst[self.ip]

            handler = {
                1:  self.add,
                2:  self.mul,
                3:  self.inp,
                4:  self.out,
                5:  self.jt,
                6:  self.jf,
                7:  self.slt,
                8:  self.se,
                99: self.ext
            }[op % 100]

            no_params = handler.__code__.co_argcount - 1
            params = (self.Parameter(self.inst[self.ip + i + 1], (op // 10**(2+i) % 10) == 1) for i in range(no_params))

            next_ip = handler(*params)

            if self.status != self.Status.RUNNING:
                break

            self.ip = next_ip if next_ip is not None else self.ip + no_params + 1


def task1(cnt):
    inst = list(map(int, cnt.split(',')))
    max_out = 0
    for init in permutations(range(5)):
        feed = 0
        for i in init:
            vm = IntcodeVM(inst[:])
            vm.input.extend([i, feed])
            vm.run()
            feed = vm.output.pop()
        max_out = max(max_out, feed)
    print(max_out)


def task2(cnt):
    inst = list(map(int, cnt.split(',')))
    max_out = 0
    for init in permutations(range(5, 10)):
        vms = [IntcodeVM(inst[:]) for _ in range(len(init))]

        for i in range(len(vms)):
            vms[i].input = vms[(i - 1) % len(vms)].output

        for i, init_val in enumerate(init):
            vms[i].input.append(init_val)
        vms[0].input.append(0)

        vm_iter = cycle(vms)
        while not all(vm.status == IntcodeVM.Status.EXIT_SUCCESS for vm in vms):
            next(vm_iter).run()

        max_out = max(max_out, vms[-1].output.pop())
    print(max_out)