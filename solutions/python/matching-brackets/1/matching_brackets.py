def is_paired(input_string):
    stack = []
    matching_pairs = {')': '(', ']': '[', '}': '{'}

    for char in input_string:
        if char in "({[":
            stack.append(char)  # Push opening brackets onto the stack
        elif char in ")}]":
            if not stack or stack[-1] != matching_pairs[char]:
                return False  # Unmatched closing bracket
            stack.pop()  # Pop the last opened bracket

    return not stack  # True if stack is empty (all brackets matched)