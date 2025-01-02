# Using iter() for custom iterators:
class Countdown:
    def __init__(self, start):
        self.start = start
    def __iter__(self):
        return self
    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        self.start -= 1
        return self.start
for number in Countdown(5):
    print(number)

# Using yield to create a generator
def generate_numbers(n):
    for i in range(n):
        yield i
for num in generate_numbers(5):
    print(num)

