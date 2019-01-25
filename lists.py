L=[6,5,6,8,9,0,1]
L.sort()
print(L)
L.append(10)
L.insert(2,2)
print(L)
x = 0.125
x.as_integer_ratio()
print(x.as_integer_ratio())
numbers = {'one':1, 'two':2, 'three':3}
m=numbers["two"]
print(m)
#set a new value and Key 
numbers["johnson"]=100
print(numbers)
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft() 
queue.popleft()                