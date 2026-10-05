
class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.cur_index = 0
        self.furthest_index = 0

    def visit(self, url: str) -> None:
        # check if there is forward history:
        # [site1, site2, site3]
        self.cur_index += 1
        if len(self.history) < self.cur_index + 1:
            self.history.append("") # make new indice
        self.history[self.cur_index] = url
        self.furthest_index = self.cur_index

    def back(self, steps: int) -> str:
        if self.cur_index - steps < 0: # more steps to go back
            self.cur_index = 0
        else:
            self.cur_index -= steps
        return self.history[self.cur_index]

    def forward(self, steps: int) -> str:
        if self.furthest_index < (self.cur_index + steps):
            self.cur_index = self.furthest_index
        else:
            self.cur_index += steps
        return self.history[self.cur_index]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)