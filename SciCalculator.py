import math
def basicmath(first, second, call):
    if call == "1":
        value = first + second
        #value1 = round(value, 2)
        return value
    if call == "2":
        return first - second
    if call == "3":
        return first * second
    if call == "4":
        return first / second
    if call == "5":
        test = first**second
        return test
    if call == "6":
        return math.log(second, first)
def results(operation_number, result_total):
    if operation_number != 0:
        print("\nSum of calculations: " + str(result_total))
        print("Number of calculations: " + str(operation_number))
        average = result_total/operation_number
        print("Average of calculations: " + str("{:.2f}".format(average)))
    elif operation_number == 0:
        print("\nError: No calculations yet to average!")
def invalid():
    print("\nError: Invalid selection!")
    print("\nEnter Menu Selection: ", end='')
    call = input()
    return call
def main():
    current_result = 0.0
    call = "99"
    operation_number = 0
    result_total = 0.0

    while call != "0":
        print("\nCurrent Result: ", end='')
        print(current_result)
        print("\nCalculator Menu")
        print("---------------")
        print("0. Exit Program \n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Exponentiation \n6. Logarithm \n7. Display Average \n")
        print("Enter Menu Selection: ", end='')
        call = input()
        while call !='0' and call != '1' and call != '2' and call != '3' and call != '4' and call != '5' and call != '6' and call != '7':
            call = invalid()
        while call == "7":
            results(operation_number, result_total)
            print("\nEnter Menu Selection: ", end='')
            call = input()
            while call !='0' and call != '1' and call != '2' and call != '3' and call != '4' and call != '5' and call != '6' and call != '7':
                call = invalid()
        if call == "1" or call == "2" or call == "3" or call == "4" or call == "5" or call == "6":
            print("Enter first operand: ", end='')
            first_operand = input()
            if first_operand == "RESULT":
                   first_operand = current_result
            else:
                first_operand = float(first_operand)
            print("Enter second operand: ", end='')
            second_operand = input()
            if second_operand == "RESULT":
                   second_operand = current_result
            else:
                second_operand = float(second_operand)
            current_result = basicmath(first_operand, second_operand, call)
            operation_number = operation_number + 1
            result_total =float("{:.2f}".format(result_total + float(current_result)))

        if call == "0":
            print("\nThanks for using this calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()