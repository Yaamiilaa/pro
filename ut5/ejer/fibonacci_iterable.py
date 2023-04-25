class Fibonacci:
    def __init__(self, num: int):
        self.num = num

    def __iter__(self):
        return self

    def __next__(self):
        a = 0
        print(a)
        b = 1
        print(b)

        for _ in range(self.num - 2):
            r = a + b
            a = b
            b = r
            print(r)


for nums in Fibonacci(1):
    print(nums)
