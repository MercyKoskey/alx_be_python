# class_static_methods_demo.py

class Calculator:
    
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        #adds a and b
        return a + b

    @classmethod
    def multiply(cls, a, b):
        # Can use class variables.
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
