class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def next_n(self, n):
        current = self
        for _ in range(n):
            current = current.next
        return current


def build_clist(cnt, mul=1):
    order = []
    handle = Node(None)
    ptr = handle
    for line in cnt.splitlines():
        ptr.next = Node(int(line) * mul)
        ptr.next.prev = ptr
        ptr = ptr.next
        order.append(ptr)
        if ptr.data == 0:
            zero = ptr
    handle.next.prev = ptr
    ptr.next = handle.next
    return order, zero


def encode(order):
    for node in order:
        node.next.prev, node.prev.next = node.prev, node.next

        ptr = node
        if node.data > 0:
            for _ in range(abs(node.data) % (len(order) - 1)):
                ptr = ptr.next
        else:
            for _ in range(abs(node.data) % (len(order) - 1) + 1):
                ptr = ptr.prev

        node.next, node.prev = ptr.next, ptr
        node.next.prev, node.prev.next = node, node


def task1(cnt):
    order, zero = build_clist(cnt)
    encode(order)
    print(sum(zero.next_n(i).data for i in [1000, 2000, 3000]))


def task2(cnt):
    order, zero = build_clist(cnt, 811589153)
    for _ in range(10):
        encode(order)
    print(sum(zero.next_n(i).data for i in [1000, 2000, 3000]))
