def split():
    qlist = question.split(" ")
    first_num = int(qlist[0])
    operation = qlist[1]
    second_num = int(qlist[2])

    answer = calculator(first_num, second_num, operation)