def addBinary(a: str, b: str) -> str:
    a = a[::-1]
    b = b[::-1]
    result = []
    carry = 0

    for i in range(max(len(a),len(b))):
        digit_a = int(a[i]) if i < len(a) else 0
        digit_b = int(b[i]) if i < len(b) else 0
        digits_sum = digit_a + digit_b + carry
        print(digits_sum)
        res_digit = digits_sum % 2
        carry = digits_sum // 2
        result.append(res_digit)
        print(f"result = {result}")


    if carry:
        result.append("1")
    res = ""
    for char in result:
        res += f"{char}"

    return res

print(addBinary("1010","1011"))