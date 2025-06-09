# Simple calculator that evaluates user input expressions

def main():
    print("Simple Calculator (type 'exit' to quit)")
    while True:
        expr = input("Enter expression: ")
        if expr.lower() == 'exit':
            break
        try:
            result = eval(expr, {"__builtins__": None}, {})
            print("Result:", result)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()