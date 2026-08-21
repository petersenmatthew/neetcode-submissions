class MinStack:

    def __init__(self):
        self.values = []
        self.mins = []

    def push(self, val: int) -> None:
        self.values.append(val)
        if (len(self.mins) == 0 or val <= self.mins[-1]):
            self.mins.append(val)
        
        else:
            self.mins.append(self.mins[-1])
        


    def pop(self) -> None:
        self.values.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.values[-1]

    def getMin(self) -> int:
        return self.mins[-1]
