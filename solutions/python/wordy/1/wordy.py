def answer(question):
    if not question.startswith("What is ") or not question.endswith("?"):
        raise ValueError("syntax error")

    question = question[8:-1].strip()  # Remove "What is " from start and "?" from end
    if not question:
        raise ValueError("syntax error")

    # Replace known phrases with tokens
    question = question.replace("multiplied by", "multiplied_by")
    question = question.replace("divided by", "divided_by")

    # Split into tokens
    tokens = question.split()

    # Convert to postfix-like list of operations
    equation = []

    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token.lstrip('-').isdigit():
            equation.append(int(token))
        elif token == "plus":
            equation.append("plus")
        elif token == "minus":
            equation.append("minus")
        elif token == "multiplied_by":
            equation.append("multiplied")
        elif token == "divided_by":
            equation.append("divided")
        else:
            raise ValueError("unknown operation")
        i += 1

    if not equation or type(equation[0]) is not int:
        raise ValueError("syntax error")

    # Evaluate left to right
    result = equation[0]
    i = 1
    while i < len(equation):
        try:
            op = equation[i]
            num = equation[i + 1]
            if type(num) is not int:
                raise ValueError("syntax error")

            if op == "plus":
                result += num
            elif op == "minus":
                result -= num
            elif op == "multiplied":
                result *= num
            elif op == "divided":
                result //= num
            else:
                raise ValueError("unknown operation")
            i += 2
        except IndexError:
            raise ValueError("syntax error")

    return result
