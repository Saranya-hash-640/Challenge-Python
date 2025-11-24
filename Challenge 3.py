class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0


def is_balanced(string):
    # Dictionary for bracket pairs
    matching_brackets = {')': '(', ']': '[', '}': '{'}
    stack = Stack()

    for char in string:
        if char in "([{":   # opening bracket
            stack.push(char)
        elif char in ")]}": # closing bracket
            top = stack.pop()
            if top != matching_brackets[char]:
                return "Not Balanced"
        else:
            # Ignore letters/numbers/other chars
            continue

    return "Balanced" if stack.is_empty() else "Not Balanced"


# --------- Test Cases ----------
print(is_balanced("{[()]}"))          # Balanced
print(is_balanced("{[(])}"))          # Not Balanced
print(is_balanced("((()))"))          # Balanced
print(is_balanced("[()]{}{[()()]()}")) # Balanced
print(is_balanced("[(])"))            # Not Balanced
print(is_balanced("a+(b*c)-{d/e}"))   # Balanced

