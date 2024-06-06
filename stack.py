class Stack:
    
    def __init__(self):
        self.__items = [0] * 500
        self.__size = 0
        self.__top = -1
    
    def stack_empty(self):
        return self.__size == 0
    
    def push(self, item):
        if self.__size == len(self.__items):
            self.__items += [0] * len(self.__size) 
        self.__size += 1
        self.__top += 1
        self.__items[self.__top] = item
        
    def pop(self):
        if self.stack_empty == True:
           return "underflow"
        else:
            top = self.__items[self.__top]
            self.__top -= 1
            self.__size -= 1
            return top
        
    def peek(self):
        return self.__items[self.__top]
        
    def size(self):
       return self.__size
       
    def __str__(self):
        return self.__items[:self.__size].__str__()
             

def is_quarantines_crrect(str):
    a = Stack()
    openings = ["(", "[", "{"]
    closings = [")", "]", "}"]
    pairs = [("(",")"),("[","]"), ("{","}") ]
    for bracket in str:
        if bracket in openings:
            a.push(bracket)
        elif bracket in closings:
            if (a.pop(), bracket) not in pairs:
                return "illegal"
        else:
             return "illegal"         
    return "legals"       
           
    
a = "([{}])"
print (is_quarantines_crrect(a))
b = "jfufkuy"
print (is_quarantines_crrect(b))