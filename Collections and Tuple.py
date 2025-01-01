# Using Counter for frequency counting:
from collections import Counter
data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
count = Counter(data)
print(count)

# Using defaultdict for handling missing keys:
from collections import defaultdict
d = defaultdict(int)
d['apple'] += 1
d['banana'] += 2
print(d)

# Using namedtuple for creating simple classes:
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)