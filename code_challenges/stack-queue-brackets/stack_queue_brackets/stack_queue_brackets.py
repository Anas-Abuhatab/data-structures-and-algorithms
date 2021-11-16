def validate_brackets(string):
    stack = []
    open_and_close = {'{':'}','[':']','(':')'}
    closing_vals = open_and_close.values()
    for x in string:
        if x in open_and_close:
            stack.append(x)
        if x in closing_vals:
            if not stack or x != open_and_close[stack.pop()]:
                return False

    return True if len(stack) == 0 else False


print(validate_brackets("[{}[jgvuyv0]((*()))]"))