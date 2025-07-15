from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, DevOps!"

if __name__ == '__main__':
    def power_calculator(a, b):    
        result = 1
        i = 0
        if 0 < b:
            while i < b:
                result *= a
                i += 1
            return result
        elif 0 > b:
            b = abs(b)
            while i < b:
                result *= a
                i += 1
            return 1/result
        else:
            return result

    while True:
        try:
            number = float(input("Enter number:"))
            global num
            num = number
            break
        except ValueError:
            print("Invalid number input.")
            continue

    while True:
        try:
            exponent = int(input("Enter number:"))
            global exp
            exp = exponent
            break
        except ValueError:
            print("Invalid exponent input.")
            continue
    
    result = power_calculator(num,exp)
    print("Result:",result)

   
