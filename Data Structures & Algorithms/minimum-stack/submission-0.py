from xmlrpc.client import MAXINT


class MinStack:

    def __init__(self):
        self.mystack = []
        self.minstack = []
        self.minstack.append(MAXINT)

    def push(self, val: int) -> None:
        self.mystack.append(val)
        if val < self.minstack[len(self.minstack)-1]:
            self.minstack.append(val)
        else:
            self.minstack.append(self.minstack[len(self.minstack)-1])

    def pop(self) -> None:
        self.mystack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.mystack[len(self.mystack)-1]

    def getMin(self) -> int:
        return self.minstack[len(self.minstack)-1]