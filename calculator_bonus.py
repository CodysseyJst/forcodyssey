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
    
    expression = input("Enter expression:")
    tupleexp = tuple(expression.split())

    num1 = int(tupleexp[0])
    num2 = int(tupleexp[2])
    sel = tupleexp[1]

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





