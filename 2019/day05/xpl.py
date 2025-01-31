from dataclasses import dataclass


class IntcodeVM:
    def __init__(self, inst, input):
        self.inst = inst
        self.input = input
        self.ip = 0
        self.running = False

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
        self.inst[a.val] = self.input.pop(0)

    def out(self, a):
        print(self.eval_param(a))

    def jt(self, a, b):
        return self.eval_param(b) if self.eval_param(a) else None

    def jf(self, a, b):
        return self.eval_param(b) if not self.eval_param(a) else None

    def slt(self, a, b, c):
        self.inst[c.val] = int(self.eval_param(a) < self.eval_param(b))

    def se(self, a, b, c):
        self.inst[c.val] = int(self.eval_param(a) == self.eval_param(b))

    def ext(self):
        self.running = False

    def run(self):
        self.running = True
        while self.running:
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
            self.ip = next_ip if next_ip is not None else self.ip + no_params + 1


def task1(cnt):
    vm = IntcodeVM(list(map(int, cnt.split(','))), [1])
    vm.run()

def task2(cnt):
    vm = IntcodeVM(list(map(int, cnt.split(','))), [5])
    vm.run()