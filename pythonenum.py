from enum import Enum
class Color(Enum):
        red = 1    
        green = 2    
        blue = 3
print(Color.red)  # Color.red    print(Color(1))  # Color.red    print(Color['red'])  # Color.red 
print(Color("red"))
