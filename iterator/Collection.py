#Collections: Counter, nametuple, orderedDict, defaultDict, deque
from collections import Counter
from collections import  namedtuple
from collections import OrderedDict
from collections import defaultdict
from collections import deque

str1 = 'aaaaabbbbccc'
counter1 = Counter(str1)
print(counter1) #Counter({'a': 5, 'b': 4, 'c': 3})
print(counter1.items()) #dict_items([('a', 5), ('b', 4), ('c', 3)])
print(counter1.keys()) #dict_keys(['a', 'b', 'c'])
print(counter1.values()) #dict_values([5, 4, 3])
print(counter1.most_common(1)[0][0])
print(list(counter1.elements()))

point = namedtuple('Point', 'x,y')
pt = point(1,-4)
print(pt)
print(pt.x, pt.y)

# order_dict = OrderedDict()
order_dict = {}
order_dict['b'] = 2
order_dict['c'] = 3
order_dict['a'] = 1
order_dict['d'] = 4
print(order_dict)

d = defaultdict(float)
d['a'] = 1
d['b'] = 2
# d['c'] = list[1,2,3,4]
print(d['d'])

de = deque()
de.append(1)
de.append(2)
de.append(3)
de.appendleft(4)
de.appendleft(5)
print(de) #deque([5, 4, 1, 2, 3])
print(de.popleft()) #5
print(de) #deque([4, 1, 2, 3])
de.extend([6,7,8])
de.extendleft([1,2])
print(de) #deque([2, 1, 4, 1, 2, 3, 6, 7, 8])
de.rotate(1)
print(de) #deque([8, 2, 1, 4, 1, 2, 3, 6, 7])
de.rotate(-1)
print(de) #deque([2, 1, 4, 1, 2, 3, 6, 7, 8])