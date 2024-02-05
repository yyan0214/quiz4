from module1.function1 import greet
from module2.function2 import Mul_num
from module3.function3 import generate_fibonacci

def main():
    print(greet())

    # Using functions from module2
    num1 = 78
    num2 = 36
    print(f"The product of two numbers is {Mul_num(num1,num2)}")

    n = 12
    print(f"The first {n} Fibonacci numbers are: {generate_fibonacci(n)}")

if __name__ == "__main__":
    main()
