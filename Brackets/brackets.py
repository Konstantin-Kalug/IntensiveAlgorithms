def are_brackets_correct(string: str) -> bool:
    from collections import deque
    s = string
    stack = deque()
    for i in range(len(s)):
        if len(stack) != 0 and stack[-1] == '(':
            if s[i] == ')':
                stack.pop()
            else:
                stack.append(s[i])
        elif len(stack) != 0 and stack[-1] == '[':
            if s[i] == ']':
                stack.pop()
            else:
                stack.append(s[i])
        elif len(stack) != 0 and stack[-1] == '{':
            if s[i] == '}':
                stack.pop()
            else:
                stack.append(s[i])
        elif len(stack) == 0:
            stack.append(s[i])
    if len(stack) != 0:
        return False
    else:
        return True


# https://leetcode.com/problems/valid-parentheses/
