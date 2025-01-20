def is_valid(s: str) -> bool:
    stack = []
    brackets_map = {"(" : ")","{": "}","[": "]"}


    for bracket in s:
        if bracket in brackets_map:
            stack.append(bracket)
        else:
            if not stack or not bracket == brackets_map[stack.pop()]:
                return False

    if not stack:
        return True

    return False

print(is_valid( "(){}{{}}{"))