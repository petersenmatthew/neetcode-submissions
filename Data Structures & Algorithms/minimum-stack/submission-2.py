class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
    # if i pop the minimum, need to know the second minimum
     # some underlying datastructure that tracks the minimum at each depth
        if not len(self.min_stack) == 0:
            self.min_stack.append(min(self.min_stack[-1], val))
        else:
            self.min_stack.append(val)
        # [6, 2, 5,]9]
        # [6, 2, 2, 2]

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
    
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
