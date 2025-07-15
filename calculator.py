from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, DevOps"

if __name__ == '__main__':
    def add(a,b):
        return a+b
    
    def subtract(a,b):
        return a-b
    
    def multiply(a,b):
        return a*b
    
    def divide(a,b):
        return a/b
    
    num1 = int(input("Enter number1:"))
    num2 = int(input("Enter number2:"))
    sel = input("Choose operation among +, -, *, / :")

    if sel == "+":
        result = add(num1,num2)
        print("Result: <계산결과>",result)
    elif sel == "-":
        result = subtract(num1,num2)
        print("Result: <계산결과>",result)
    elif sel == "*":
        result = multiply(num1,num2)
        print("Result: <계산결과>",result)
    elif sel == "/":
        try:
            result = divide(num1,num2)
            print("Result: <계산결과>",result)
        except ZeroDivisionError:
            print("Error: Division by zero.")
    else:
        print("Invalid operator.")





