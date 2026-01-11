class Numbers:
    def __init__(self, limit):
        self.limit = limit
    def __iter__(self):
        return (i for i in range(self.limit) if i % 2 == 0)
nums = Numbers(21)

for a in nums:
    print(a)