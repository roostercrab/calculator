def calculator():
    while True:
        first_num = float(input("What is your first number? "))
        second_num = float(input("What is your second number? "))
        operation = input(
        """
        What do you want to do with those two numbers?\n
        +: add\n
        -: subtract\n
        *: multiply\n
        /: divide\n
        ^: power to\n
        
        choice: 
        """)

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
            print("dafug you say??")
            continue
    
        print(f"{first_num} {operation} {second_num} is {answer}")
        first_num = answer
        print('')