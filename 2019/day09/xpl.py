from collections import defaultdict
from dataclasses import dataclass
from enum import Enum


class IntcodeVM:
    def __init__(self, inst):
        self.inst = defaultdict(int) | {i: v for i, v in enumerate(inst)}
        self.input = []
        self.output = []
        self.ip = 0
        self.rel_base = 0
        self.status = self.Status.INITIALIZED

    class Status(Enum):
        INITIALIZED = 0
        RUNNING = 1
        EXIT_SUCCESS = 2
        HALTED_NO_INPUT = 3

    @dataclass
    class Parameter:
        val: int
        mode: int

    def get_val(self, p: Parameter):
        match p.mode:
            case 0:
                return self.inst[p.val]
            case 1:
                return p.val
            case 2:
                return self.inst[self.rel_base + p.val]

    def write_value(self, p: Parameter, v):
        match p.mode:
            case 0:
                self.inst[p.val] = v
            case 1:
                raise RuntimeError("Can't write to immediate parameter.")
            case 2:
                self.inst[self.rel_base + p.val] = v

    def add(self, a, b, c):
        self.write_value(c, self.get_val(a) + self.get_val(b))

    def mul(self, a, b, c):
        self.write_value(c, self.get_val(a) * self.get_val(b))

    def inp(self, a):
        if self.input:
            self.write_value(a, self.input.pop(0))
        else:
            self.status = self.Status.HALTED_NO_INPUT

    def out(self, a):
        self.output.append(self.get_val(a))

    def jt(self, a, b):
        return self.get_val(b) if self.get_val(a) else None

    def jf(self, a, b):
        return self.get_val(b) if not self.get_val(a) else None

    def slt(self, a, b, c):
        self.write_value(c, int(self.get_val(a) < self.get_val(b)))

    def se(self, a, b, c):
        self.write_value(c, int(self.get_val(a) == self.get_val(b)))

    def adb(self, a):
        self.rel_base += self.get_val(a)

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
                9:  self.adb,
                99: self.ext
            }[op % 100]

            no_params = handler.__code__.co_argcount - 1
            params = (self.Parameter(self.inst[self.ip + i + 1], op // 10**(2+i) % 10) for i in range(no_params))

            next_ip = handler(*params)

            if self.status != self.Status.RUNNING:
                break

            self.ip = next_ip if next_ip is not None else self.ip + no_params + 1


def task1(cnt):
    vm = IntcodeVM(list(map(int, cnt.split(','))))
    vm.input.append(1)
    vm.run()
    print(vm.output.pop())


def task2(cnt):
    vm = IntcodeVM(list(map(int, cnt.split(','))))
    vm.input.append(2)
    vm.run()
    print(vm.output.pop())