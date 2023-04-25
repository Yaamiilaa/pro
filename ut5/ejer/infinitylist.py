class InfinityList:
    def __init__(self, *values: int, fill_value=None):
        self.values = list(values)
        self.fill_value = fill_value

    def __getitem__(self, index: int):
        return self.values[index]

    def __len__(self):
        return len(self.values)

    def __setitem__(self, index: int, value: int):
        for _ in range(len(self.values), index + 1):
            self.values.append(self.fill_value)
        self.values[index] = value


h = InfinityList(5, 5, 6, 8)
h[10] = 20
print(h.values)
