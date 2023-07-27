import sys
from calc import add, subtract, multiply, divide

def get_args():
    try:
        return (sys.argv[1], float(sys.argv[2]), float(sys.argv[3]))
    except IndexError:
        print("Not all inputs have been supplied")
        print("Correct usage is operation, start number, operation number\n")
        raise
    except:
        print("Input error found, see below for details")

def main():
    operation, start_number, operation_number = get_args()
    if operation == "add" :
        result = add(start_number, operation_number)
    elif operation == "subtract" :
        result = subtract(start_number, operation_number)
    elif operation == "multiply" :
        result = multiply(start_number, operation_number)
    elif operation == "divide" :
        result = divide(start_number, operation_number)
    else:
        raise Exception("Unsupport operation requested: '{operation}")
    print(result)
    return 0

if __name__ == "__main__":
    sys.exit(main())