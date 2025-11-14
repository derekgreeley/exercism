import operator

class StackUnderflowError(Exception):
    """Raised when the stack does not have enough values for an operation."""
    pass

class Stack(list):
    def pop(self, num=1):
        if len(self) < num:
            raise StackUnderflowError("Insufficient number of items in stack")
        values = self[-num:]
        del self[-num:]
        return values if num > 1 else values[0]

    def push(self, *items):
        self.extend(items)

    def peek(self):
        val = self.pop()
        self.push(val)
        return val

def evaluate(input_data):
    stack = Stack()
    macros = {}

    for command in input_data:
        tokens = command.split()
        words = [t.lower() for t in tokens]

        i = 0
        while i < len(words):
            word = words[i]

            if word == ':':
                name = words[i + 1]
                if name.lstrip('-').isdigit():
                    raise ValueError("illegal operation")

                try:
                    end_index = words.index(';', i + 2)
                except ValueError:
                    raise ValueError("macro not terminated with ;")

                definition = words[i + 2:end_index]

                # Expand macros in the definition
                expanded = []
                for w in definition:
                    expanded.extend(macros.get(w, [w]))
                macros[name] = expanded

                i = end_index + 1
                continue

            elif word.isdigit() or (word.startswith('-') and word[1:].isdigit()):
                stack.push(int(word))

            elif word in macros:
                words = words[:i] + macros[word] + words[i + 1:]
                continue

            elif word in ('+', '-', '*', '/'):
                a, b = stack.pop(2)
                if word == '/' and b == 0:
                    raise ZeroDivisionError("divide by zero")

                operations = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.floordiv}
                stack.push(operations[word](a, b))

            elif word == 'dup':
                stack.push(stack.peek())

            elif word == 'drop':
                stack.pop()

            elif word == 'swap':
                a, b = stack.pop(2)
                stack.push(b, a)

            elif word == 'over':
                a, b = stack.pop(2)
                stack.push(a, b, a)

            else:
                raise ValueError("undefined operation")

            i += 1

    return stack
