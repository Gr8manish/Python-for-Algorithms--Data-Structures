def balance_check(s):
    corresponding_dict = {
        '}' : '{',
        ')': '(',
        ']': '['
    }

    stack = []

    for c in s:
        if c in corresponding_dict:
            if stack.pop() != corresponding_dict[c]:
                return False
        else:
            stack.append(c)

    return len(stack) == 0

print(balance_check('[]'))
print(balance_check('[](){([[[]]])}'))
print(balance_check('()(){]}'))
print(balance_check('[](){([[[]]])}('))
print(balance_check('[{{{(())}}}]((()))'))

# Output
# True
# True
# False
# False
# True