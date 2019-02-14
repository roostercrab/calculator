def calculator(first_num, second_num, operation):
    if operation == "+":
        answer = first_num + second_num
    elif operation == "-":
        answer = first_num - second_num
    elif operation == "*":
        answer = first_num * second_num
    elif operation == "/":
        answer = first_num / second_num
    elif operation == "^":
        answer = first_num ** second_num
    else:
        print("dafug you say??\n")

    print(f"{first_num} {operation} {second_num} is {answer}\n")
    return answer


