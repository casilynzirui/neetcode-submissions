import math

class AreaCalc:
    # TODO: Implement calculate method
    def calculate(self, *args) -> int:
        if len(args) == 1:
            area = args[0]**2 * math.pi
            return round(area, 2)
        elif len(args) == 2:
            area = args[0] * args[1]
            return area
    

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
