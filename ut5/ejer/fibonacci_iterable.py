# ******************
# FIBONACCI ITERABLE
# ******************


def run():
    class Fibonacci:
        def __init__(self):
            self.a = 0
            self.b = 1
            

        def __str__(self):
            return f'{self.a} {self.b} {self.value}'
        

    class FibonacciIterable:
        def __init__(self, num):
            self.num = num
            self.pointer = 0
            self.nums = [Fibonacci(i) for i in range(self.num)]

        def __iter__(self):
            return self

        def __next__(self):
            if self.pointer >= self.num:
                raise StopIteration
            
            nums = self.nums[self.pointer]
            self.pointer += 1
            return nums

    for nums in FibonacciIterable(1):
        print(nums)