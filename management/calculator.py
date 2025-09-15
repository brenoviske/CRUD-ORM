class Calculator:
    
    def __init__(self,n1:float,n2:float):
        self.n1  = n1
        self.n2 = n2
    

    def sum(self) -> float:
        return self.n1 + self.n2
    

    def sub(self) -> float:
        return self.n1 - self.n2
    
    def mul(self) -> float:
        return self.n1 * self.n2
    
    def div(self)-> float:
        if self.n2  == 0:
            return 'error'
        return self.n1 / self.n2
    

def num1()-> float:
    return float(input("Enter the first number:"))

def num2()-> float:
    return float(input("Enter the second number:"))


isRunning = True
while isRunning :
    op = str(input("Select your option:"))
    
    n1 = num1()
    n2 = num2()
    
    calc = Calculator(n1,n2)
    match op:
        case "+" : print(calc.sum())
        case "-": print(calc.sub())
        case "*": print(calc.mul())
        case "/": print(calc.div())
        