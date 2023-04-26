# ******************
# FIBONACCI ITERABLE
# ******************


def run(n: int):
    class FibonacciIterable:
        def __init__(self, num: int):
            self.num = num
            self.a = 0
            self.b = 1
            self.num = num
            self.pointer = 0

        def __str__(self):
            return f"{self.a} {self.b} {self.num}"

        def __iter__(self):
            return self

        def __next__(self):
            if self.pointer >= self.num:
                raise StopIteration

            self.r = self.a
            self.a = self.b
            self.b = self.r + self.b
            self.pointer += 1
            return self.r

    return list(FibonacciIterable(n))
